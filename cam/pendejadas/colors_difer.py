import cv2 as cv 
import matplotlib.pyplot as plt

img = cv.imread('Photos/juju.jpg')
cv.imshow('color ', img)


#plt.imshow(img)
#plt.show()



rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb_img)

plt.imshow(rgb_img)
plt.show()




cv.waitKey(0)