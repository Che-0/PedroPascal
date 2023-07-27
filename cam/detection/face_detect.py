import cv2 as cv

img = cv.imread('caras/dona.jpg')
#cv.imshow('Dona', img)

#al igual que varios procesos pasados 
#la imagen se tiene que pasar a escala de grises
# la deteccion de rostros no involucra colores de piel o
# los colores presentes en la imagen 

#solo se vasa en los bordes para determinar si es o no
#una cara 


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

haar_cascade = cv.CascadeClassifier('detection/hear_face.xml')
#esta variable se crea para poder almacenar los datos que se encuentran en el archivo

face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
# detectMultiScale es el metodo que se utiliza para detectar los rostros 
# en la imagen, recibe como parametros la imagen en escala de grises
# scaleFactor es el factor de escala que se utiliza para detectar los rostros y se puede modificar
# para que detecte rostros mas pequeños o mas grandes , 1.1 es el valor por defecto pero para rostros mas pequeños
# se puede utilizar 1.05 o 1.02 y para grandes 1.4 o 1.5
# minNeighbors es el numero de vecinos que se utilizan para detectar los rostros
# entre mas alto sea el numero de vecinos mas preciso sera la deteccion de rostros
# pero tambien se puede perder la deteccion de rostros, el valor por defecto es 3
# y se puede modificar para que sea mas preciso o menos preciso

print(f'Number of faces found = {len(face_rect)}')

# ya que la variable de face_rect almacena los datos de los rostros detectados en coordenadas 
# rectangulares podemos recorrer la lista para tomar los datos de cada rostro y dibujar un rectangulo
# en cada rostro detectado

for (x,y,w,h) in face_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', img)

cv.waitKey(0)   