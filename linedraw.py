import cv2

events = [i for i in dir(cv2) if "EVENT" in i]

def click_event(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 2, (0,255,0), -1)
        points.append((x,y))
        if len(points) >= 2:
            cv2.line(img, points[-2],points[-1], (0,255,0),1)
        cv2.imshow('image',img)

img = cv2.imread('C:/Users/abhay/Desktop/cv/red_wind.jpg',1)

cv2.imshow('image',img)
points = []
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()