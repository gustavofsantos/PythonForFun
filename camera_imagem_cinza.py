# gustavo_fernandes_dos_santos
# teste de blur, saturacao e colorizacao
# multiplas janelas
# 03-05-2013

import cv2
import cv2.cv
import cv

cam = cv2.VideoCapture(0) #inicia a captura da camera
im = cam.read() #transforma cada frame em uma imagem para ser analizada

cv2.namedWindow('original')
								#cria as janelas
cv2.namedWindow('teste')

cv2.namedWindow('blur')

while True:	
	blur = cv2.GaussianBlur(cam.read()[1], (0,0), 5)
	hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
	
	if hsv < (240, 0, 0):
		print 'adsdf'
	
	cv2.imshow('teste', hsv)
	cv2.imshow('blur', blur)
	cv2.imshow('original', c)
	
	c = cv2.waitKey(54)
	if c == 'a':
		cv2.DestroyWIndow('teste')
		break
