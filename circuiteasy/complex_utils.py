import cmath
import math

def print_complexANDpolar(name, value):
    """
    Print a complex value in both polar (magnitude∠angle) and rectangular (a+bj) form.
    Args:
        name  : Variable name (string).
        value : Complex number.
    """
    mag, angle_rad = cmath.polar(value)
    angle_deg = math.degrees(angle_rad)
    print(f"{name}: {mag:.2f} ∠ {angle_deg:.2f}°")
    print(f"{name}: ({value.real:.2f}) + ({value.imag:.2f}j)\n")

def polar_to_complex(magnitude, angle_deg):
    """
    Convert polar form (magnitude, angle in degrees) to a complex number.
    Args:
        magnitude : Magnitude (float).
        angle_deg : Angle in degrees (float).
    Returns:
        Complex number.
    """
    angle_rad = math.radians(angle_deg)
    return magnitude * (math.cos(angle_rad) + 1j * math.sin(angle_rad))

def complex_to_polar(c):
    """
    Convert a complex number to polar form.
    Args:
        c : Complex number.
    Returns:
        Tuple (magnitude, angle_deg), both rounded to 2 decimals.
    """
    mag, angle_rad = cmath.polar(c)
    angle_deg = math.degrees(angle_rad)
    return round(mag, 2), round(angle_deg, 2)

def to_real(z):
    """
    Return the real part of a complex number z.
    Args:
        z : Complex number.
    Returns:
        Real part (float).
    """
    real_part = z.real
    return real_part
