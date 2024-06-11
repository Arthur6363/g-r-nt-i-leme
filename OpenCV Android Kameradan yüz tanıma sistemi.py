# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 14:01:28 2024

@author: necip
"""


import cv2
import numpy as np
import requests

# URL'den görüntü çekeceğimiz adres
url = "http://192.168.0.112:8080/shot.jpg"

# Haar Cascade sınıflandırıcısını yüklüyoruz
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    # URL'den görüntü verisini alıyoruz
    img_resp = requests.get(url)
    arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    img = cv2.resize(img, (800, 600))
    
    # Görüntüyü gri tonlamaya çeviriyoruz
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Yüzleri tespit ediyoruz
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Tespit edilen yüzlerin etrafına dikdörtgen çiziyoruz
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # Görüntüyü bir pencere içinde gösteriyoruz
    cv2.imshow("Face Detection", img)
    
    # 'q' tuşuna basıldığında döngüden çıkıyoruz
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
# Pencereleri kapatıyoruz
cv2.destroyAllWindows()