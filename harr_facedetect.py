import cv2
import numpy as np

"""
Face detection using harr feature based object classifiers
This is a machine learning approach where a casscade function
is made to run over many images to get positive and negative feedback

"""
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)


while True:
    _,frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.1, 4)


    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)

    cv2.imshow('face detection',frame)

    k = cv2.waitKey(1) & 0XFF

    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
