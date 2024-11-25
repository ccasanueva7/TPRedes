
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import TransferFunction, bode

# Coeficientes de la función de transferencia ajustados con 10^6
numerator = [33.93, 33.93 * (50968.26 + 125663706), 33.93 * 50968.26 * 125663706]
denominator = [
    1,
    (10053.1 + 2.51327412e6),  # Usando notación exponencial para 2.51327412 * 10^6
    10053.1 * 2.51327412e6
]

# Crear la función de transferencia
system = TransferFunction(numerator, denominator)

# Rango de frecuencias (logarítmico) para análisis
frequencies = np.logspace(1, 8, 500)  # De 10 Hz a 100 MHz
w, mag, phase = bode(system, w=frequencies * 2 * np.pi)  # Convertir Hz a rad/s

# Graficar módulo y fase
plt.figure(figsize=(12, 8))

# Magnitud (Módulo)
plt.subplot(2, 1, 1)
plt.semilogx(frequencies, mag)  # Escala logarítmica en frecuencia
plt.title('Respuesta en frecuencia de Z1(s) ')
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
