#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------
#  movimento.py
#  gustavo_fernandes_dos_santos
#	17-02-2014
# ----------------------------------------------------
#  Captura de movimento
# ----------------------------------------------------
import cv2
import cv
import numpy as np

cam = cv2.VideoCapture(0)

def diffImg(t0, t1, t2):
	d1 = cv2.absdiff(t2, t1)
	d2 = cv2.absdiff(t1, t0)
	return cv2.bitwise_and(d1, d2)
	

s, img = cam.read()

janela = 'Teste'
janela2 = 'Imagem estatica'
janela3 = 'Cor encontrada'

cv2.namedWindow(janela,cv2.CV_WINDOW_AUTOSIZE)

tzero = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
tmais = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

print("Pressione 'g' para pausar ou 'q' para sair")
i = 0
j = 0

while True:
	cv2.imshow(janela, 5*diffImg(tzero, t, tmais))
	
	tzero = t
	t = tmais
	tmais = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
	
	imag = diffImg(tzero, t, tmais)
	imag2 = np.fromstring(imag, np.uint8)

	d = cv.Scalar
	c = cv.Scalar

	for x in imag:
		imag3 = np.fromstring(imag2, np.uint8)
		d=cv.Get2D(imag3,i,j)

		if((d.val(2)==230) and (d.val(1)==230) and (d.val(0)==230)):
			c.val[2]=0 
			c.val[1]=255
			c.val[0]=0
			cv.Set2D(imag2,i,j,c) 
		i = i + 1
		j = j + 1

	cv2.imshow(janela2, imag)
	cv2.imshow(janela3, imag2)

	a = cv2.waitKey(22)

	if a == 'g':
		cv2.DestroyWindow(janela)
		break
	if a == 'q':
		cv2.DestroyWindow('Teste')
		break
