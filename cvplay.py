import cv2

img = cv2.imread('C:/Users/abhay/Desktop/cv/red_wind.jpg',1)

h,w,c = img.shape

img = cv2.circle(img,(int(w/2),int(h/2)),50,(0,255,0),1)
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,"This is OpenCV",(50,50),font,0.5,(0,255,0),2)
cv2.imshow('image',img)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()