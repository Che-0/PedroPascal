import cv2 as cv

img = cv.imread('photos/S.jpg')
cv.imshow('R', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
otra = cv.cvtColor(img,cv.COLOR_YCrCb2RGB)
cv.imshow('Gray', gray)
#cv.imshow('Otra', otra)


# Desenfocar una imagen 
# blir se nevarga de suavizar una imagen 
blur = cv.GaussianBlur(img, (65,65), cv.BORDER_DEFAULT)
#border default es un parametro que se le pone a la imagen para que se rellene con pixeles negros
# utilizando como parametro el tamaño img y el kernel
# se pone (7,7) para que sea impar y asi se pueda centrar puede ser cualquier numero impar
cv.imshow('Blur', blur)

# Edge cascade (deteccion de bordes)

canny = cv.Canny(img, 125, 175 )
# se pone 125 y 175 como parametros de umbral que significa que si el pixel es mayor a 125 se va a considerar un borde
cv.imshow('Canny', canny)
#tambien podemos poner blur como parametro de canny blur en lugar de img para que se haga mas borrosa y se detecten menos bordes
 

# diloting the image (dilatar la imagen) osea hacer mas gruesos los bordes
dilated = cv.dilate(canny, (7,7), iterations=3)
# se pone (7,7) para que sea impar y asi se pueda centrar puede ser cualquier numero impar
# se pone iterations=3 para que se haga 3 veces el proceso de dilatar
cv.imshow('Dilated', dilated)

#Eroding (erosionar) osea hacer mas delgados los bordes
eroded = cv.erode(dilated, (7,7), iterations=3)
# se pone (7,7) para que sea impar y asi se pueda centrar puede ser cualquier numero impar
# se pone iterations=3 para que se haga 3 veces el proceso de erosionar
cv.imshow('Eroded', eroded)

## Resize (redimensionar) osea cambiar el tamaño de la imagen o video
resized = cv.resize(img, (200,200), interpolation=cv.INTER_CUBIC)
# se pone (500,500) para que sea el tamaño de la imagen o video
# se pone interpolation=cv.INTER_CUBIC para que se haga una interpolacion cubica 
# esto significa que los pixeles se van a interpolar de una manera mas suave

# si queremos escalar la imagen y ampliarla podemos utilizar el siguiente codigo
#resized = cv.resize(img, (500,500), interpolation=cv.INTER_LINEAR) o
#resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)  <--- este es mas lento pero los resultados son mejores
cv.imshow('Resized', resized)



# Las imagenes son matrices por lo cual podemos amplirlas o reducirlas
# el slicing de una imagen es lo mismo que el slicing de una matriz

# Cropping (recortar) osea recortar una imagen
cropped = img[0:400, 0:100]
# se pone [50:200, 200:400] para que se recorte la imagen desde el pixel 50 hasta el 200 y desde el pixel 200 hasta el 400
cv.imshow('Cropped', cropped)

cv.waitKey(0)