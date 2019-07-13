import numpy as np
import cv2
import sys

imagen = cv2.imread("imagen/amigos.jpg")
cas_path = 'imagen/haarcascade_frontalface_default.xml'

rostroCascade = cv2.CascadeClassifier(cas_path)

filtro = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY) 

rostros = rostroCascade.detectMultiScale(
    filtro,
    scaleFactor = 1.2,
    minNeighbors = 5,
    minSize= (30,30),
    flags = cv2.CASCADE_SCALE_IMAGE
)

for (x, y, w, h) in rostros:
    cv2.rectangle(imagen, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Rostros encontrados", imagen) 
cv2.waitKey(0) 
