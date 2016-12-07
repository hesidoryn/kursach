import cv2
import numpy as np
from matplotlib import pyplot as plt

# loading image
#img0 = cv2.imread('SanFrancisco.jpg',)
img0 = cv2.imread('test.jpg',1)

# converting to gray scale
gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)

# remove noise
img = cv2.GaussianBlur(gray,(3,3),0)

# convolute with proper kernels
laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)  # x
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)  # y

abs_grad_x = cv2.convertScaleAbs(sobelx) #converting back to uint8
abs_grad_y = cv2.convertScaleAbs(sobely)

dst = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, (0.5), 0)

plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(dst,cmap = 'gray')

plt.show()

cv2.imwrite('lapl.jpg',laplacian)
cv2.imwrite('sx.jpg',sobelx)
cv2.imwrite('sy.jpg',sobely)

edges = cv2.Canny(img,100,200)

cv2.imwrite('canny.jpg',edges)
