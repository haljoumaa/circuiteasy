def series(*resistors: float) -> float:
    """
    Compute total resistance of resistors in series.
    Args:
        *resistors: Any number of resistances (Ω).
    Returns:
        Total resistance (Ω).
    """
    r_tot = round(sum(resistors), 2)
    return r_tot

def parallel(*resistors: float) -> float:
    """
    Compute total resistance of resistors in parallel.
    Args:
        *resistors: Any number of resistances (Ω).
    Returns:
        Equivalent parallel resistance (Ω).
    Prints warning and returns 0 if any resistor is 0 or negative.
    """
    if any(r == 0 for r in resistors):
        print("A resistor can't be negative or zero")
        return 0.0
    reciprocal = sum(1/r for r in resistors)
    r_par = round(1/reciprocal, 2)
    return r_par

def voltage_divider(v_in: float, r1: float, r2: float) -> float:
    """
    Compute output voltage from a simple voltage divider.
    Args:
        v_in: Input voltage (V)
        r1  : Series resistance 1 (Ω)
        r2  : Series resistance 2 (Ω)
    Returns:
        Output voltage across r2 (V)
    """
    v = round(v_in * r2 / (r1 + r2), 2)
    return v

def current_divider(I_in: float, R1: float, R2: float) -> float:
    """
    Compute current through R1 using a two-resistor current divider.
    Args:
        I_in: Total current entering parallel (A)
        R1  : Resistance R1 (Ω)
        R2  : Resistance R2 (Ω)
    Returns:
        Current through R1 (A)
    """
    i = round(I_in * R1 / (R1 + R2), 2)
    return i

def wheatstone_bridge(v_in: float, r1: float, r2: float, r3: float, r4: float) -> float:
    """
    Compute output voltage (Vout) of a Wheatstone bridge.
    Args:
        v_in: Input voltage (V)
        r1  : Resistance (Ω)
        r2  : Resistance (Ω)
        r3  : Resistance (Ω)
        r4  : Resistance (Ω)
    Returns:
        Bridge output voltage (V)
    """
    v_plus = v_in * r2 / (r1 + r2)
    v_minus = v_in * r4 / (r3 + r4)
    v = round(v_plus - v_minus, 2)
    return v
