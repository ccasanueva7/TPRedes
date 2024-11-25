import numpy as np
import matplotlib.pyplot as plt

# Frecuencias (en Hz) en el eje X
frecuencias = np.array([200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000, 2000000])

# Voltajes de salida (en V) correspondientes a cada frecuencia
voltaje_salida = np.array([8e-3, 13.8e-3, 22.8e-3, 38e-3, 88e-3, 170e-3, 328e-3, 728e-3, 1.1, 1.4, 1.52, 1.54, 1.54])  # Voltajes de salida en V
voltaje_entrada = 3.5  # Voltaje de entrada en V

# Cálculo del módulo en dB para cada voltaje de salida, usando valor absoluto para evitar resultados negativos
ganancia_db = 20 * np.log10(np.abs(voltaje_salida / voltaje_entrada))
# Imprimir los valores del módulo en dB para cada frecuencia
print("Frecuencia (Hz) | Módulo (dB)")
print("-----------------|-------------")
for f, db in zip(frecuencias, ganancia_db):
    print(f"{f:15} | {db:12.2f}")
# Crear gráfico
plt.figure(figsize=(10, 6))
plt.semilogx(frecuencias, ganancia_db, marker='o', color='magenta', linestyle='-', linewidth=2, markersize=6)
# Para 200 Hz
plt.annotate(f'200 Hz', xy=(200, ganancia_db[0]), xytext=(200, ganancia_db[0] + 10),
             arrowprops=dict(facecolor='red', shrink=0.05), fontsize=12, color='red')

# Para 2 MHz
plt.annotate(f'2 MHz', xy=(2000000, ganancia_db[-1]), xytext=(2000000, ganancia_db[-1] + 10),
             arrowprops=dict(facecolor='red', shrink=0.05), fontsize=12, color='red')

# Títulos y etiquetas
plt.title('Respuesta en frecuencia (Módulo) en dB', fontsize=14)
plt.xlabel('Frecuencia (Hz)', fontsize=12)
plt.ylabel('Ganancia (dB)', fontsize=12)
plt.grid(True, which="both", ls="--", linewidth=0.5)

# Mostrar el gráfico
plt.tight_layout()
plt.show()
