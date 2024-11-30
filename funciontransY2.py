import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction, bode

# Coeficientes de la función de transferencia ajustados
numerator = [1, 0]  # Numerador: s
denominator = [200, 2 * np.pi * 10e5]  # Denominador ajustado para que la frecuencia de corte esté en 10^5 Hz

# Crear la función de transferencia
system = TransferFunction(numerator, denominator)

# Rango de frecuencias (logarítmico) para análisis
frequencies = np.logspace(1, 7, 500)  # De 10 Hz a 100 MHz
w, mag, phase = bode(system, w=frequencies )  # Convertir Hz a rad/s

# Graficar módulo y fase
plt.figure(figsize=(12, 8))

# Magnitud (Módulo)
plt.subplot(2, 1, 1)
plt.semilogx(frequencies, mag)  # Escala logarítmica en frecuencia
plt.title('Respuesta en frecuencia de Y2(s)')
plt.ylabel('Magnitud [dB]')
plt.grid(which='both', linestyle='--', linewidth=0.7)

# Fase
plt.subplot(2, 1, 2)
plt.semilogx(frequencies, phase)  # Escala logarítmica en frecuencia
plt.ylabel('Fase [°]')
plt.xlabel('Frecuencia [Hz]')
plt.grid(which='both', linestyle='--', linewidth=0.7)

plt.tight_layout()
plt.show()
