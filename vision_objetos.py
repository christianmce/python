import numpy as np
import cv2

original = cv2.imread("imagen/monedas.jpg")
cv2.imshow("original", original)
 
# Convertimos a escala de grises
gris = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
 
# Aplicar suavizado Gaussiano
gauss = cv2.GaussianBlur(gris, (5,5), 0)
 
cv2.imshow("suavizado", gauss)

canny = cv2.Canny(gauss, 50, 150)
 
cv2.imshow("canny", canny)

(_,contornos,h) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
 
print("He encontrado {} objetos".format(len(contornos)))
 
cv2.drawContours(original,contornos,-1,(0,0,255), 2)
cv2.imshow("contornos", original)
 
cv2.waitKey(0)
