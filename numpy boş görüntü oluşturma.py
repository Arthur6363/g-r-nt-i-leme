# -*- coding: utf-8 -*-
"""
Created on Thu May  2 21:24:35 2024

@author: necip
"""

import numpy as np
import cv2

canvas = np.zeros((512,512,3), dtype = np.uint8) + 200
print(canvas)

cv2.imshow("pencere", canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()