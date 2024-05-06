# -*- coding: utf-8 -*-
"""
Created on Mon May  6 14:08:32 2024

@author: necip
"""

import cv2
import numpy as np

img = cv2.imread("sufii.jpg")
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img3 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


cv2.imshow("sufi", img)
cv2.imshow("rgb", img1)
cv2.imshow("hsv", img2)
cv2.imshow("gray", img3)


cv2.waitKey(0)
cv2.destroyAllWindows()