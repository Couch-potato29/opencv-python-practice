import cv2


def ac(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow('tracking')
cv2.createTrackbar('Threshold','tracking', 0, 255, ac)

while True:
    _,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # canny = cv2.Canny(gray,100,200)

    # cv2.imshow('canny',canny)
    th1 = cv2.getTrackbarPos('Threshold','tracking')
    _,thresh = cv2.threshold(gray,th1,255,0)

    contours,heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    cv2.drawContours(frame, contours, -1, (0,255,0), 3)
    cv2.imshow('contoured image',frame)

    k = cv2.waitKey(1) & 0XFF
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()