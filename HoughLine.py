import cv2
import numpy as np

# Program to perfom houghline transform using HOUGH LINES
def ac(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow('tracking')
cv2.createTrackbar('thres1','tracking',0,255,ac)
cv2.createTrackbar('thres2','tracking',0,255,ac)
cv2.createTrackbar('acc','tracking',0,255,ac)

while True:
    _,frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    th1 = cv2.getTrackbarPos('thres1','tracking')
    th2 = cv2.getTrackbarPos('thres2','tracking')
    acc = cv2.getTrackbarPos('acc','tracking')

    edges = cv2.Canny(gray, th1, th2, apertureSize=3)
    lines = cv2.HoughLines(edges, 1, np.pi/180, acc)

    for line in lines:
        rho,theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho

        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))

        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        cv2.line(frame, (x1,y1), (x2,y2), (0,255,0), 2)
    cv2.imshow('newim',edges)

    k = cv2.waitKey(1) & 0XFF
    if k == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()