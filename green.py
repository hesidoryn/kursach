import numpy as np
import cv2

image = cv2.imread('map.jpg')
kernel1 = np.ones((25,25),np.uint8)
kernel2 = np.ones((1,3),np.uint8)

boundaries = [
	#([0, 30, 200], [50, 90, 255]),
	([65, 250, 155], [115, 255, 225]),
	#([86, 31, 4], [220, 88, 50]),
	#([25, 146, 190], [62, 174, 250]),
	#([103, 86, 65], [145, 133, 128])
]

for (lower, upper) in boundaries:
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")

	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask< = mask)
	closing1 = cv2.morphologyEx(output, cv2.MORPH_CLOSE, kernel1)
	closing2 = cv2.morphologyEx(output, cv2.MORPH_CLOSE, kernel2)

	cv2.imwrite('green1.jpg', closing1)
	cv2.imwrite('green2.jpg', closing2)
	cv2.imwrite('green3.jpg', output)
