import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread('photos\S.jpg')
cv.imshow('S', img)

blank = np.zeros(img.shape[:2], dtype='uint8')


circulo = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2) , 100, 255, -1)
cv.imshow('Circulo', circulo)

mask = cv.bitwise_and(img, img, mask=circulo)
cv.imshow('Mask', mask)

color = ('b', 'g', 'r')

for i, col in enumerate(color):
    hist =cv.calcHist([img], [i], circulo, [256], [0, 256])
    plt.plot(hist, color=col) 
    plt.xlim([0, 256])
plt.show()

cv.waitKey(0)