import matplotlib.pyplot as plt

# Datos para el eje x e y
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 18, 25]

# Crear un gráfico de línea
plt.plot(x, y)

# Configurar etiquetas y título
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfico de Línea Simple')

# Mostrar el gráfico
plt.show()