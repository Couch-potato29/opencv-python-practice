import cv2

img = cv2.imread('spiderman2.jpg')
img2 = cv2.imread('red_wind.jpg')

print(img.shape)
print(img.size)
print(img.dtype)
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

img = cv2.resize(img,(512,521))
img2 = cv2.resize(img2,(512,521))

# head = img[280:340, 330:390]
# #cv2.imshow('image',head)
# img[8:16, 40:100] = head
newimg = cv2.addWeighted(img, 0.9, img2, .4, 0)



cv2.imshow('image',newimg)
cv2.waitKey(0)
cv2.destroyAllWindows()