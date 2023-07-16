import cv2 as cv
import numpy as np


img = cv.imread('Photos/S.jpg')
cv.imshow('uwu', img)


b,g,r = cv.split(img)
cv.imshow('blue', b)
cv.imshow('green', g)
cv.imshow('red', r)


print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)


#La explicacion de este pedo es simple, el split divide la imagen en sus canales de color
#y los muestra por separado, en este caso, la imagen original tiene 3 canales, por lo que
#se divide en 3 imagenes, cada una con un canal de color, en este caso, azul, verde y rojo

# y ya, en donde se vea mas blanco es porque hay una mayor cantidad de ese color en la imagen (de a cuerdo a su canal)
# y en donde se vea negro ps no habra tanto color de ese
# en el caso en el que se vea muy pinche blanco todo es porque hay poco o ni madres de color 

# Otro perro dato es que en la primera imagen (img) esta en el formato bgr cre y por eso aparece el 
# argumento 3 porque ps son 3 colores
# en los demas canales de color no aparece porque por defecto es 1 aunque no aparezca 
# el uno es en si escala de gris, la razon por la cual vemos las imagenes de los canales asi y ya

##   juntar

juntar = cv.merge([b,g,r])
cv.imshow("merge image",juntar)  # <-- y ya alv los combina 


#Pensaba que las pinches imagenes nomas se ponian una sobre otra y si jaja 
# la imagen tambien se puede construir creando una hoja en blanco con numpy  

blank  = np.zeros(img.shape[:2],dtype="uint8")   #<- este formato es para imagenes y para imprimir el color B

azul = cv.merge([b,blank,blank])
verde = cv.merge([blank,g,blank])
rojo = cv.merge([blank,blank,r])

# al hacer este pedo estamos configurando los parametros que en blanco ( a todos menos al que pongamos) claro 
# me refiero a que como en el caso de azul, el azul es el unico que tiene color y los demas estan en blanco


cv.imshow("azul",azul)
cv.imshow("verde",verde)
cv.imshow("rojo",rojo)

cv.waitKey(0)