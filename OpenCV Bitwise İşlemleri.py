# -*- coding: utf-8 -*-
"""
Created on Tue May  7 11:59:43 2024

@author: necip
"""

import cv2
import numpy as np

img1 = cv2.imread("arthur.jpg")
img2 = cv2.imread("siyahbeyaz.png")

bit_and = cv2.bitwise_and(img1,img2)


cv2.imshow("1", img1)
cv2.imshow("2", img2)
cv2.imshow("bit", bit_and)



cv2.waitKey(0)
cv2.destroyAllWindows()
