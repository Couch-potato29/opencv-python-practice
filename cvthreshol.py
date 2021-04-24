import cv2

cap =  cv2.VideoCapture(0)
cv2.namedWindow('thresimage')

while True:
    _,frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #possible flags:
    # cv2.THRESH_BINARY
    # cv2.THRESH_BINARY_INV
    # cv2.THRESH_TOZERO
    # cv2.THRESH_TRUNC
    _,th1 = cv2.threshold(gray,200,255,cv2.THRESH_BINARY)

    cv2.imshow('thresimage',th1)

    k = cv2.waitKey(1) & 0XFF

    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()