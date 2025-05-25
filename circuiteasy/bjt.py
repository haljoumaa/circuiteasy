import matplotlib.pyplot as plt
import numpy as np

def print_si(var_name, var, precision=3):
    """
    Print a variable's value with its name and SI prefix (auto-scaled).
    Args:
        var_name : Name of the variable (string).
        var      : Numeric value to print.
        precision: Number of significant digits (default: 3).
    Example:
        print_si('Ic', 0.0032)  # Output: Ic: (3.2)m
    """
    import math
    SI_PREFIXES = {
        -24: 'y', -21: 'z', -18: 'a', -15: 'f', -12: 'p', -9: 'n',
        -6: 'μ', -3: 'm', 0: '', 3: 'k', 6: 'M', 9: 'G', 12: 'T',
        15: 'P', 18: 'E', 21: 'Z', 24: 'Y'
    }
    if var == 0:
        magnitude = 0
    else:
        magnitude = int(math.floor(math.log10(abs(var)) / 3) * 3)
    magnitude = max(min(magnitude, max(SI_PREFIXES)), min(SI_PREFIXES))
    prefix = SI_PREFIXES[magnitude]
    scaled = var / (10 ** magnitude)
    print(f"{var_name}: ({scaled:.{precision}g}){prefix}\n")

def find_re(Ie=None, Ic=None, gm=None, Vt=0.026):
    """
    Compute small-signal re for BJT.
    Priority: gm > Ie > Ic. Requires at least one of these.
    Vt defaults to 0.026 V.
    Args:
        Ie : Emitter current (A).
        Ic : Collector current (A).
        gm : Transconductance (S).
        Vt : Thermal voltage (V), default 0.026 V.
    Returns:
        re (Ω)
    """
    if gm is not None and gm != 0:
        re = 1 / gm
        print(f"re (gm): {re:.3g} Ω")
        return re
    elif Ie is not None and Ie != 0:
        re = Vt / Ie
        print(f"re (Ie): {re:.3g} Ω")
        return re
    elif Ic is not None and Ic != 0:
        re = Vt / Ic
        print(f"re (Ic): {re:.3g} Ω")
        return re
    else:
        print("Error: Must provide gm, Ie, or Ic (nonzero).")
        return None
    
def find_rpi(beta=None, Ie=None, Ic=None, gm=None, Vt=0.026):
    """
    Compute small-signal r_pi for BJT.
    Priority: (gm & beta) > (Ie & beta) > (Ic & beta).
    Vt defaults to 0.026 V.
    Args:
        beta: Current gain (dimensionless).
        Ie  : Emitter current (A).
        Ic  : Collector current (A).
        gm  : Transconductance (S).
        Vt  : Thermal voltage (V), default 0.026 V.
    Returns:
        rpi (Ω)
    """
    if beta is None:
        print("Error: Must provide beta.")
        return None
    if gm is not None and gm != 0:
        rpi = beta / gm
        print(f"r_pi (gm): {rpi:.2g} Ω")
        return rpi
    elif Ie is not None and Ie != 0:
        rpi = beta * Vt / Ie
        print(f"r_pi (Ie): {rpi:.3g} Ω")
        return rpi
    elif Ic is not None and Ic != 0:
        rpi = beta * Vt / Ic
        print(f"r_pi (Ic): {rpi:.3g} Ω")
        return rpi
    else:
        print("Error: Must provide (gm, Ie, or Ic) in addition to beta.")
        return None

def find_gm(Ic=None, Ie=None, Vt=0.026):
    """
    Compute BJT transconductance gm.
    Priority: Ic > Ie. Requires at least one of Ic or Ie.
    Vt defaults to 0.026 V (room temp).
    Args:
        Ic : Collector current (A).
        Ie : Emitter current (A).
        Vt : Thermal voltage (V), default 0.026 V.
    Returns:
        gm (S)
    """
    if Ic is not None:
        gm = Ic / Vt
        print(f"gm (Ic): {gm:.3g} S")
        return gm
    elif Ie is not None:
        gm = Ie / Vt
        print(f"gm (Ie): {gm:.3g} S")
        return gm
    else:
        print("Error: Must provide Ic or Ie.")
        return None

def plot_bjt_loadline_and_qpoint(Ic, Vce, Vcesat, Icmax, Vcemax=None):
    """
    Plots BJT output characteristics and marks Q-point, cutoff, saturation, and active regions.
    Args:
        Ic     : Collector current at Q-point (A).
        Vce    : Collector-emitter voltage at Q-point (V).
        Vcesat : Collector-emitter saturation voltage (V).
        Icmax  : Maximum collector current (A, for axis scaling).
        Vcemax : Maximum Vce (V, for axis scaling). If None, auto-calculated.
    """
    if Vcemax is None:
        Vcemax = max(2*Vce, 5*Vcesat)
    vce = np.linspace(0, Vcemax, 200)
    load_line = Icmax - (Icmax/Vcemax)*vce

    plt.figure(figsize=(7,5))
    
    # Regions
    cutoff_ic = Icmax * 0.07  # ~7% of Icmax
    plt.axhspan(0, cutoff_ic, color='red', alpha=0.10, label='Cutoff')
    plt.axvspan(0, Vcesat, color='orange', alpha=0.15, label='Saturation')
    plt.axvspan(Vcesat, Vcemax, color='green', alpha=0.07, label='Active')
    
    # Load line and Q-point
    plt.plot(vce, load_line, 'b-', label='Load Line')
    plt.plot(Vce, Ic, 'ro', label='Q-point')
    
    # Boundaries
    plt.axvline(Vcesat, color='orange', linestyle='--', linewidth=1)
    plt.axhline(0, color='gray', linestyle='--', linewidth=1)
    
    # Annotate regions
    plt.text(Vcemax*0.85, cutoff_ic*0.7, 'Cutoff', color='red', fontsize=10)
    plt.text(Vcesat*0.2, Icmax*0.8, 'Saturation', color='orange', fontsize=10, rotation=90)
    plt.text(Vcesat+Vcemax*0.05, Icmax*0.8, 'Active', color='green', fontsize=10)

    plt.title('BJT Output Regions & Q-point')
    plt.xlabel('$V_{CE}$ (V)')
    plt.ylabel('$I_C$ (A)')
    plt.ylim(0, Icmax*1.1)
    plt.xlim(0, Vcemax)
    plt.grid(True, which='both', linestyle='--', alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()


def bjt_currents(beta, Ic=None, Ie=None, Ib=None):
    """
    Universal BJT current converter.
    Provide exactly one of Ic, Ie, or Ib (in Amps), and beta.
    Calculates and prints all three currents.
    Args:
        beta: Current gain (dimensionless).
        Ic  : Collector current (A).
        Ie  : Emitter current (A).
        Ib  : Base current (A).
    Returns:
        dict with keys 'Ic', 'Ib', 'Ie'
    """
    if sum(x is not None for x in [Ic, Ie, Ib]) != 1:
        print("Error: Provide exactly one of Ic, Ie, or Ib.")
        return None

    if Ic is not None:
        Ib_calc = Ic / beta
        Ie_calc = Ic * (beta + 1) / beta
        print(f"Ic: {Ic:.3g} A")
        print(f"Ib: {Ib_calc:.3g} A")
        print(f"Ie: {Ie_calc:.3g} A")
        return {'Ic': Ic, 'Ib': Ib_calc, 'Ie': Ie_calc}
    elif Ie is not None:
        Ic_calc = Ie * beta / (beta + 1)
        Ib_calc = Ie / (beta + 1)
        print(f"Ie: {Ie:.3g} A")
        print(f"Ic: {Ic_calc:.3g} A")
        print(f"Ib: {Ib_calc:.3g} A")
        return {'Ie': Ie, 'Ic': Ic_calc, 'Ib': Ib_calc}
    elif Ib is not None:
        Ic_calc = beta * Ib
        Ie_calc = Ib * (beta + 1)
        print(f"Ib: {Ib:.3g} A")
        print(f"Ic: {Ic_calc:.3g} A")
        print(f"Ie: {Ie_calc:.3g} A")
        return {'Ib': Ib, 'Ic': Ic_calc, 'Ie': Ie_calc}
