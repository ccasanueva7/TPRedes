import numpy as np
import matplotlib.pyplot as plt

# New data points
frequencies_new = np.array([200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 
                            100000, 200000, 500000, 1000000, 2000000])  
magnitudes_new = np.array([7804.55, 7627.78, 6712.75, 4922.46, 2816.10, 
                           2037.50, 1794.44, 1672.92, 1617.68, 1500.94, 
                           1032.43, 610.87, 293.04])  

# Frequency range for the plot
freq_range = np.logspace(1, 7, 1000)  # From 10 Hz to 10 MHz

# Create the Bode plot for the new data
plt.figure(figsize=(10, 6))
plt.semilogx(frequencies_new, magnitudes_new, 'o', label='Data Points', color='green')  # Original points
plt.semilogx(freq_range, np.interp(freq_range, frequencies_new, magnitudes_new), 
             label='Interpolated Curve', color='blue')  # Interpolated curve
plt.title("Impendancia Z1")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Impedancia (Ohm)")
plt.grid(which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()
