import numpy as np
import argparse
# imutils: local file to create convenience methods to do common tasks like translation, rotation, and resizing
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

'''
defining translation matrix
it tells how many pixels to the left or right, and up or down, the image will be shifted
it should be a floating point array because OpenCV demands so

first row of the matrix: [1, 0, t_x] where t_x is the number of pixels it should be shifted towards left or right
negative t_x: shift to left; positive t_x: shift to right

second of the matrix: [0, 1, t_y] where t_y is the number of pixels it should be shifted towards up or down
negative t_y: shift to up, positive t_y: shift to down

shifting our image 25 pixels towards right and 50 pixels down
'''
M = np.float32([[1, 0, 25], [0, 1, 50]])

'''
actual translation function
image: the image we want to shift
M: translation matrix
3rd argument: manually supplying the dimensions (width x height)
'''
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Down and Right", shifted)
cv2.waitKey(0)

# another translation 50 pixel towards left and 90 pixels upward
M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Left", shifted)
cv2.waitKey(0)

shifted = imutils.translate(image, 0, 100)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)
