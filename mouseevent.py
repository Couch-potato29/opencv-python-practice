import cv2

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,"  ",y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        content = str(x)+", "+str(y)
        cv2.circle(img, (x,y),1, (0,255,0), 2)
        cv2.imshow('image',img)

img = cv2.imread('C:/Users/abhay/Desktop/cv/spiderman2.jpg',1)
cv2.imshow('image',img)
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()