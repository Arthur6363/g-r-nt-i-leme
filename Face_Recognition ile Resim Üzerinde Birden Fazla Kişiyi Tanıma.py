# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 14:40:41 2024

@author: necip
"""

import cv2
import face_recognition

# Yüzleri tanımak için resimleri yükle
kisi1 = face_recognition.load_image_file("tarkan.jpg")
kisi1_encodings = face_recognition.face_encodings(kisi1)[0]

kisi2 = face_recognition.load_image_file("haluk.jpg")
kisi2_encodings = face_recognition.face_encodings(kisi2)[0]

# Kodlamaları ve isimleri listelere ekle
encoding_list = [kisi1_encodings, kisi2_encodings]
name_list = ["Tarkan", "Haluk Bilginer"]

# Test resmini yükle ve yüzleri tanı
test_image = cv2.imread("tarkan2.jpg")
test_image_encodings = face_recognition.face_encodings(test_image)[0]
face_locations = face_recognition.face_locations(test_image)

# Yüzleri karşılaştır ve sonuçları göster
for face_location, face_encoding in zip(face_locations, test_image_encodings):
    ustsoly, altsagx, altsagy, ustsolx = face_location
    match_faces = face_recognition.compare_faces(encoding_list, face_encoding)
    name = "Bilinmeyen Kişi"

    if True in match_faces:
        matched_index = match_faces.index(True)
        name = name_list[matched_index]

    # Eşleşen yüzün etrafına bir dikdörtgen çiz
    cv2.rectangle(test_image, (ustsolx, ustsoly), (altsagx, altsagy), (255, 0, 0), 2)
    # Yüzün üzerine isim yaz
    cv2.putText(test_image, name, (ustsolx, ustsoly), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)

# Sonucu göster
cv2.imshow("Sonuç", test_image)
print(name)
cv2.waitKey(0)
cv2.destroyAllWindows()
