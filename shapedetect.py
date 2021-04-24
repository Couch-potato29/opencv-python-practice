import cv2

def ac(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow('track')
cv2.createTrackbar('threshold','track',0,255,ac)
#cv2.createTrackbar('epsilon','track',0.00,0.50,ac)
while True:
    _,frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    th = cv2.getTrackbarPos('threshold','track')
    _,thresh = cv2.threshold(gray, th, 255, cv2.THRESH_BINARY_INV)

    contours,_ = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #ep = cv2.getTrackbarPos('epsilon','track')
    for contour in contours:
        #epsilon( the second arguement of the function ) defines the parameters approximation accuracy
        #approximates ploygonal curves with a specific precision
        # the arclength function gives the arc lengthof that contour in the image
        approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour, True),True)

        cv2.drawContours(frame, [approx], 0, (0,255,0), 3)

        x = approx.ravel()[0]
        y = approx.ravel()[1]

        if len(approx) == 3:
            cv2.putText(frame, "Triangle",(x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0))
        elif len(approx) == 4:
            x,y,w,h = cv2.boundingRect(approx)
            aspectRatio = float(w)/h
            if aspectRatio >= 0.95 and aspectRatio<=1.05:
                cv2.putText(frame, "Square",(x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0))
            else:
                cv2.putText(frame, "Rectangle",(x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0))
        elif len(approx) == 5:
            cv2.putText(frame, "pentagon",(x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0))
        elif len(approx) == 10:
            cv2.putText(frame, "Star",(x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0))
        else:
            cv2.putText(frame, "Circle",(x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0))

    cv2.imshow('shapes',frame)

    k = cv2.waitKey(1) & 0XFF
    if k == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
