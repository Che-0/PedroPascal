import cv2 as cv

#mostrar camara
img = cv.imread('photos/an.jpg')
cv.imshow('imgagen', img)


griz = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('griz', griz)


#mas = cv.resize(img, (900, 900), interpolation=cv.INTER_CUBIC)
#cv.imshow('mas', mas)


#crooped = img[300:400, 0:300]
#cv.imshow('crooped', crooped)


vuelta = cv.flip(img, 1)
cv.imshow('vuelta', vuelta)


canne = cv.Canny(img, 1, 1)
cv.imshow('canne', canne)
cv.waitKey(0)