#smoothing significa suavizado

import cv2 as cv

img = cv.imread('photos/S.jpg')
cv.imshow('Gato', img)

#average blur    average significa promedio
avareage = cv.blur(img, (3,3))
cv.imshow('Average Blur', avareage)

# Lo que hace este metodo es que toma los pixeles que estan alrededor (circundantes) de la imagen y los promedia
# y los pixeles que estan en el centro los reemplaza por el promedio de los pixeles que estan alrededor de la imagen
#cuanto mayor sea el kernel de la imagen mas desenfoque habra la imagen


#Gaussian Blur

gauss = cv.GaussianBlur(img, (3,3), 0) # el tercer parametro es la desviacion estandar en x 
cv.imshow('Gaussian Blur', gauss)      
#hace lo mismo que el metodo average exepto que en lugar de calcular todos los pixeles en el kernel

# En vez de eso, el metodo gaussian le asigna a cada pixel en ejecucion un peso determinado
# y el promedio de los productos de esos pesos da el valor para el verdader centro 
# (Este metodo tiende a obtener menos desenfoque )
# el metodo gaussian blur calcula los pixeles mas cercanos a los pixeles del centro del kernel



# Median Blur

median = cv.medianBlur(img, 7) # el 3 es por el kernel ,ya que cv asume que el kernel es un numero impar
cv.imshow('Median Blur', median)
#medianBlur no esta diseñado para tamaños de kernel grandes como 7 o 9 e incluso 5 en algunos casos 

# Es casi lo mismo que promediar, excepto que en lugar de encontrar el promedio 
# encuentra la media de los pixeles circundantes 
# ( tiende a ser mas efectivo para reducir el ruido de las imagenes  en comparacion con el promedio y gauss)
# es bastante bueno para eliminar ruidos de sal y pimienta en las imagenes 
# Se tiende a utilizar este metodo en pcerdas avanzadas y en proyectos de vision que dependen de
# una cantidad sustancial de ruido  


# Bilateral Blur 

bilateral = cv.bilateralFilter(img, 5, 15, 15) 
cv.imshow('Bilateral Blur', bilateral)         


# repecto a los parametros del metodo bilateralFilter
# el primer parametro es la imagen que se va a suavizar
# el segundo parametro es el diametro de los pixeles circundantes
# el tercer parametro es el color sigma, un mayor valor significa que los pixeles que estan mas lejos del pixel central
# tendran un mayor efecto sobre el pixel central
# el cuarto parametro es el espacio sigma, un mayor valor significa que solo los pixeles que estan mas cerca del pixel central
# tendran un mayor efecto sobre el pixel central

# Este es el mas efectivo y aveces se usa en proyectos de vision por computadora
# Tradicionalmente se usa para reducir el ruido mientras se mantiene los bordes de la imagen
# ya que los otros metodos tienden a suavizar los bordes de la imagen ( reducirlos )
# ASI QUE SE TIENE UNA IMAGEN BORROSA PERO CONSERVANDO LOS BORDES  gracias a bilateral blur
#  
cv.waitKey(0)  