# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 15:30:19 2024

@author: necip
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 15:02:16 2024

@author: necip
"""

import cv2
import numpy as np
from collections import deque

dq = deque(maxlen=3)

#%%
buffer_size = 16
pts = deque(maxlen=buffer_size)

bluelower = (84,98,0)
blueupper = (179,200,200)

cap = cv2.VideoCapture(1)
cap.set(3, 960)
cap.set(3,480)

while True:
    succes, imgorginal = cap.read()
    
    if succes:
        blured = cv2.GaussianBlur(imgorginal, (11,11), 0)
        hsv = cv2.cvtColor(blured, cv2.COLOR_BGR2HSV)
        cv2.imshow("hsv penceresi", hsv)
        
        
        mask = cv2.inRange(hsv, bluelower, blueupper)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        cv2.imshow("maskeli pencere", mask)
        
        
        (contours,_)= cv2.findContours(mask.copy, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        center = None
        
        if len(contours)>=0:
            c = max(contours,key = cv2.contourArea)
            rect = cv2.minAreaRect(c)
            ((x,y), (widht,height), rotation)=rect
            s = "x:{}, y:{}, widht:{}, height:{}, rotation:{}".format(np.round(x), np.round(y), np.round(widht), np.round(height), np.round(rotation))
            print(s)
            
            box = cv2.boxPoints(rect)
            box = np.int64(box)
            
            
            M = cv2.moments(c)
            center = int(M["m10"]/M["m00"]), int(M["m01"], M["m00"])
            cv2.drawContours(imgorginal, [box], 0,(0,255,255),2)
            cv2.circle(imgorginal, center, 5, (255,0,0))
            
            pts.append(center)
            for i in range(1,len(pts)):
                if pts[i-1] is None or pts[i] is None: continue
                cv2.line(imgorginal, pts[i-1], pts[i], (0,255,255),3)
            cv2.imshow("orgina", imgorginal)
        
        
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
  
  