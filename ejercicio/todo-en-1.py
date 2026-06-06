import cv2

# Cargar la imagen original
imagen_original = cv2.imread("imagen-1.jpg")

# Redimensionar la imagen a 720x600 píxeles
imagen_redimensionada = cv2.resize(imagen_original, (720, 600))

# Aplicar el filtro de mediana con un kernel de tamaño 3
imagen_median_3 = cv2.medianBlur(imagen_original, 3)

# Aplicar el filtro de mediana con un kernel de tamaño 5
imagen_median_5 = cv2.medianBlur(imagen_original, 5)

# Aplicar el filtro de mediana con un kernel de tamaño 7
imagen_median_7 = cv2.medianBlur(imagen_original, 7)

# Copiar la imagen original
imagen_copiada = imagen_original.copy()

# Invertir colores
imagen_invertida = cv2.bitwise_not(imagen_original)

# Rotar la imagen original 90 grados en sentido antihorario
filas, columnas, canales = imagen_original.shape
matriz_rotacion = cv2.getRotationMatrix2D((columnas / 2, filas / 2), 90, 1)
imagen_rotada = cv2.warpAffine(imagen_original, matriz_rotacion, (columnas, filas))

# Guardar cada imagen generada con nombres descriptivos
cv2.imwrite("imagen_redimensionada.jpg", imagen_redimensionada)
cv2.imwrite("imagen_median_3.jpg", imagen_median_3)
cv2.imwrite("imagen_median_5.jpg", imagen_median_5)
cv2.imwrite("imagen_median_7.jpg", imagen_median_7)
cv2.imwrite("imagen_copiada.jpg", imagen_copiada)
cv2.imwrite("imagen_invertida.jpg", imagen_invertida)
cv2.imwrite("imagen_rotada.jpg", imagen_rotada)

# Crear ventanas redimensionables
ventanas = [
    "Imagen Redimensionada",
    "Imagen Mediana (Kernel 3)",
    "Imagen Mediana (Kernel 5)",
    "Imagen Mediana (Kernel 7)",
    "Imagen Copiada",
    "Imagen Invertida",
    "Imagen Rotada"
]

for ventana in ventanas:
    cv2.namedWindow(ventana, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(ventana, 350, 250)

# Mostrar las imágenes
cv2.imshow("Imagen Redimensionada", imagen_redimensionada)
cv2.imshow("Imagen Mediana (Kernel 3)", imagen_median_3)
cv2.imshow("Imagen Mediana (Kernel 5)", imagen_median_5)
cv2.imshow("Imagen Mediana (Kernel 7)", imagen_median_7)
cv2.imshow("Imagen Copiada", imagen_copiada)
cv2.imshow("Imagen Invertida", imagen_invertida)
cv2.imshow("Imagen Rotada", imagen_rotada)

# Posicionar las ventanas
cv2.moveWindow("Imagen Redimensionada", 100, 100)
cv2.moveWindow("Imagen Mediana (Kernel 3)", 500, 100)
cv2.moveWindow("Imagen Mediana (Kernel 5)", 900, 100)
cv2.moveWindow("Imagen Mediana (Kernel 7)", 100, 400)
cv2.moveWindow("Imagen Copiada", 500, 400)
cv2.moveWindow("Imagen Invertida", 900, 400)
cv2.moveWindow("Imagen Rotada", 1300, 250)

# Esperar hasta que se presione una tecla y luego cerrar todas las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()