import cv2
import numpy as np
from matplotlib import pyplot as plt

def act(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow('image')

cv2.createTrackbar("LH",'image', 0, 255, act)
cv2.createTrackbar("LS",'image', 0, 255, act)
cv2.createTrackbar("LV",'image', 0, 255, act)
cv2.createTrackbar('UH','image', 255, 255, act)
cv2.createTrackbar('US','image', 255, 255, act)
cv2.createTrackbar('UV','image', 255, 255, act)

while True:
    _,frame = cap.read()

    #frame = cv2.threshold(frame, cv2.THRESH_BINARY)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos('LH','image')
    ls = cv2.getTrackbarPos('LS','image')
    lv = cv2.getTrackbarPos('LV','image')

    uh = cv2.getTrackbarPos('UH','image')
    us = cv2.getTrackbarPos('US','image')
    uv = cv2.getTrackbarPos('UV','image')

    l_b = np.array([lh, ls, lv])
    u_b = np.array([uh, us, uv])

    mask = cv2.inRange(hsv, l_b, u_b)

    res = cv2.bitwise_and(frame,frame, mask= mask)

    kernel = np.ones((5,5),np.uint8)
    dialate = cv2.dilate(mask,kernel,iterations=1)
    erode = cv2.erode(mask, kernel, iterations=1)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    
    #cv2.imshow('hsv', hsv)
    cv2.imshow('result', res)
    #cv2.imshow('erode', erode)
    cv2.imshow('dilate', dialate)
    cv2.imshow('opening', opening)


    k = cv2.waitKey(1) & 0XFF
    if k == 27:
        break


cap.release()
cv2.destroyAllWindows()