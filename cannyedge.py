import cv2
"""
5 steps of canny edge detection
Apply gaussian filter to remove noise
calculate gradient intensity
get rid of spurious responses (non-maximum supression)
Double Threshold to determine potential edges
edge tracking by hysteresis
"""
def acti(x):
    pass
cap = cv2.VideoCapture(0)
cv2.namedWindow('canny')
cv2.createTrackbar('Thres1','canny',0,255,acti)
cv2.createTrackbar('Thres2','canny',0,255,acti)
while True:
    _,frame = cap.read()

    th1 = cv2.getTrackbarPos('Thres1','canny')
    th2 = cv2.getTrackbarPos('Thres2','canny')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    canny = cv2.Canny(gray,th1,th2)

    cv2.imshow('canny',canny)

    k = cv2.waitKey(1) & 0XFF

    if k == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()