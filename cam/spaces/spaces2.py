import cv2 as cv
import matplotlib.pyplot as plt
 
img = cv.imread('Photos/OIP.jpg')
cv.imshow('uwu', img)

plt.imshow(img)
plt.show()


#Las imagenes son de diferentes colores porque 
# una es BGR y la otra es RGB 

#matplotlib no sabe que es bgr porque este utiliza el 
# formato rgb 

# La forma en la que se puede convertir el formato 
# de una imagen es con el metodo cv.cvtColor()


#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

plt.imshow(rgb)
plt.show()


#Por todo lo visto es que tenemos que tener cuidado cuando 
# trabajemos con dos librerias distintas 
# por la inversion de color de las imagenes y el resultado que 
# causara una l;ibreria en otra RGB 2 BGR y BGR 2 CV2 
cv.waitKey(0)