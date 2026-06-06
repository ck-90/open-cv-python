import cv2

SP_IMG = cv2.imread("imagen-1.jpg", 0)

IMG = cv2.resize(SP_IMG, (720, 600))

IMG = IMG

Opencv_Median = cv2.medianBlur(IMG, 3)

cv2.imshow('Imagen Suavizada', Opencv_Median)
#guardamo
cv2.imwrite("imagen_suavizada.jpg", Opencv_Median)
cv2.waitKey(0)
cv2.destroyAllWindows()