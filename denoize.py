import numpy as np
import cv2

img = cv2.imread('green.jpg')
dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)

b,g,r = cv2.split(dst)      
rgb_dst = cv2.merge([r,g,b])

cv2.imwrite('denoisegreen.jpg',rgb_dst)
