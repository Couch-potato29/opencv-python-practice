import cv2
from matplotlib import pyplot as plt
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()

    kernel = np.ones((5,5), np.float32)/25

    dst = cv2.filter2D(frame, -1 ,kernel)
    blur = cv2.blur(frame, (5,5))
    glbur = cv2.GaussianBlur(frame, (5,5), 0)
    median = cv2.medianBlur(frame, 5)


    cv2.imshow('image',frame)
    cv2.imshow('2D',dst)
    cv2.imshow('blur', blur)
    cv2.imshow('gaussian',glbur)
    cv2.imshow('median',median)

    k = cv2.waitKey(1) & 0XFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
