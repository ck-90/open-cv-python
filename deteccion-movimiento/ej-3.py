import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen
imagen = cv2.imread('imagen-1.jpg')

# Verificar que la imagen se cargó correctamente
if imagen is None:
    print("Error: No se pudo cargar la imagen.")
    exit()

# Convertir de BGR (OpenCV) a RGB (Matplotlib)
imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

# Separar los canales
canal_r = imagen[:, :, 2]
canal_g = imagen[:, :, 1]
canal_b = imagen[:, :, 0]

# Calcular histogramas
hist_r = cv2.calcHist([canal_r], [0], None, [256], [0, 256])
hist_g = cv2.calcHist([canal_g], [0], None, [256], [0, 256])
hist_b = cv2.calcHist([canal_b], [0], None, [256], [0, 256])

# Mostrar imagen y sus histogramas
plt.figure(figsize=(15, 8))

# Imagen original
plt.subplot(2, 2, 1)
plt.imshow(imagen_rgb)
plt.title('Imagen Original')
plt.axis('off')

# Histograma rojo
plt.subplot(2, 2, 2)
plt.title('Histograma Canal Rojo')
plt.plot(hist_r, color='red')
plt.xlim([0, 256])

# Histograma verde
plt.subplot(2, 2, 3)
plt.title('Histograma Canal Verde')
plt.plot(hist_g, color='green')
plt.xlim([0, 256])

# Histograma azul
plt.subplot(2, 2, 4)
plt.title('Histograma Canal Azul')
plt.plot(hist_b, color='blue')
plt.xlim([0, 256])

plt.tight_layout()
plt.show()