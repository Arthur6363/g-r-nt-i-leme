# -*- coding: utf-8 -*-
"""
Created on Fri May  3 14:05:28 2024

@author: necip
"""
import cv2
import numpy as np

img = cv2.imread("sufii.jpg")

roi = img[300:300, 350:200]

cv2.imshow("sufi", img)

cv2.imshow("roi", roi)

cv2.waitKey(0)
cv2.destroyAllWindows()