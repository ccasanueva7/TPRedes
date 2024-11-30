import numpy as np
import matplotlib.pyplot as plt

# Data points
frequencies = np.array([200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 
                        100000, 200000, 500000, 1000000, 2000000])  # in Hz
magnitudes = np.array([-98.83, -94.08, -89.70, -85.24, -77.85, -71.97, -65.95, 
                       -58.19, -53.74, -50.88, -49.84, -49.67, -49.67])  # in dB

# Frequency range for the plot
freq_range = np.logspace(1, 7, 1000)  # From 10 Hz to 10 MHz

# Create the Bode plot
plt.figure(figsize=(10, 6))
plt.semilogx(frequencies, magnitudes, 'o', label='Data Points', color='red')  # Original points
plt.semilogx(freq_range, np.interp(freq_range, frequencies, magnitudes), 
             label='Interpolated Curve', color='blue')  # Interpolated curve
plt.title("Admitancia Y2")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Admintancia (dB)")
plt.grid(which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()
