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
aspect ratio is to be maintained
aspect ratio is the proportional relationship of width and the height of the image
width of the new image = 150.0
r: aspect ratio of width - new width/old width
ascept ratio of height = ascept ratio of width
'''
r = 150.0 / image.shape[1]
# new height = old height * aspect ratio
# width x height
dim = (150, int(image.shape[0] * r))

'''
actual resize
image: image to resize
dim: computed dimension for new image
interpolation: algorithm behind the scenes to handle resizing
other resizing algorithms - cv2.INTER_LINEAR, cv2.INTER_CUBIC, cv2.INTER_NEAREST
'''

resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("Resized (Width)", resized)
cv2.waitKey(0)

r = 50.0 / image.shape[0]
# width x height
dim = (int(image.shape[1] * r), 50)

resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("Resized (Height)", resized)
cv2.waitKey(0)

resized = imutils.resize(image, width = 100)
cv2.imshow("Resized via Function", resized)
cv2.waitKey(0)

resized = imutils.resize(image, height = 50)
cv2.imshow("Resized via Function", resized)
cv2.waitKey(0)




