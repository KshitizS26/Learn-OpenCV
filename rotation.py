import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

'''
rotating the image around its center
OpenCV allows to specify arbitrary point upon which to rotate
'''
(h, w) = image.shape[:2]
# integer division is used to ensure we receive whole integer numbers
center = (w // 2, h //2)

'''
defining a matrix to rotate an image by calling getRotationMatrix2D() instead of creating a NumPy array manually
center: the point at which we want to rotate
theta: the number of degrees to rotate the image
scale: 1.0 means the same dimensions of the image are used; a value of 2.0 will double the size of the image; a value of 0.5 will half the image
'''
M = cv2.getRotationMatrix2D(center, 45, 1.0)
'''
applying rotation
image: the image to be rotated
M: rotation matrix
(w, h): output dimension of the image
'''
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 45 Degrees", rotated)
cv2.waitKey(0)

M = cv2.getRotationMatrix2D(center, -90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by -90 Degrees", rotated)
cv2.waitKey(0)

rotated = imutils.rotate(image, 180)
cv2.imshow("Rotated by 180 Degrees", rotated)
cv2.waitKey(0)

