import cv2
import matplotlib.pyplot as plt

# Cargar la imagen en escala de grises
imagen = cv2.imread('imagen-1.jpg', cv2.IMREAD_GRAYSCALE)

# Calcular el histograma
histograma = cv2.calcHist([imagen], [0], None, [256], [0, 256])

# Crear figura con dos paneles
plt.figure(figsize=(10, 4))

# Imagen
plt.subplot(1, 2, 1)
plt.imshow(imagen, cmap='gray')
plt.title('Imagen')
plt.axis('off')

# Histograma
plt.subplot(1, 2, 2)
plt.plot(histograma)
plt.title('Histograma')
plt.xlabel('Valor de píxel')
plt.ylabel('Frecuencia')
plt.xlim([0, 256])

plt.tight_layout()
plt.show()