import cv2
import datetime as d
vid = cv2.VideoCapture(0)

vid.set(cv2.CAP_PROP_FRAME_HEIGHT,1080)
vid.set(cv2.CAP_PROP_FRAME_WIDTH,1920)

w = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
h = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
da = d.datetime.now()

while(True):
    ret,frame = vid.read()
    if ret == True:

        text = str(w)+" "+str(h)+" "+str(da)
        frame = cv2.putText(frame,text,(0,20),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),2)
        cv2.imshow("Video",frame)

    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()