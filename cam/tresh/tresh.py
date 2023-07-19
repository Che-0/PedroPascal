import cv2 as cv 
import numpy as np

img = cv.imread('photos\S.jpg')
cv.imshow('S', img)

#primero tenemos que convertirla a escala de grises 

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray) 


#simple thresholding 
# 
# threshold almacena el valor de umbral que se ha aplicado, thresh es la imagen que se ha aplicado el umbral                   
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY) # 150 es el valor de umbral, 255 es el valor que 
#se le asigna a los pixeles que superan el umbral, cv.THRESH_BINARY es el tipo de umbral que se va a aplicar
cv.imshow('Simple Thresholded', thresh)

threshold, thresh_inv = cv.threshold(gray,150, 255, cv.THRESH_BINARY_INV) # 150 es el valor de umbral, 255 es el valor que 
cv.imshow('Simple Thresholded inverse', thresh_inv)

#THRESH_BINARY consiste en que los pixeles que superan el umbral se les asigna el valor de 255, y los que no se les asigna el valor de 0

# estaba pendejeando con el valor del umbral
#threshold, threshh = cv.threshold(gray, 69, 255, cv.THRESH_BINARY) # 150 es el valor de umbral, 255 es el valor que 
#se le asigna a los pixeles que superan el umbral, cv.THRESH_BINARY es el tipo de umbral que se va a aplicar
#cv.imshow('Simple', threshh)


#Adaptive thresholding
# Este consiste en que el umbral se calcula para cada pixel, es decir, no es un valor fijo para toda la imagen
adaptative_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3) 
# respecto a los argumentos de la funcion, 255 es el valor que se le asigna a los pixeles que superan el umbral,
# se pone cv.ADAPTIVE_THRESH_MEAN_C para que se calcule el umbral con la media de los pixeles vecinos,
# y thresh_binary para que se aplique el umbral binario  
# 11 es el tamaño del bloque lo que significa que se va a calcular el umbral con los 11 pixeles vecinos, 
# 3 es la constante que se le resta a la media, mientras mayor sea el numero  menor sera el umbral y por ende la imagen sera mas clara
cv.imshow('Adaptative thresholding', adaptative_thresh)




cv.waitKey(0)   

