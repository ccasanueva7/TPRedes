import numpy as np
import matplotlib.pyplot as plt

# Frecuencias (en Hz) en el eje X
frecuencias = np.array([200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000, 2000000])

# Valores de fase (en grados) correspondientes a cada frecuencia
fase = np.array([-8.64, -18, -28.8, -40.32, -43.2, -26, -21.6, -18, -17.28, -23.04, -45, -54, -54.72])  # Valores de fase en grados

# Crear gráfico
plt.figure(figsize=(10, 6))
plt.semilogx(frecuencias, fase, marker='o', color='g', linestyle='-', linewidth=2, markersize=6)

# Títulos y etiquetas
plt.title('Respuesta en frecuencia (Fase)', fontsize=14)
plt.xlabel('Frecuencia (Hz)', fontsize=12)
plt.ylabel('Fase (grados)', fontsize=12)
plt.grid(True, which="both", ls="--", linewidth=0.5)

# Mostrar el gráfico
plt.tight_layout()
plt.show()
