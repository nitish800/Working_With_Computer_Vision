import cv2

gimg = cv2.imread('test.jpg',cv2.IMREAD_GRAYSCALE) #Read image as grayscale image
cv2.imwrite('newgray.jpg', gimg)       #write image as grayscale
