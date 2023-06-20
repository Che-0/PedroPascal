import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    #shape[1] es el ancho de la imagen
    height = int(frame.shape[0]*scale)
    #shape[0] es el alto de la imagen

    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changesRes(width, height):
    #solo funciona con live video
    capture.set(3, width) 
    capture.set(4, height)

#leer una imagen
#img = cv.imread('photos/R.jpg')
#cv.imshow('R', img)
#cv.waitKey(0)

##leer un video
capture = cv.VideoCapture('videos/pet_-_20830 (360p).mp4')
# aqui en la parte del argumento se puede poner un numero que es el id de la camara
#generalmente el 0 es la camara de la computadora y el 1 es la camara externa
#para leer un video se pone el nombre del video o la ruta del video

while True:
    isTrue, frame = capture.read()
    #isTrue es una variable que nos dice si se esta leyendo el video
    #frame es el frame del video
    
    frame_resized = rescaleFrame(frame, scale=.2)

    cv.imshow('Video', frame)
    cv.imshow('Video resized', frame_resized)
    #muestra el frame del video
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    #si se presiona la tecla d se cierra el video

capture.release()
#libera la camara o el video
cv.destroyAllWindows()
#cierra todas las ventanas

cv.waitKey(0)
#espera a que se presione una tecla para cerrar la ventana