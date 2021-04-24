import cv2
import numpy as np

def act(x):
    pass

vid = cv2.VideoCapture(0)
cv2.namedWindow('tracking')
cv2.createTrackbar("LH",'tracking', 0, 255, act)
cv2.createTrackbar("LS",'tracking', 0, 255, act)
cv2.createTrackbar("LV",'tracking', 0, 255, act)
cv2.createTrackbar('UH','tracking', 255, 255, act)
cv2.createTrackbar('US','tracking', 255, 255, act)
cv2.createTrackbar('UV','tracking', 255, 255, act)


while True:
    
    #img = cv2.imread('spiderman2.jpg')
    _, img = vid.read()

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos('LH','tracking')
    ls = cv2.getTrackbarPos('LS','tracking')
    lv = cv2.getTrackbarPos('LV','tracking')

    uh = cv2.getTrackbarPos('UH','tracking')
    us = cv2.getTrackbarPos('US','tracking')
    uv = cv2.getTrackbarPos('UV','tracking')

    l_b = np.array([lh, ls, lv])
    u_b = np.array([uh, us, uv])

    mask = cv2.inRange(hsv, l_b, u_b)

    res = cv2.bitwise_and(img,img, mask= mask)


    #cv2.imshow('image',img)
    cv2.imshow('hsv', hsv)
    cv2.imshow('result', res)

    k = cv2.waitKey(1) & 0XFF
    if k == 27:
        break

vid.release()
cv2.destroyAllWindows()