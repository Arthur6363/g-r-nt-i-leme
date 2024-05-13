# -*- coding: utf-8 -*-
"""
Created on Mon May 13 14:00:59 2024

@author: necip
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
yuz = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gri = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = yuz.detectMultiScale(gri, 1.2, 4)
    
    for x,y,w,h in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
    cv2.imshow("face", frame)
    
    
    if ret == 0:
        break
    
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break
        
    
cap.release()
cv2.destroyAllWindows()
       
    