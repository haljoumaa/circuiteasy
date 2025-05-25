import cmath
import math

class ParallelImpedance:
    """
    Represents the result of a parallel/series impedance calculation,
    with easy access to magnitude and phase.
    """
    def __init__(self, complex):
        """
        Initialize with a complex impedance value.
        """
        self.complex = complex
        self.magnitude = abs(complex)
        self.angle_deg = math.degrees(cmath.phase(complex))
        
    def __str__(self):
        """
        Return a formatted string with both rectangular and polar forms.
        """
        return (f"Complex: {self.complex.real:.2f} + j{self.complex.imag:.2f} Ω\n"
                f"Polar: Magnitude = {self.magnitude:.2f} Ω, Angle = {self.angle_deg:.2f}°")
     
    @property
    def value(self):
        """
        Get the complex value of the impedance.
        """
        return self.complex

def compute_parallel_impedance(*impedances):
    """
    Compute the total impedance of parallel-connected impedances.
    Returns a ParallelImpedance object.
    """
    complex_impedances = [complex(Z) for Z in impedances]
    reciprocal_sum = sum(1 / Z for Z in complex_impedances if Z != 0)
    if reciprocal_sum == 0:
        raise ValueError("Sum of admittances is zero, cannot compute parallel impedance.")
    Z_parallel = 1 / reciprocal_sum
    return ParallelImpedance(Z_parallel)

def series_impedance(*impedances: complex) -> complex:
    """
    Compute the total impedance of series-connected impedances.
    Returns a ParallelImpedance object.
    """
    return ParallelImpedance(sum(impedances))

def capacitor_impedance(C: float, w: float) -> complex:
    """
    Compute the impedance of a capacitor at a given angular frequency.
    Args:
        C : Capacitance in Farads.
        w : Angular frequency in rad/s.
    Returns:
        Complex impedance.
    """
    if C <= 0:
        raise ValueError("Capacitance must be positive and non-zero.")
    if w <= 0:
        raise ValueError("Angular frequency must be positive and non-zero.")

    return -1j / (w * C)

def inductor_impedance(L: float, w: float) -> complex:
    """
    Compute the impedance of an inductor at a given angular frequency.
    Args:
        L : Inductance in Henry.
        w : Angular frequency in rad/s.
    Returns:
        Complex impedance.
    """
    if L <= 0:
        raise ValueError("Inductance must be positive and non-zero.")
    if w <= 0:
        raise ValueError("Angular frequency must be positive and non-zero.")

    return 1j * w * L

def print_impedance(Z) -> None:
    """
    Print the impedance in a formatted (rectangular) form.
    Accepts either a complex number or ParallelImpedance object.
    """
    if hasattr(Z, "value"):
        Z = Z.value
    Z = complex(Z)  

    def format_impedance(Z: complex) -> str:
        R = Z.real
        X = Z.imag
        sign = '+' if X >= 0 else '-'
        return f"{R:.3f} {sign} j{abs(X):.3f} Ω"

    print(f"Impedance: {format_impedance(Z)}")

def capacitor_admittance(C: float, w: float) -> complex:
    """
    Compute the admittance of a capacitor at a given angular frequency.
    Args:
        C : Capacitance in Farads.
        w : Angular frequency in rad/s.
    Returns:
        Complex admittance.
    """
    if C <= 0 or w <= 0:
        raise ValueError("Capacitance and angular frequency must be positive and non-zero.")
    Y = 1j * w * C
    return complex(round(Y.real, 2), round(Y.imag, 2))

def inductor_admittance(L: float, w: float) -> complex:
    """
    Compute the admittance of an inductor at a given angular frequency.
    Args:
        L : Inductance in Henry.
        w : Angular frequency in rad/s.
    Returns:
        Complex admittance.
    """
    if L <= 0 or w <= 0:
        raise ValueError("Inductance and angular frequency must be positive and non-zero.")
    Y = -1j / (w * L)
    return complex(round(Y.real, 2), round(Y.imag, 2))

def resistor_admittance(R: float) -> complex:
    """
    Compute the admittance of a resistor.
    Args:
        R : Resistance in Ohms.
    Returns:
        Conductance (float).
    """
    if R <= 0:
        raise ValueError("Resistance must be positive and non-zero.")
    return round(1 / R, 2)

def admittance_to_GB(Y: complex) -> tuple[float, float]:
    """
    Split a complex admittance into its conductance (G) and susceptance (B) parts.
    Args:
        Y : Complex admittance.
    Returns:
        Tuple (G, B).
    """
    G = round(Y.real, 2)
    B = round(Y.imag, 2)
    return G, B

def conjugate(z: complex) -> complex:
    """
    Return the complex conjugate of z.
    """
    return z.conjugate()

def impedance_to_c_or_l_w(Z, omega, mode='C'):
    """
    Given |Z| and angular frequency, compute equivalent capacitance or inductance.
    Args:
        Z     : Absolute value of impedance (Ohms).
        omega : Angular frequency (rad/s).
        mode  : 'C' for capacitance, 'L' for inductance.
    Returns:
        Capacitance in Farads (if mode='C'), or inductance in Henry (if mode='L').
    """
    if omega == 0:
        print("Angular frequency must be non-zero.")
        return None
    if mode.upper() == 'C':
        C = 1 / (omega * abs(Z))
        print(f"C: {C:.3g} F")
        return C
    elif mode.upper() == 'L':
        L = abs(Z) / omega
        print(f"L: {L:.3g} H")
        return L
    else:
        print("Mode must be 'C' (capacitance) or 'L' (inductance).")
        return None
