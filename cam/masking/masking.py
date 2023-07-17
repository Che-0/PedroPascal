import cv2 as cv 
import numpy as np 

#masking esencialmente nos permite centrarnos en cierta partes de una imagen 
#

img = cv.imread("photos/S.jpg")
cv.imshow("imagen", img)

blank = np.zeros(img.shape[:2], dtype="uint8") #creamos una imagen en blanco del mismo tamaño que la imagen original
cv.imshow("Blank", blank)

maskara = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1) #creamos una mascara circular
cv.imshow("mask", maskara)
# el 1// 2   y 0//2 es para que la mascara se centre en la imagen


masked = cv.bitwise_and(img,img,mask=maskara)    #ahora si utilizamos el parametro mask 
cv.imshow("mascara",masked)


# y este pedo ps es igual para las diferentes formas, no nomas para el pinche circulo 

cv.waitKey(0)