from __future__ import print_function
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

# addition using cv2.add between two 8-bit unsigned integers
# addition would be clipped at a maximum of 255
print("max of 255: {}".format(cv2.add(np.uint8([200]), np.uint8([100]))))
# subtraction using cv2.subtract between two 8-bit unsigned integers
# subtraction would be clipped at a minimum of 0
print("min of 0: {}".format(cv2.subtract(np.uint8([50]), np.uint8([100]))))

# NumPy doesn't perform clipping; it performs modulo arithmetic and wraps around
# once a value of 255 is reached, NumPy wraps around to zero, and then starts counting up again, until 100 steps have been reached
print("wrap around: {}".format(np.uint8([200]) + np.uint8([100])))
# once 0 is reached during the subtraction, the modolus operations wraps around and starts counting backward from 255
print("wrap around: {}".format(np.uint8([50]) - np.uint8([100])))

'''
Note:
1. Use OpenCV's built-in methods for image arithmetic if you want values to 
be clipped if they fall outside the range [0,255]
2. Use NumPy arrays for addition and subtraction if you want modulus arithmetic 
operations and have values wrap around if they fall outside the range of [0, 255]

'''

M = np.ones(image.shape, dtype = "uint8") * 100
added = cv2.add(image, M)
cv2.imshow("Added", added)
cv2.waitKey(0)

M = np.ones(image.shape, dtype = "uint8") * 50
subtracted = cv2.subtract(image, M)
cv2.imshow("Subtracted", subtracted)
cv2.waitKey(0)