import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('photos\S.jpg')
cv.imshow('S', img)


#histogramas para escalas de grises
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])  
# respecto a los argumentos que pide, es evidente que todo lo pide en lista, pero la 
# explicacion seria la siguiente 

# [gray] = imagen de entrada, en este caso la imagen en escala de grises

# [0] = canales, en este caso solo es 1 canal, por lo que solo se pone 0 otro podria ser 
# [0,1] si se quisiera hacer un histograma de una imagen a color

# None = mascara, en este caso no se usa mascara, por lo que se pone None pero si se quisiera
# usar una mascara se pondria la mascara en este argumento

# [256] = numero de bins, en este caso se usan 256 bins, pero se puede cambiar a cualquier numero
# los bins son los contenedores en los que se guardan los pixeles

# [0,256] = rango, en este caso se usa el rango de 0 a 256, pero se puede cambiar a cualquier rango

plt.figure()  #crea una nueva figura
plt.title("Grayscale Histogram")  #titulo de la figura
plt.xlabel("Bins")  #etiqueta del eje x
plt.ylabel("# of Pixels")  #etiqueta del eje y
plt.plot(gray_hist)  #grafica el histograma
plt.xlim([0, 256])  #limites del eje x
plt.show()  #muestra la figura


cv.waitKey(0)