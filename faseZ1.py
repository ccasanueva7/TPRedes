import numpy as np
import matplotlib.pyplot as plt

# Desplazamientos en el tiempo (en segundos)
delta_t = np.array([1280e-6, 500e-6, 250e-6, 120e-6, 47e-6, 22e-6, 10.8e-6, 3.5e-6, 
                    1.32e-6, 440e-9, 80e-9, 20e-9, 5e-9])  # µs y ns convertidos a segundos

# Fase (en grados)
fase = np.array([89.28, 90, 90, 86.4, 84.6, 79.2, 77.76, 63, 47.52, 31.68, 14.4, 7.2, 3.6])

# Calcular las frecuencias correspondientes
frecuencias = 1 / delta_t  # f = 1 / Δt

# Crear gráfico
plt.figure(figsize=(10, 6))
plt.semilogx(frecuencias, fase, marker='o', color='r', linestyle='-', linewidth=2, markersize=6)

# Títulos y etiquetas
plt.title('Respuesta en frecuencia (Fase)', fontsize=14)
plt.xlabel('Frecuencia (Hz)', fontsize=12)
plt.ylabel('Fase (grados)', fontsize=12)
plt.grid(True, which="both", ls="--", linewidth=0.5)

# Mostrar el gráfico
plt.tight_layout()
plt.show()
