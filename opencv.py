# -*- coding: utf-8 -*-
"""
Created on Thu May  2 12:46:00 2024

@author: necip
"""
import cv2

img = cv2.imread("airplane.jpg") #dosyayı okuttuk

#img = cv2.resize(img,(400,300))

cv2.namedWindow("image", cv2.WINDOW_NORMAL) #açılacak olan pencerede resmin boyutunu ayarlamak için

cv2.imshow("image", img) #resmi açma imshow

cv2.imwrite("copy.jpg", img) #resmi kaydetme 

cv2.waitKey(0) # waitkey 0 demek resim açık kalacak bir tuşa basılana kadar

cv2.destroyAllWindows() # ne varsa kapat
