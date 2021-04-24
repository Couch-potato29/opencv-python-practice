import cv2
# bitwise operarions are done to perform an operation on a specificpart of the matrix, in ohter word, masks
import numpy as np

img = np.zeros((250,500,3),np.uint8)
img = cv2.rectangle(img,(200,0),(300,100),(255,255,255),-1)

img2 = np.zeros((250,500,3),np.uint8)
img2 = cv2.rectangle(img2,(250,0),(500,250),(255,255,255),-1)

bit_and = cv2.bitwise_and(img2, img)

cv2.imshow('image',img)
cv2.imshow('img2',img2)
cv2.imshow('AND',bit_and)

cv2.waitKey(0)
cv2.destroyAllWidows()
