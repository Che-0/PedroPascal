import cv2 as cv

img = cv.imread('photos/juju.jpg')
#cv.imshow('jujustu',img)

#canny significa que es un borde de la imagen
#el metodo canny se encarga de detectar los bordes de la imagen}
canny = cv.Canny(img, 50, 175)  # 125 es el valor minimo y 175 es el valor maximo
cv.imshow('canny', canny)

otro_color = cv.cvtColor(canny, cv.COLOR_BayerBG2RGB)
cv.imshow('otro_color', otro_color)
difuminando  = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('difuminando', difuminando)


dilatar_bordes = cv.dilate(canny, (3,3), iterations=5)
cv.imshow('dilatar_bordes', dilatar_bordes)

disminuir_br = cv.erode(dilatar_bordes, (3,3), iterations=5)
cv.imshow("disminuir_br", disminuir_br)


resize = cv.resize(img, (300,200), interpolation=cv.INTER_CUBIC)  
cv.imshow('resize', resize)


cv.waitKey(0)