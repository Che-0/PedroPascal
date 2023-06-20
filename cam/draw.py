import cv2 as cv
import numpy as np 

img = cv.imread('photos/S.jpg')
cv.imshow('R', img)

#blank = np.zeros(img.shape[:2], dtype='uint8')
#crea una imagen en blanco del mismo tamaño que la imagen original
#dtype es el tipo de dato que va a tener la imagen en este caso es uint8 que es un entero sin signo de 8 bits 

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('blue', blank)


#pintar la imagen de un color
#blank[200:300, 300:600] = 0,0,255 # el 200:300 es el rango de pixeles que se van a pintar en el eje y y el 300:400 es el rango de pixeles que se van a pintar en el eje x
#cv.imshow('Green', blank)


# Dibujar un rectangulo
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2)
#el primer argumento es la imagen en la que se va a dibujar (en este caso es blank)
#el segundo argumento es la esquina superior izquierda del rectangulo (en este caso es (0,0)
#el tercer argumento es la esquina inferior derecha del rectangulo(en este caso es (250,250)
#el cuarto argumento es el color del rectangulo(en este caso es (0,255,0) que es verde)
#el quinto argumento es el grosor del rectangulo(en este caso es 2) tambien podemos poner cv.FILLED para que se rellene el rectangulo o poner -1 en el grosor

#En el caso del tercer argumento de 250,250 se podria poner blank.shape[1]//2, blank.shape[0]//2 para que el rectangulo sea la mitad de grande que la imagen original
cv.imshow('Rectangle', blank)


# Dibujar un circulo
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)
cv.imshow('Circle', blank)

# Dibujar una linea

cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
cv.imshow('Line', blank)


# Escribir 
cv.putText(blank, 'HUevooos', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow('Text', blank)

cv.waitKey(0)
cv.destroyAllWindows()

