import face_recognition
photo_indra1=face_recognition.load_image_file('./img/indiragandhi.jpeg')
photo_indra2=face_recognition.load_image_file('./img/indiragandhi1.webp')
photo_priy1=face_recognition.load_image_file('./img/priyankagandhi.jpg')
photo_priy2=face_recognition.load_image_file('./img/priyankagandhi1.jpg')
photo_sonia=face_recognition.load_image_file('./img/soniagandhi.jpg')
encodings_indra1=face_recognition.face_encodings(photo_indra1)[0]
encodings_indra2=face_recognition.face_encodings(photo_indra2)[0]
encodings_priy1=face_recognition.face_encodings(photo_priy1)[0]
encodings_priy2=face_recognition.face_encodings(photo_priy2)[0]
encodings_sonia=face_recognition.face_encodings(photo_sonia)[0]
print("Distance: Priyanka01 to Indra01, Indra02, Sonia, Priyanka02")
faces=[encodings_indra1,encodings_indra2,encodings_sonia,encodings_priy2]
print(face_recognition.face_distance(faces,encodings_priy1))