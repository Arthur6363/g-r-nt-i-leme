# -*- coding: utf-8 -*-
"""
Created on Mon May 13 15:30:53 2024

@author: necip
"""


import cv2
import numpy as np

cap = cv2.VideoCapture("video.mp4" )

yuz = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
goz = cv2.CascadeClassifier("haarcascade_eye.xml")



while True:
    ret, frame = cap.read()
    
    
    gri = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = yuz.detectMultiScale(gri, 1.3, 4)
    
    
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
        
        
        img2 = frame[y:y+h, x:x+h]
        gri2 = gri[y:y+h, x:x+h]
        
        gozler = goz.detectMultiScale(gri2)
        
        for x1, y1, w1, h1 in gozler:
            cv2.rectangle(img2, (x1,y1), (x1+w1, y1+h1), (0,255,0), 2)
        
        if ret==0:
            break
        
        cv2.imshow("sa", frame)
        if cv2.waitKey(10) & 0xFF == ord("q"):
            break
            
        
        
cap.release()
cv2.destroyAllWindows()