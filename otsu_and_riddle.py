from __future__ import print_function
import numpy as np
import argparse
# mahotas is yet another image processing library
import mahotas
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5,5), 0)
cv2.imshow("Image", image)

# finding out the value of T using otsu's thresholding algorithm
T = mahotas.thresholding.otsu(blurred)
print("Otsu's threshold: {}".format(T))

thresh = image.copy()
# convert any pixel greater than T white
thresh[thresh > T] = 255
# convert everything black
thresh[thresh < 255] = 0
# invert the thresholding; equivalent to applying cv2.THRESH_BINARY_INV
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Otsu", thresh)

# finding out the value of T using riddler-calvard algorithm
T = mahotas.thresholding.rc(blurred)
print("Riddler-Calvard: {}".format(T))

thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < 255] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Riddler-Calvard", thresh)
cv2.waitKey(0)


