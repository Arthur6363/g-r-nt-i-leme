# -*- coding: utf-8 -*-
"""
Created on Mon May  6 14:15:57 2024

@author: necip
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def fonks(x):
    pass

cv2.namedWindow("bar")
cv2.resizeWindow("bar", 600,600)


cv2.createTrackbar("alt-h", "bar", 0,180,fonks)         
cv2.createTrackbar("alt-s", "bar", 0,255,fonks)    
cv2.createTrackbar("alt-v", "bar", 0,255,fonks)    


cv2.createTrackbar("ust-h", "bar", 0,180,fonks)    
cv2.createTrackbar("ust-s", "bar", 0,255,fonks)    
cv2.createTrackbar("ust-v", "bar", 0,255,fonks)    

cv2.setTrackbarPos("ust-h,", "bar", 150)
cv2.setTrackbarPos("ust-s,", "bar", 150)
cv2.setTrackbarPos("ust-v,", "bar", 150)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    

    alt_h = cv2.getTrackbarPos("alt_h", "bar")
    alt_s = cv2.getTrackbarPos("alt_s", "bar")
    alt_v = cv2.getTrackbarPos("alt_v", "bar")
    
    ust_h = cv2.getTrackbarPos("ust_h", "bar")
    ust_s = cv2.getTrackbarPos("ust_s", "bar")
    ust_v = cv2.getTrackbarPos("ust_v", "bar")
    
    
    alt_renk = np.array([alt_h, alt_s, alt_v])
    ust_renk = np.array([ust_h, ust_s, ust_v])
    
    mask = cv2.inRange(frame_hsv, alt_renk, ust_renk)
    
    cv2.imshow("a", frame)

    cv2.imshow("m", mask) 
    
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break
    
    
cap.release()
cv2.destroyAllWindows("bar")    
    
    
    
    