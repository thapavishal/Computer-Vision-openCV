import cv2

img = cv2.imread('rebecca.jpg',0)
# reads the image in grayscale
#print(img) # gives the image in matrix form

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
