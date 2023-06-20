import cv2 as cv
from numpy import float32
img = cv.imread('photos/an.jpg')
cv.imshow('imgagenAnime', img)
nueva = cv.resize(img, (200, 200), interpolation=cv.INTER_CUBIC)
cv.imshow('nueva', nueva)



# Translation (traslacion) 
def translate(img, x, y):
    transMat = float32([[1, 0, x], [0, 1, y]]) # Matriz de traslacion
    # 1 = no se mueve, 0 = no se mueve, x = pixeles a mover en x, y = pixeles a mover en y
    dimensions = (img.shape[1], img.shape[0]) # Dimensiones de la imagen 1 = ancho, 0 = alto
    return cv.warpAffine(img, transMat, dimensions) # Aplicamos la traslacion

# -x --> Izquierda
# -y --> Arriba
# x --> Derecha
# y --> Abajo

translated = translate(img, 100, 100)
cv.imshow('translated', translated)

# Rotation (rotacion) Este tambien es un desmadre
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2] # Obtenemos el alto y ancho de la imagen
    if rotPoint is None:
        rotPoint = (width//2, height//2) # Si no se especifica el punto de rotacion, se toma el centro
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0) # Matriz de rotacion, el 1.0 es el scale
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow('rotated', rotated)


## flipping (voltear)
flip = cv.flip(img, -1) # 0 = voltear verticalmente, 1 = voltear horizontalmente, -1 = voltear ambos
cv.imshow('flip', flip)


# Cropping (recortar)
cropped = img[0:400, 300:400] # Recortamos la imagen
#0:400 = alto, 300:400 = ancho
cv.imshow('cropped', cropped)

cv.waitKey(0)
