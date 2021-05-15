import cv2

img = cv2.imread('rebecca.jpg',0)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.imwrite('rebecca_copy.png',img)
cv2.destroyAllWindows()