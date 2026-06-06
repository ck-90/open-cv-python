import cv2
import numpy as np

# Cargar la imagen
imagen = cv2.imread('imagen-1.jpg')

# Verificar que la imagen se cargó correctamente
if imagen is None:
    print("Error: No se pudo cargar la imagen.")
else:
    # Ajustar el brillo y el contraste
    alfa = 1.5  # Factor de contraste
    beta = 50   # Valor de brillo

    imagen_ajustada = cv2.convertScaleAbs(imagen, alpha=alfa, beta=beta)

    # Crear ventanas redimensionables
    cv2.namedWindow('Imagen Original', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Imagen Ajustada', cv2.WINDOW_NORMAL)

    # Mostrar imágenes
    cv2.imshow('Imagen Original', imagen)
    cv2.imshow('Imagen Ajustada', imagen_ajustada)

    cv2.waitKey(0)
    cv2.destroyAllWindows()