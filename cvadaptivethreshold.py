import cv2

def act(x):
    pass
cap = cv2.VideoCapture(0)

cv2.namedWindow('threshold')
cv2.createTrackbar('Cslider','threshold', 0, 255,act)

while True:

    _,frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    p = cv2.getTrackbarPos('Cslider','threshold')
    th1 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, p)
    
    cv2.imshow('threshold',th1)

    k = cv2.waitKey(1) & 0XFF
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()