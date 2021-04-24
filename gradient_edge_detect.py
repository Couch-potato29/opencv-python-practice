import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #laplacican
    #sobelX
    #sobelY
    #combined Sobel
    sobelX = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
    sobelY = cv2.Sobel(gray, cv2.CV_64F, 0, 1)

    sobelX = np.uint8(np.absolute(sobelX))
    sobelY = np.uint8(np.absolute(sobelY))

    sobelcomb = cv2.bitwise_or(sobelX,sobelY)
    cv2.imshow('video',sobelcomb)

    k = cv2.waitKey(1) & 0XFF

    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()