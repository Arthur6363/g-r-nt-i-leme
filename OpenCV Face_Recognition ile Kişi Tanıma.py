# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 15:29:20 2024

@author: necip
"""

import cv2
import dlib
import face_recognition

detector = dlib.get_frontal_face_detector()

necip = face_recognition.load_image_file("necip.jpg")
necip_enc = face_recognition.face_encodings(necip)[0]


cap = cv2.VideoCapture(1)
while True:
    ret, frame = cap.read()
    
    faces = detector(frame)
    for face in faces:
        x=face.left()
        y=face.top()
        w=face.right()
        h=face.bottom()
        face_loc.append((y,w,h,x))
    
    
    face_loc = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame,face_loc)
    
    
    
    for face in face_encodings:
        sonuc = face_recognition.compare_faces([necip_enc],face)
        print(sonuc)
    
    
    
    
    
    cv2.imshow("1", frame)
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break
    
    
cap.release()
cv2.destroyAllWindows()