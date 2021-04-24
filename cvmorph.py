import cv2
import numpy as np
from matplotlib import pyplot as plt


cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    _,mask = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)

    dialation = cv2.dilate(mask, kernel=(np.ones((2,2), np.uint8)),iterations=2)
    erode = cv2.erode(mask,kernel = (np.ones((2,2),np.uint8)),iterations=1)
    op = cv2.morphologyEx(mask,cv2.MORPH_OPEN, kernel = (np.ones((2,2), np.uint8)))

    cl = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel= (np.ones((2,2),np.uint8)))
    k = cv2.waitKey(1) &0XFF

    cv2.imshow('closing',cl)
    cv2.imshow('dialation',dialation)
    cv2.imshow('erode',erode)

    if k == ord('q'):
        break

# titles = ['image','mask','dilated','erode']
# images = [img,mask,dialation,erode]

# for i in range(4):
#     plt.subplot(1,4,i+1), plt.imshow(images[i], 'gray')
#     plt.title(titles[i])

# plt.show()
cap.release()
cv2.destroyAllWindows()