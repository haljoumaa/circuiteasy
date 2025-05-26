import math
import matplotlib.pyplot as plt
import numpy as np

def cutoff_freq_RC(R, C):
    """
    Returnerer grensefrekvensen (f_c og ω_c) for RC lavpass/høypassfilter.
    f_c = 1/(2πRC), ω_c = 1/(RC)
    """
    fc = 1 / (2 * math.pi * R * C)
    wc = 1 / (R * C)
    return fc, wc

def cutoff_freq_RL(R, L):
    """
    Returnerer grensefrekvensen (f_c og ω_c) for RL lavpass/høypassfilter.
    f_c = R/(2πL), ω_c = R/L
    """
    fc = R / (2 * math.pi * L)
    wc = R / L
    return fc, wc

def bode_plot_first_order(R, C=None, L=None, filter_type='RC_lowpass', Vin=1):
    """
    Plott Bode-magnitude og -fase for førsteordens RC eller RL filter.
    Hvis Vin oppgis, vises Vout = |H| * Vin både i dB og volt.
    """
    freqs = np.logspace(1, 6, 500)
    w = 2 * np.pi * freqs

    if filter_type.startswith('RC'):
        if C is None:
            raise ValueError("C must be provided for RC filter.")
        if filter_type == 'RC_lowpass':
            H = 1 / (1 + 1j * w * R * C)
        elif filter_type == 'RC_highpass':
            H = (1j * w * R * C) / (1 + 1j * w * R * C)
    elif filter_type.startswith('RL'):
        if L is None:
            raise ValueError("L must be provided for RL filter.")
        if filter_type == 'RL_lowpass':
            H = R / np.sqrt(R**2 + (w*L)**2) * np.exp(-1j * np.arctan(w*L/R))
        elif filter_type == 'RL_highpass':
            H = (1j * w * L) / (R + 1j * w * L)
    else:
        raise ValueError("filter_type må være 'RC_lowpass', 'RC_highpass', 'RL_lowpass' eller 'RL_highpass'.")

    magnitude = 20 * np.log10(np.abs(H))
    phase = np.angle(H, deg=True)
    Vout_abs = np.abs(H) * Vin
    Vout_db = 20 * np.log10(Vout_abs)

    plt.figure(figsize=(10,8))
    plt.subplot(3,1,1)
    plt.semilogx(freqs, magnitude)
    plt.ylabel('Magnitude [dB]')
    plt.title(f'Bode plot - {filter_type}')
    plt.grid(True, which='both', linestyle='--')

    plt.subplot(3,1,2)
    plt.semilogx(freqs, phase)
    plt.ylabel('Phase [degrees]')
    plt.grid(True, which='both', linestyle='--')

    plt.subplot(3,1,3)
    plt.semilogx(freqs, Vout_abs, label='|Vout| [V]')
    plt.semilogx(freqs, Vout_db, label='|Vout| [dB]')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Output')
    plt.legend()
    plt.grid(True, which='both', linestyle='--')

    plt.tight_layout()
    plt.show()
