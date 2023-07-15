#para poder cambiar el tamaño de la imagen y su escala tenemos que implementar una funcion 

#pero antes de eso tenemos que saber el por que de eso 
#por lo general las imagenes y videos de las webcams son de 720
#pero las imagenes y videos de las camaras externas son de 1080 o mas , excediendo el tamaño de la pantalla
#por lo que tenemos que cambiar el tamaño de la imagen o video para que se pueda ver en la pantalla
#para eso tenemos que usar la funcion 

import cv2 as cv

img = cv.imread('photos/an.jpg')
cv.imshow('R',img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    #shape[1] es el ancho de la imagen
    height = int(frame.shape[0]*scale)
    #shape[0] es el alto de la imagen

    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
    #interpolation es el metodo que se usa para cambiar el tamaño de la imagen
    #hay varios metodos pero el mas usado es el INTER_AREA
    #interpolation se encarga de cambiar el tamaño de la imagen o video 

resized_image = rescaleFrame(img)
cv.imshow('Resca', resized_image)
cv.waitKey(0)

    