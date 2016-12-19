import cv2
import numpy as np

img1 = cv2.imread('green.jpg')
img2 = cv2.imread('sobel.jpg')
dst = cv2.addWeighted(img1,1,img2,0.5,0)

cv2.imwrite('adding.jpg',dst)
