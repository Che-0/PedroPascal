import cv2 as cv 
import numpy as np

img = cv.imread('photos\S.jpg') # el cero es porque es en escala de grises
cv.imshow("imagen",img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#Primer metosdo de deteccion de bordes
#laplacian (significa  que es el metodo de la segunda derivada)
lap = cv.Laplacian(gray,cv.CV_64F) #el segundo argumento es la profundidad de la imagen 
#tambien se le llama profuncidad de bits o profundidad D
#cv.CV_64F es el tipo de dato que se le va a asignar a la imagen  equivale a 64 bits
lap = np.uint8(np.absolute(lap)) #se convierte a 8 bits y se hace valor absoluto
#esto se tiene que hacer porque la imagen se convierte en negativa y se tiene que hacer positiva
cv.imshow("laplacian",lap) 


#Sobel   significa que es el metodo de la primera derivada
#Lo que hace este metodo es que basicamente calcula los gradientes en dos direcciones x  y

sobelx = cv.Sobel(gray,cv.CV_64F,1,0) # 1 es la direccion de x y 0 la de y
sobely = cv.Sobel(gray,cv.CV_64F,1,0) # 0 es la direccion de x y 1 la de y



cv.imshow("sobelx",sobelx)
cv.imshow("sobely",sobely)

# y para combinarlos

combined_sobel = cv.bitwise_or(sobelx,sobely)
cv.imshow("combined_sobel",combined_sobel)

canny = cv.Canny(gray,150,175) # 150 y 175 son los umbrales
cv.imshow("canny",canny)

# ps como explicacion el we dijo que el metodo de cany esta mas pulido que los demas
# y que es el que se usa mas comunmente, pero que los demas metodos tambien son utiles
# sobel en especial en otros casos 

cv.waitKey(0)
