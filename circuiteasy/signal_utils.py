import math

def pp_to_rms(pp: float) -> float:
    """
    Convert peak-to-peak value to RMS value.
    Args:
        pp: Peak-to-peak value.
    Returns:
        RMS value.
    """
    return round((pp / 2) / math.sqrt(2), 2)

def rms_to_pp(rms: float) -> float:
    """
    Convert RMS value to peak-to-peak value.
    Args:
        rms: RMS value.
    Returns:
        Peak-to-peak value.
    """
    return round(rms * 2 * math.sqrt(2), 2)

def rms_to_peak(rms: float) -> float:
    """
    Convert RMS value to peak value.
    Args:
        rms: RMS value.
    Returns:
        Peak value.
    """
    return round(rms * math.sqrt(2), 2)

def peak_to_rms(peak: float) -> float:
    """
    Convert peak value to RMS value.
    Args:
        peak: Peak value.
    Returns:
        RMS value.
    """
    return round(peak / math.sqrt(2), 2)

def peak_to_pp(peak: float) -> float:
    """
    Convert peak value to peak-to-peak value.
    Args:
        peak: Peak value.
    Returns:
        Peak-to-peak value.
    """
    return round(2 * peak, 2)

def pp_to_peak(pp: float) -> float:
    """
    Convert peak-to-peak value to peak value.
    Args:
        pp: Peak-to-peak value.
    Returns:
        Peak value.
    """
    return round(pp / 2, 2)

def freq_to_period(freq: float) -> float:
    """
    Convert frequency (Hz) to period (s).
    Args:
        freq: Frequency in Hz.
    Returns:
        Period in seconds.
    """
    return round(1 / freq, 2)

def period_to_freq(period: float) -> float:
    """
    Convert period (s) to frequency (Hz).
    Args:
        period: Period in seconds.
    Returns:
        Frequency in Hz.
    """
    return round(1 / period, 2)

def angular_freq_to_freq(omega: float) -> float:
    """
    Convert angular frequency (rad/s) to frequency (Hz).
    Args:
        omega: Angular frequency in rad/s.
    Returns:
        Frequency in Hz.
    """
    return round(omega / (2 * math.pi), 2)

def freq_to_angular_freq(freq: float) -> float:
    """
    Convert frequency (Hz) to angular frequency (rad/s).
    Args:
        freq: Frequency in Hz.
    Returns:
        Angular frequency in rad/s.
    """
    return round(2 * math.pi * freq, 2)
