import cv2
import tkinter as tk
from tkinter import Entry, Button

# Función para aplicar el filtro de mediana con el valor ingresado
def apply_median_filter():
    kernel_size = entry.get()

    try:
        kernel_size = int(kernel_size)

        if kernel_size % 2 == 1 and 3 <= kernel_size <= 100:
            Opencv_Median = cv2.medianBlur(IMG, kernel_size)
            cv2.imshow('Imagen Suavizada', Opencv_Median)
        else:
            print("El valor debe ser un número impar entre 3 y 100.")

    except ValueError:
        print("Por favor, ingresa un número válido.")

# Cargar la imagen en escala de grises
SP_IMG = cv2.imread("imagen-1.jpg", 0)

if SP_IMG is None:
    print("Error: No se pudo cargar la imagen.")
    exit()

IMG = cv2.resize(SP_IMG, (720, 600))

# Crear una ventana de Tkinter
root = tk.Tk()
root.title("Ajuste del Kernel del Filtro de Mediana")

# Crear una entrada de texto para ingresar el tamaño del kernel
entry = Entry(root)
entry.insert(0, "3")  # Valor predeterminado
entry.pack()

# Crear un botón para aplicar el filtro de mediana
button = Button(root,
                text="Aplicar Filtro de Mediana",
                command=apply_median_filter)
button.pack()

# Mostrar la imagen suavizada inicialmente
Opencv_Median = cv2.medianBlur(IMG, 3)
cv2.imshow('Imagen Suavizada', Opencv_Median)

# Iniciar el bucle principal de Tkinter
root.mainloop()

# Cerrar ventanas de OpenCV
cv2.destroyAllWindows()