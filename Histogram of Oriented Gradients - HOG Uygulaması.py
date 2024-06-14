# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 14:20:28 2024

@author: necip
"""

import cv2
from skimage.feature import hog
from skimage import exposure

image = cv2.imread("arthur.jpg")
gri = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_,hogimage = hog(gri, visualize=True)
rescaled = exposure.rescale_intensity(hogimage, in_range=(0,10))




cv2.imshow("hog", hogimage)
cv2.imshow("orginal", image)
cv2.imshow("rescale", rescaled)


cv2.waitKey(0)
cv2.destroyAllWindows()

