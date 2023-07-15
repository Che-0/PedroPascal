import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
#cv.imshow('blue', blank)

blank[:,:] =181,126,220 # el 200:300 es el rango de pixeles que se van a pintar en el eje y y el 300:400 es el rango de pixeles que se van a pintar en el eje x
#cv.imshow('Green', blank)

cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2)
cv.imshow('Rectangle', blank)

cv.rectangle(blank, (9,10), (250,250), (240,191,191), thickness= cv.FILLED) #174,15,15
cv.imshow('Rectangleee', blank)


# Dibujar un circulo
cv.circle(blank,(100,100), 40, (13,12,12), thickness=3)
#cv.imshow('Circle', blank)

cv.circle(blank,(100,106), 6, (13,12,12), thickness=cv.FILLED)
cv.imshow('Circle dos', blank)

cv.rectangle(blank, (10,160), (80,240), (0,0,0), thickness=6)
#300,200 es la esquina superior izquierda y 0,10 es la esquina inferior derecha
cv.imshow('pico', blank)

cv.line(blank, (10,200), (80,200), (0,0,0), thickness=3)
cv.imshow('Line', blank)

cv.rectangle(blank, (150,250), (500,430), (240,191,191), thickness=cv.FILLED)
cv.imshow('cuerpo', blank)

cv.line(blank, (400,430), (400,500), (0,0,0), thickness=3)
cv.imshow('pata', blank)

cv.putText(blank, 'Cuack', (200,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,0,0), thickness=3)
#el 1.0 es el tamaño de la letra
cv.imshow('Text', blank)

gris = cv.cvtColor(blank, cv.COLOR_BGR2GRAY)
cv.imshow('gris', gris)


cv.waitKey(0)