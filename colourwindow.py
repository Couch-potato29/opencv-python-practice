import cv2
import numpy as np

event = [i for i in dir(cv2) if "EVENTS" in i]

def click_event(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x,y,0]
        green = img[x,y,1]
        red = img[x,y,2]
        
        colimg = np.zeros((512,512,3), np.uint8)

        colimg[:] = [blue,green,red]
        cv2.imshow('colour window',colimg)

img = cv2.imread('C:/Users/abhay/Desktop/cv/spiderman.jpg')
img = cv2.resize(img,(512,512))
cv2.imshow('image',img)

cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()