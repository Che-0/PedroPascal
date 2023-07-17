# bitwise significa bit a bit
import cv2 as cv
import numpy as np

#img = cv.imread('Photos/S.jpg')
#cv.imshow('Cats', img)

blank = np.zeros((400,400), dtype='uint8')

rectangulo = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1) # el -1 rellena todo alv
cv.imshow('Blank Image', rectangulo)
# En la parte de 255 que es el argumento en donde se ponen los colores solo se 
# pone uno que es el blanco ya que no es una imagen de color sino una binaria



circulo = cv.circle(blank.copy(), (200,200), 200, 255, -1) #200,200 es el centro del circulo y 200 es el radio
cv.imshow('Circulo', circulo)


#primer operador bitwise    AND
bitwise_and = cv.bitwise_and(rectangulo, circulo)
cv.imshow('AND', bitwise_and)
#Muestra la INTERSECCION de las dos imagenes

#segundo operador bitwise    OR   --- interseccion
bitwise_or = cv.bitwise_or(rectangulo, circulo)
cv.imshow('OR', bitwise_or)
#Muestra la UNION de las dos imagenes

#tercer operador bitwise    XOR   --- no interseccion
bitwise_xor = cv.bitwise_xor(rectangulo, circulo)
cv.imshow('XOR', bitwise_xor)
#Muestra la DIFERENCIA de las dos imagenes osea que MUESTRA LAS PARTES EN DONDE
#NO HAY INTERSECCION 

#cuarto operador bitwise    NOT   --- inegro a blanco     y   blanco a negro 
bitwise_not = cv.bitwise_not(rectangulo)
cv.imshow('NOT', bitwise_not)
#Muestra la INVERSION de la imagen  los pixeles blancos pasan a ser negros y ps lo mismo al reves 

cv.waitKey(0)