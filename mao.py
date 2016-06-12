import cv
import time
import Image
import os
import pygame
pygame.init()
from pygame.mixer import Sound

#importa audio para ser usado mais tarde
audio = pygame.mixer.Sound("/usr/share/sounds/KDE-Im-Irc-Event.ogg")
 
def DetectFace(imagem, faceCascade):
 
    min_size = (20,20)
    imagem_scale = 2
    haar_scale = 1.1
    min_neighbors = 3
    haar_flags = 0
 
    # pega imagens temporarias
    grayscale = cv.CreateImage((imagem.width, imagem.height), 8, 1)
    smallImage = cv.CreateImage((cv.Round(imagem.width/imagem_scale), cv.Round(imagem.height/imagem_scale)), 8 ,1)
 
    # converte o original para cinza
    cv.CvtColor(imagem, grayscale, cv.CV_BGR2GRAY)
 
    # altera a escala para o processamento ser mais rapido
    cv.Resize(grayscale, smallImage, cv.CV_INTER_LINEAR)
 
    # equaliza o histograma
    cv.EqualizeHist(smallImage, smallImage)
 
    # detecta os olhos ou qualquer outro objeto estabelecido (HaarDetectObjects) 
    olhos = cv.HaarDetectObjects(smallImage, faceCascade, cv.CreateMemStorage(0), haar_scale, min_neighbors, haar_flags, min_size)
 
    # se sao encontrados olhos, entao:
    if olhos:
        for ((x, y, w, h), n) in olhos:
            # the input to cv.HaarDetectObjects was resized, so scale the
            # bounding box of each face and convert it to two CvPoints
            pt1 = (int(x * imagem_scale), int(y * imagem_scale))
            pt2 = (int((x + w) * imagem_scale), int((y + h) * imagem_scale))
            cv.Rectangle(imagem, pt1, pt2, cv.RGB(0, 0, 255), 5, 8, 0)
    #se nao for encontrados olhos, tocar o som estabelecido no inicio
    #else:
		#audio.play()
 
    return imagem
 
cam = cv.CaptureFromCAM(0)


# tudo que se quer detectar depende desses arquivos abaixo

#faceCascade = cv.Load("/usr/share/doc/opencv-doc/examples/haarcascades/haarcascade_frontalface_alt_tree.xml")
faceCascade = cv.Load("/media/Arquivos/py/haarcascades/frontalEyes35x16.xml")
 
while (cv.WaitKey(15)==-1):
    vid = cv.QueryFrame(cam)
    imagem = DetectFace(vid, faceCascade)
    cv.ShowImage("reconhecimendo dos olhos", imagem)
 
cv.ReleaseCapture(cam)
