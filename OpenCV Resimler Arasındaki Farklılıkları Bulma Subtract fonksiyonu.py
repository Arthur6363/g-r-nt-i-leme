# -*- coding: utf-8 -*-
"""
Created on Mon May 13 13:39:19 2024

@author: necip
"""

import cv2
import numpy as np

img1 = cv2.imread("ub1.jpg")
img2 = cv2.imread("ub2.jpg")

fark= cv2.subtract(img1, img2)
b,g,r = cv2.split(fark)


cv2.imshow("farl", fark)


"""
cv2.imshow("sa", img1)
cv2.imshow("as", img2)
"""

cv2.waitKey(0)
cv2.destroyAllWindows()