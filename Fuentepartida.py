import matplotlib.pyplot as plt # type: ignore
import numpy as np

# Datos
frequencies = [
    200, 500, 1000, 2000, 5000, 10000, 20000, 50000,
    100000, 200000, 500000, 1000000, 2000000
]
v1 = [1.69, 1.72, 1.75, 1.8, 1.88, 1.93, 1.95, 1.95, 1.94, 1.94, 1.99, 2.12, 2.31]
v2 = [-1.82, -1.82, -1.82, -1.82, -1.8, -1.81, -1.81, -1.81, -1.78, -1.73, -1.62, -1.57, -1.54]
v_diff = np.array(v1) - np.array(v2)

# Convertir frecuencias a escala logarítmica
frequencies_log = 20*np.log10(frequencies)

# Crear el gráfico
plt.figure(figsize=(10, 6))
#plt.plot(frequencies, v_diff , marker='o', label="Diferenciaf [V]",color= 'pink')
plt.plot(frequencies, v2, marker='s', label="V2 [V]", color='black')
plt.plot(frequencies, v1 , marker='o', label="V1 [V]",color= 'orange')


# Configuraciones del gráfico
plt.xscale('log')
plt.title("V1 V2 y diferencia")
plt.xlabel("Frecuencia [Hz] (escala logarítmica)")
plt.ylabel("Voltaje [V]")
plt.grid(which="both", linestyle="--", linewidth=0.5)
plt.legend()
plt.tight_layout()

# Mostrar el gráfico
plt.show()
