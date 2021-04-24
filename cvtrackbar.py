import cv2
import numpy as np

def action(x):
    pass

img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar('B','image', 0, 255, action)
cv2.createTrackbar('G','image', 0, 255, action)
cv2.createTrackbar('R','image', 0, 255, action)

while True:
    cv2.imshow('image',img)

    k = cv2.waitKey(1) & 0XFF
    if k == 27:
        break
    b = cv2.getTrackbarPos('B','image')
    g = cv2.getTrackbarPos('G','image')
    r = cv2.getTrackbarPos('R','image')
    
    img[:] = [b,g,r]

cv2.destroyAllWindows()