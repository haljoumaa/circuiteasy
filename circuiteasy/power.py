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

def ac_active_power(
    Vrms: float = None,
    Irms: float = None,
    R: float = None,
    pf: float = None,
    phase: float = None,
    S_mag: float = None) -> float:
    """
    Calculate AC active (real) power (P) using available values.

    Possible formulas:
        - P = Vrms * Irms * pf            (if Vrms, Irms, pf given)
        - P = Vrms * Irms * cos(phase)    (if Vrms, Irms, phase given)
        - P = S_mag * pf                  (if S_mag, pf given)
        - P = S_mag * cos(phase)          (if S_mag, phase given)
        - P = Vrms^2 / R                  (if Vrms, R given, for purely resistive load)
        - P = Irms^2 * R                  (if Irms, R given, for purely resistive load)
    
    Args:
        Vrms: RMS voltage (V)
        Irms: RMS current (A)
        R: Resistance (Ohm)
        pf: Power factor (cosϕ), 0...1
        phase: Phase angle in degrees (ϕ)
        S_mag: Apparent power magnitude (VA)
    
    Returns:
        Active power P (W), rounded to 2 decimals.
    """
    if phase is not None:
        phase_rad = math.radians(phase)
        if Vrms is not None and Irms is not None:
            return round(Vrms * Irms * math.cos(phase_rad), 2)
        if S_mag is not None:
            return round(S_mag * math.cos(phase_rad), 2)
    if Vrms is not None and Irms is not None and pf is not None:
        return round(Vrms * Irms * pf, 2)
    if S_mag is not None and pf is not None:
        return round(S_mag * pf, 2)
    if Vrms is not None and R is not None:
        return round(Vrms ** 2 / R, 2)
    if Irms is not None and R is not None:
        return round(Irms ** 2 * R, 2)
    raise ValueError("Provide (Vrms, Irms, pf), (Vrms, Irms, phase), (S_mag, pf), (S_mag, phase), (Vrms, R), or (Irms, R).")


import math

def ac_reactive_power(
    Vrms: float = None,
    Irms: float = None,
    S_mag: float = None,
    phase: float = None,
    Z: float = None,
    pf: float = None,
    Vrms_phasor: complex = None,
    Irms_conjphsor: complex = None) -> complex:
    """
    Calculate AC reactive power (Q) as a complex value using available values.

    Possible formulas:
        - Q = Vrms * Irms * sin(phase)          (if Vrms, Irms, phase given)
        - Q = S_mag * sin(phase)                (if S_mag, phase given)
        - Q = S_mag * sqrt(1 - pf^2)            (if S_mag, pf given)
        - Q = Vrms^2 / Z                        (if Vrms, Z given, for purely reactive)
        - Q = Irms^2 * Z                        (if Irms, Z given, for purely reactive)
        - Q = imag(Vrms_phasor * Irms_conjphsor)        (if Vrms_phasor, Irms_conjphsor given)
    
    Args:
        Vrms: RMS voltage (V)
        Irms: RMS current (A)
        S_mag: Apparent power magnitude (VA)
        phase: Phase angle in degrees (ϕ)
        Z: Reactance (Ohm)
        pf: Power factor (cosϕ), 0...1
        Vrms_phasor: RMS voltage as a phasor (complex, must be RMS)
        Irms_conjphsor: Conjugated current phasor (complex, must be RMS)
    
    Returns:
        Reactive power Q as a complex (0 + jQ), rounded to 2 decimals.
    """
    if phase is not None:
        phase_rad = math.radians(phase)
        if Vrms is not None and Irms is not None:
            Q = Vrms * Irms * math.sin(phase_rad)
            return complex(0, round(Q, 2))
        if S_mag is not None:
            Q = S_mag * math.sin(phase_rad)
            return complex(0, round(Q, 2))
    if S_mag is not None and pf is not None:
        if not (0 <= pf <= 1):
            raise ValueError("Power factor must be between 0 and 1.")
        Q = S_mag * math.sqrt(1 - pf**2)
        return complex(0, round(Q, 2))
    if Vrms is not None and Z is not None:
        Q = Vrms ** 2 / Z
        return complex(0, round(Q, 2))
    if Irms is not None and Z is not None:
        Q = Irms ** 2 * Z
        return complex(0, round(Q, 2))
    if Vrms_phasor is not None and Irms_conjphsor is not None:
        Q = (Vrms_phasor * Irms_conjphsor).imag
        return complex(0, round(Q, 2))
    raise ValueError("Provide (Vrms, Irms, phase), (S_mag, phase), (S_mag, pf), (Vrms, Z), (Irms, Z), or (Vrms_phasor, Irms_conjphsor) for calculation.")

def ac_apparent_power(P: float = None, Q: float = None, Vrms: float = None, Irms: float = None) -> complex:
    """
    Calculate complex apparent power S.
    Either supply (P, Q) or (Vrms, Irms).
    Returns S as complex number: S = P + jQ (units: VA)
    """
    if P is not None and Q is not None:
        return complex(round(P, 2), round(Q, 2))
    if Vrms is not None and Irms is not None:
        S = Vrms * Irms
        return complex(round(S, 2), 0)
    raise ValueError("Provide (P, Q) or (Vrms, Irms) for apparent power.")


def apparent_power_magnitude(Vrms: float = None, Irms: float = None, P: float = None, Q: float = None) -> float:
    """
    Calculate apparent power magnitude |S| = sqrt(P^2 + Q^2) or Vrms * Irms.
    """
    if Vrms is not None and Irms is not None:
        return round(Vrms * Irms, 2)
    if P is not None and Q is not None:
        return round(math.sqrt(P**2 + Q**2), 2)
    raise ValueError("Provide (Vrms, Irms) or (P, Q) for S magnitude.")


def ac_apparent_power_phasors(Vrms: complex = None, Irms_conj: complex = None, Z: complex = None) -> complex:
    """
    Calculate apparent (complex) power S using phasors.
    Args:
        Vrms      : Voltage phasor (RMS, complex)
        Irms_conj : Conjugated current phasor (RMS, complex)
        Z         : Complex impedance (optional, for alternate calc)
    Returns:
        Complex apparent power S (in VA)
    Raises:
        ValueError if required arguments are missing.
    """
    if Vrms is not None and Irms_conj is not None:
        return Vrms * Irms_conj
    if Vrms is not None and Z is not None:
        S_mag = abs(Vrms)**2 / abs(Z)
        V_angle = math.degrees(math.atan2(Vrms.imag, Vrms.real))
        Z_angle = math.degrees(math.atan2(Z.imag, Z.real))
        S_angle = 2 * V_angle - Z_angle
        S = polar_to_complex(S_mag, S_angle)
        return S
    raise ValueError("Provide (Vrms, Irms_conj) for S = V·I*, or (Vrms, Z) for |S| = |V|^2/|Z|.")


def print_complex_power(S: complex):
    """
    Print apparent power in P + jQ form and as magnitude.
    """
    P = S.real
    Q = S.imag
    mag = abs(S)
    print(f" S = ({P:.2f})+ ({Q:.2f}j VA) ")
    print(f"|S| = {mag:.2f} VA \n")