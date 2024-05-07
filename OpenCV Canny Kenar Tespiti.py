# -*- coding: utf-8 -*-
"""
Created on Tue May  7 13:50:54 2024

@author: necip
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    kenar = cv2.Canny(frame, 50,150)
    cv2.imshow("o", frame)
    cv2.imshow("c", kenar)
    
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break
    
    
cap.release()
cv2.destroyAllWindows()