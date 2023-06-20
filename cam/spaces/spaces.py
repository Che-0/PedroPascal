import cv2 as cv 

img = cv.imread('Photos/OIP.jpg')
cv.imshow('uwu', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

other = cv.cvtColor(img, cv.COLOR_Lab2BGR)
cv.imshow('other', other)



# Para este pedo de los colores rgb bre y esas mamadas se tiene que tener cuidado
#
cv.waitKey(0)