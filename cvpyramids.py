import cv2

img = cv2.imread('spiderman.jpg',0)

lr = img

for i in range(4):
    lr = cv2.pyrDown(lr)

cv2.imshow('original',img)
lr = cv2.pyrUp(lr)
cv2.imshow('PyrDown',lr)
cv2.waitKey(0)
cv2.destroyAllWindows()