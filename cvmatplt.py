import cv2
from matplotlib import pyplot as plt

img = cv2.imread('spiderman2.jpg',0)
cv2.imshow('image',img)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

_,th1 = cv2.threshold(img,127,255, cv2.THRESH_BINARY)
_,th2 = cv2.threshold(img,200,255, cv2.THRESH_BINARY_INV)
_,th3 = cv2.threshold(img,127,255, cv2.THRESH_TRUNC)
_,th4 = cv2.threshold(img,127,255, cv2.THRESH_TOZERO)
_,th5 = cv2.threshold(img,127,255, cv2.THRESH_TOZERO_INV)

titles = ['image','BINARY','BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, th1,th2,th3,th4,th5]
for i in range(6):
    plt.subplot(2, 3, i+1),plt.imshow(images[i], 'gray')
    plt.title(titles[i])
# plt.imshow(img)
# plt.show()
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()