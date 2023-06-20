import cv2 as cv

img = cv.imread('photos/an.jpg')
#cv.imshow('imgagenAnime', img)

# una vez que hemos leido la imagen, vamos a convertirla a escala de grises
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('imgagenAnime', gray)
 

 # Canny es un algoritmo de deteccion de bordes
canny = cv.Canny(gray, 125, 175)
cv.imshow('canny', canny)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# RETR_LIST: recupera todos los contornos, pero no crea ninguna jerarquía entre ellos.
# CHAIN_APPROX_SIMPLE: comprime los segmentos horizontales, verticales y diagonales y deja solo sus puntos finales.
#Este metodo es para encontrar los contornos de la imagen y almacenarlos en la variable contours 
print(f'{len(contours)} contornos encontrados')
cv.waitKey(0) 