import numpy as np
import scipy
from scipy import ndimage
import cv2

im = scipy.misc.imread('green.jpg')
im = im.astype('int32')
#dx = ndimage.sobel(im, 0)  
#dy = ndimage.sobel(im, 1)  
#mag = numpy.hypot(dx, dy)  
#scipy.misc.imsave('presobel.jpg', mag)
#mag *= 255.0 / numpy.max(mag)  
#scipy.misc.imsave('sobelgreen.jpg', mag)

#drawing = np.zeros(im.shape,np.uint8)
#contours, hierarchy = cv2.findContours(im,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#for cnt in contours:
#	color = np.random.randint(0,255,(3)).tolist()  # Select a random color
#	cv2.drawContours(drawing,[cnt],0,color,2)
#	cv2.imshow('output',drawing)

#

img = cv2.imread('green2.jpg',cv2.CV_LOAD_IMAGE_GRAYSCALE)

th,dst = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
contours,hierarchy = cv2.findContours(dst, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(dst,contours,-1,(255,255,255),0)
cv2.imwrite('input.jpg',dst)

print len(contours)
