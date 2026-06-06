import cv2

# Cargar la imagen
imagen = cv2.imread('imagen-1.jpg')

if imagen is None:
    print("Error: No se pudo cargar la imagen.")
else:
    # Crear una copia de la imagen
    imagen_copiada = imagen.copy()

    # Crear ventanas redimensionables
    cv2.namedWindow('Imagen Original', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Imagen Copiada', cv2.WINDOW_NORMAL)


    # Mostrar imágenes
    cv2.imshow('Imagen Original', imagen)
    cv2.imshow('Imagen Copiada', imagen_copiada)

    cv2.waitKey(0)
    cv2.destroyAllWindows()