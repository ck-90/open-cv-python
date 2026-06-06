import cv2

# Cargar la imagen
imagen = cv2.imread('imagen-1.jpg')

# Redimensionar la imagen
imagen = cv2.resize(imagen, (400, 300))

# Obtener dimensiones de la imagen
alto, ancho = imagen.shape[:2]

# Definir el ángulo de rotación
angulo_rotacion = 45

# Calcular la matriz de rotación
matriz_rotacion = cv2.getRotationMatrix2D((ancho / 2, alto / 2), angulo_rotacion, 1)

# Aplicar la rotación a la imagen
imagen_rotada = cv2.warpAffine(imagen, matriz_rotacion, (ancho, alto))

# Mostrar las imágenes
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Imagen Rotada', imagen_rotada)

# Mover las ventanas hacia el centro de la pantalla
cv2.moveWindow('Imagen Original', 500, 200)
cv2.moveWindow('Imagen Rotada', 950, 200)

cv2.waitKey(0)
cv2.destroyAllWindows()