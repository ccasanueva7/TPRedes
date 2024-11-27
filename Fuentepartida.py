import matplotlib.pyplot as plt
import numpy as np

# Datos
frequencies = [
    200, 500, 1000, 2000, 5000, 10000, 20000, 50000,
    100000, 200000, 500000, 1000000, 2000000
]
v1 = [1.69, 1.72, 1.75, 1.8, 1.88, 1.93, 1.95, 1.95, 1.94, 1.94, 1.99, 2.12, 2.31]
v2 = [-1.82, -1.82, -1.82, -1.82, -1.8, -1.81, -1.81, -1.81, -1.78, -1.73, -1.62, -1.57, -1.54]
v_diff = [0.13, 0.10, 0.07, 0.0, 0.08, 0.12, 0.14, 0.14, 0.16, 0.21, 0.37, 0.55, 0.77]

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(frequencies, v_diff, marker='x', label="Diferencia [V]", color='magenta')
#plt.plot(frequencies, v2, marker='s', label="V2 [V]", color='black')
#plt.plot(frequencies, v1, marker='o', label="V1 [V]", color='orange')

for freq, v, label in zip(
    [1000, 2000, 5000], 
    [v_diff[frequencies.index(1000)], v_diff[frequencies.index(2000)], v_diff[frequencies.index(5000)]],
    ["1000 Hz", "2000 Hz", "5000 Hz"]
):
    plt.annotate(
        label, 
        xy=(freq, v), 
        xytext=(freq * 1.5, v + 0.1), 
        arrowprops=dict(facecolor='black', arrowstyle="->"),
        fontsize=10, color="black"
    )


# Configuraciones del gráfico
plt.xscale('log')
plt.title("Diferencia de Voltaje")
plt.xlabel("Frecuencia [Hz] (escala logarítmica)")
plt.ylabel("Voltaje [V]")
plt.grid(which="both", linestyle="--", linewidth=0.5)
plt.legend()
plt.tight_layout()

# Mostrar el gráfico
plt.show()
