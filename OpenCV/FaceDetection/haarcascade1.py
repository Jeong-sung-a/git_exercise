import cv2
import matplotlib.pyplot as plt

image_cv2 = cv2.imread("../FaceDetection/Resource/side_girl.jpg")

face_classifier_frontal = cv2.CascadeClassifier("../FaceDetection/Resource/haarcascade_frontalface_default.xml")
face_classifier_profile = cv2.CascadeClassifier("../FaceDetection/Resource/haarcascade_profileface.xml")
faces_frontal = face_classifier_frontal.detectMultiScale(image_cv2)
faces_profile = face_classifier_profile.detectMultiScale(image_cv2)

# draw bounding box for each face detected
for (x, y, w, h) in faces_frontal:
    color = (255, 0, 0) # red
    stroke = 5
    cv2.rectangle(image_cv2, (x, y), (x + w, y + h), color, stroke)

for (x, y, w, h) in faces_profile:
    color = (0, 255, 255) # in light blue
    stroke = 5
    cv2.rectangle(image_cv2, (x, y), (x + w, y + h), color, stroke)

plt.figure(figsize=(20, 10))
plt.imshow(image_cv2)
plt.show() 
plt.axis('off')