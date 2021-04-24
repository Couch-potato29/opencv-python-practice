import cv2 
#import imutils
cam = cv2.VideoCapture(0)
HEIGHT = 700
WIDTH = 480
# cam.set(3,HEIGHT)
# cam.set(4,WIDTH)
#cam.set(10,150)
def ac(x):
    pass

cv2.namedWindow('tracking')
cv2.createTrackbar('winstride','tracking',2,20,ac)
cv2.createTrackbar('padding','tracking',2,20,ac)
cv2.createTrackbar('scale','tracking',2,10,ac)

# Initializing the HOG person 
# detector 
hog = cv2.HOGDescriptor() 
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector()) 

# Reading the Image 
while True:
    _,image = cam.read() 
    # Resizing the Image 
    #image = imutils.resize(image, width=min(400, image.shape[1])) 

    win = cv2.getTrackbarPos('winstride','tracking')
    pad = cv2.getTrackbarPos('padding','tracking')
    scale = cv2.getTrackbarPos('scale','tracking')

    # Detecting all the regions in the 
    # Image that has a pedestrians inside it 
    (regions, _) = hog.detectMultiScale(image, winStride=(win, win), padding=(pad, pad), scale=scale) 

    # Drawing the regions in the Image 
    for (x, y, w, h) in regions: 
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2) 

    # Showing the output Image 
    cv2.imshow("Image", image) 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()