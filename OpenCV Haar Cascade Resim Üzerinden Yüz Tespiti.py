# -*- coding: utf-8 -*-
"""
Created on Mon May 13 13:45:52 2024

@author: necip
"""

import cv2
import numpy as np

img = cv2.imread("face.jpg")

yuz = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 
gri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


face = yuz.detectMultiScale(gri, 1.3, 4)

for x, y, w, h in face:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 1)
    
cv2.imshow("face", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
    