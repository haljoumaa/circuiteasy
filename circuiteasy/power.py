from circuiteasy.complex_utils import polar_to_complex
import math 

def dc_power(v: float = None, i: float = None, r: float = None) -> float:
    
    given = [v is not None, i is not None, r is not None].count(True)
    if given != 2:
        raise ValueError("Provide exactly two of (v, i, r) to calculate power.")
    if v is not None and i is not None:
        return round(v * i, 2)
    if i is not None and r is not None:
        return round(i ** 2 * r, 2)
    if v is not None and r is not None:
        return round(v ** 2 / r, 2)

def active_from_pf(Vrms: float, Irms: float, pf: float) -> float:
    """P = V·I·pf."""
    if not (0 <= pf <= 1):
        raise ValueError("Power factor must be between 0 and 1.")
    return Vrms * Irms * pf

def active_from_phase(Vrms: float, Irms: float, phase_rad: float) -> float:
    """P = V·I·cos(ϕ)."""
    return Vrms * Irms * math.cos(phase_rad)

def active_from_S_pf(S_mag: float, pf: float) -> float:
    """P = S·pf."""
    if not (0 <= pf <= 1):
        raise ValueError("Power factor must be between 0 and 1.")
    return S_mag * pf

def active_from_S_phase(S_mag: float, phase_rad: float) -> float:
    """P = S·cos(ϕ)."""
    return S_mag * math.cos(phase_rad)

def active_pure_resistive(Vrms: float=None, Irms: float=None, R: float=None) -> float:
    """
    Purely resistive load:
      • if R given & Vrms: P = V²/R
      • elif R given & Irms: P = I²·R
    """
    if R is None:
        raise ValueError("Resistance R is required for purely resistive calculation.")
    if Vrms is not None:
        return Vrms**2 / R
    if Irms is not None:
        return Irms**2 * R
    raise ValueError("Provide Vrms or Irms for resistive calculation.")

def reactive_from_phasors(Vrms_ph: complex, Irms_conj_ph: complex) -> float:
    """Q = Im(V·I*) in VAR."""
    return (Vrms_ph * Irms_conj_ph).imag

def reactive_from_pq(S_mag: float, power_factor: float) -> float:
    """Q = S·√(1–pf²), with 0 ≤ pf ≤ 1."""
    if not 0 <= power_factor <= 1:
        raise ValueError("Power factor must be between 0 and 1.")
    return S_mag * math.sqrt(1 - power_factor**2)

def reactive_from_magnitudes(Vrms: float, Irms: float, phase_rad: float) -> float:
    """Q = V·I·sin(ϕ)."""
    return Vrms * Irms * math.sin(phase_rad)

def reactive_pure(V: float, X: float=None, I: float=None) -> float:
    """
    Purely reactive (θ=±90°): 
      • if X provided: Q = V²/X 
      • elif I provided:   Q = I²·X
    """
    if X is not None:
        return V**2 / X
    if I is not None:
        return I**2 * X
    raise ValueError("Provide either X or I for purely-reactive Q.")


def ac_apparent_power(
    P: float = None,
    Q: float = None,
    Vrms: float = None,
    Irms: float = None,
    pf: float = None
) -> complex:
    """
    Compute complex apparent power S = P + jQ (VA).
    - Supply P and Q directly, or
    - Supply Vrms, Irms and power factor (pf = cos φ).
    """
    # Direct branch
    if P is not None and Q is not None:
        return complex(round(P,2), round(Q,2))

    # From magnitudes + power factor
    if Vrms is not None and Irms is not None and pf is not None:
        S_mag = Vrms * Irms
        φ = math.acos(pf)
        P_calc = S_mag * pf
        Q_calc = S_mag * math.sin(φ)
        return complex(round(P_calc,2), round(Q_calc,2))

    raise ValueError("Provide either (P, Q) or (Vrms, Irms, pf).")



def apparent_power_magnitude(Vrms: float = None, Irms: float = None, P: float = None, Q: float = None) -> float:
    """
    Calculate apparent power magnitude |S| = sqrt(P^2 + Q^2) or Vrms * Irms.
    """
    if Vrms is not None and Irms is not None:
        return round(Vrms * Irms, 2)
    if P is not None and Q is not None:
        return round(math.sqrt(P**2 + Q**2), 2)
    raise ValueError("Provide (Vrms, Irms) or (P, Q) for S magnitude.")

def ac_apparent_power_phasors(
    Vrms: complex = None,
    Irms_conj: complex = None,
    Z: complex = None
) -> complex:
    """
    Calculate complex apparent power S (VA) for a single component.
    
    Args:
        Vrms      : RMS voltage phasor across the component (complex).
        Irms_conj : Conjugate of the RMS current phasor through it (complex).
        Z         : Component’s complex impedance (optional).
    
    Returns:
        Complex apparent power S = V·I* (VA).
    
    Raises:
        ValueError if insufficient arguments are provided.
    """
    # Primary branch: direct phasor product
    if Vrms is not None and Irms_conj is not None:
        return Vrms * Irms_conj

    # Alternate branch: use impedance (I = V / Z)
    if Vrms is not None and Z is not None:
        # S = V·I* = V·(V/Z)* = |V|^2 / Z*
        return Vrms * (Vrms / Z).conjugate()
    
    raise ValueError(
        "Insufficient inputs: provide either (Vrms and Irms_conj) "
        "or (Vrms and Z) to compute S."
    )


def print_complex_power(S: complex):
    """
    Print apparent power in P + jQ form and as magnitude.
    """
    P = S.real
    Q = S.imag
    mag = abs(S)
    print(f" S = ({P:.2f})+ ({Q:.2f}j)VA ")
    print(f"|S| = {mag:.2f} VA \n")

def db_power(Pout, Pin):
    """
    Returnerer effektforholdet i desibel (dB) basert på utgangs- og inngangseffekt.
    Brukes når du sammenligner to effekter (W).
    Formel: 10 * log10(Pout / Pin)
    """
    if Pin == 0:
        raise ValueError("Inngangseffekten kan ikke være null.")
    return 10 * math.log10(Pout / Pin)

def db_power(Pout, Pin):
    """
    Returnerer effektforholdet i desibel (dB) basert på utgangs- og inngangseffekt.
    Brukes når du sammenligner to effekter (W).
    Formel: 10 * log10(Pout / Pin)
    """
    if Pin == 0:
        raise ValueError("Inngangseffekten kan ikke være null.")
    return 10 * math.log10(Pout / Pin)

def db_current(Iout, Iin):
    """
    Returnerer strømforholdet i desibel (dB) basert på utgangs- og inngangsstrøm.
    Brukes når du sammenligner to strømmer (A).
    Formel: 20 * log10(Iout / Iin)
    """
    if Iin == 0:
        raise ValueError("Inngangsstrømmen kan ikke være null.")
    return 20 * math.log10(Iout / Iin)
