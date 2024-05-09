# -*- coding: utf-8 -*-
"""
Created on Thu May  9 14:51:30 2024

@author: necip
"""

import cv2
import numpy as np

cap = cv2.VideoCapture("video.mp4")

sub = cv2.createBackgroundSubtractorMOG2(history = 100,varThreshold=50, detectShadows=True)

while True:
    a, frame = cap.read()
    m = sub.apply(frame)
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break
    cv2.imshow("frame", frame)
    cv2.imshow("max", m)
    
    
cap.release()
cv2.destroyAllWindows()
        
