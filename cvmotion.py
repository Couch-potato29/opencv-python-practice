import cv2
#steps to find contours:
#1) intitialise two frames
#2) find the absolute difference between the two frames which is done in the while loop
#3) convert the image to grayscale for better contouring
#4) blur the graysscale frame
#5) apply threshold (here we apply binary)
#6) dilate the frame (dilation is increasing the white values more to reduce noise)
#7) find contours on the thresholded frame and then draw those contours on the original frame that is frame1
#8) display the original frame
#9) assign frame2 to frame1 and read the new frame to frame2




cap = cv2.VideoCapture(0)
_,frame1 = cap.read()
_,frame2 = cap.read()

while True:
    diff = cv2.absdiff(frame1,frame2)

    #converting to gray scale to find contours of the frame later
    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)

    #_,frame = cap.read()
    #blurring the frame
    blur = cv2.blur(gray, (5,5), 0)
    _,thresh = cv2.threshold(blur, 20,255, cv2.THRESH_BINARY)
    dilate = cv2.dilate(thresh,None, iterations=3)

    #finding contours
    contours,_ = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #iterating over the contours so that we can draw the bounding rectangle on individual contours
    for contour in contours:
        (x,y,w,h) = cv2.boundingRect(contour)
        #we draw rectangles only for the area of the rectangles whose area is >= to a certain value

        if cv2.contourArea(contour) < 10000:
            continue
        cv2.rectangle(frame1, (x,y),(x+w,y+h), (0,255,0),2)
        cv2.putText(frame1, "status: {}".format('Movement'), (10,20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0),3)



    #cv2.drawContours(frame1, contours,-1,(0,255,0), 2)
    cv2.imshow('result',frame1)

    frame1 = frame2
    _,frame2 = cap.read()

    k = cv2.waitKey(1) & 0XFF

    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()