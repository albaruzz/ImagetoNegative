import sys
import cv2

img1 = cv2.imread(sys.path[0]+'\\lena-gray.bmp')

img2 = 255 - img1

cv2.imshow('input image', img1)
cv2.imshow('negative image', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()