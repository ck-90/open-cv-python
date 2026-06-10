import cv2
import matplotlib.pyplot as plt

# Cargar imagen a color
IMG = cv2.imread("imagen-1.jpg")

# Verificar que se cargó correctamente
if IMG is None:
    print("Error: No se pudo cargar la imagen.")
    exit()

# Convertir de BGR a RGB para Matplotlib
IMG_RGB = cv2.cvtColor(IMG, cv2.COLOR_BGR2RGB)

# Tamaño del kernel
kernel_size = input("Ingrese el tamaño del kernel (número impar, 3-100): ")
kernel_size = int(kernel_size)

# Aplicar filtro de mediana
suavizada = cv2.medianBlur(IMG, kernel_size)

# Convertir también la imagen suavizada a RGB
suavizada_RGB = cv2.cvtColor(suavizada, cv2.COLOR_BGR2RGB)

# Mostrar imágenes
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(IMG_RGB)
plt.title("Imagen Original")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(suavizada_RGB)
plt.title(f"Imagen Suavizada (Kernel={kernel_size})")
plt.axis("off")

plt.show()