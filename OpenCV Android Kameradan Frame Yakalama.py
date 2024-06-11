# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 13:42:08 2024

@author: necip
"""
import cv2
import numpy as np
import requests

url = "http://192.168.0.112:8080/shot.jpg"

while True:
    img_resp = requests.get(url)
    arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    img = cv2.resize(img, (800, 600))
    
    cv2.imshow("1", img)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
cv2.destroyAllWindows()