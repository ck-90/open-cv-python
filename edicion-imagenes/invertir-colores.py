import cv2

# Cargar la imagen
imagen = cv2.imread('imagen-1.jpg')

# Verificar que la imagen se cargó correctamente
if imagen is None:
    print("Error: No se pudo cargar la imagen.")
else:
    # Invertir los colores de la imagen
    imagen_invertida = cv2.bitwise_not(imagen)

    # Crear ventanas redimensionables
    cv2.namedWindow('Imagen Original', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Imagen Invertida', cv2.WINDOW_NORMAL)

    # Mostrar imágenes
    cv2.imshow('Imagen Original', imagen)
    cv2.imshow('Imagen Invertida', imagen_invertida)

    cv2.waitKey(0)
    cv2.destroyAllWindows()