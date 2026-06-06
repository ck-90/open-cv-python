import cv2

imagen = cv2.imread('imagen-1.jpg')

imagen_invertida = cv2.bitwise_not(imagen)

cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.namedWindow('Invertida', cv2.WINDOW_NORMAL)
cv2.imshow('Original', imagen)
cv2.imshow('Invertida', imagen_invertida)
cv2.waitKey(0)
cv2.destroyAllWindows()