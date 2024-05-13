# -*- coding: utf-8 -*-
"""
Created on Mon May 13 15:22:06 2024

@author: necip
"""

import cv2
import numpy as np

img = cv2.imread("face.jpg")
yuz = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
goz = cv2.CascadeClassifier("haarcascade_eye.xml")

gri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = yuz.detectMultiScale(gri, 1.3, 4)


for x, y, w, h in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
    
    
    img2 = img[y:y+h, x:x+h]
    gri2 = gri[y:y+h, x:x+h]
    
    gozler = goz.detectMultiScale(gri2)
    
    for x1, y1, w1, h1 in gozler:
        cv2.rectangle(img2, (x1,y1), (x1+w1, y1+h1), (0,255,0), 2)
        
cv2.imshow("resm", img)
cv2.waitKey(0)
cv2.destroyAllWindows()