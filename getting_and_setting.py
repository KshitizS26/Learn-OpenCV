# importing from __future__ so that print() works in both Python 2.7 and 3
from __future__ import print_function
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the input image")
ap.add_argument("-o", "--output", required = True, help = "Path to the output image")
args = vars(ap.parse_args())

# cv2 returns a NumPy array
image = cv2.imread(args["image"])

cv2.imshow("Original", image)

# accessing the pixel at y = 0 and x = 0
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# changing the pixel at y = 0 and x = 0
image[0, 0] = (0, 0, 255)

(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

corner = image[0:100, 0:100]
cv2.imshow("Corner", corner)

image[0:100, 0:100] = (0, 255, 0)

cv2.imshow("Updated", image)
cv2.waitKey(0)

cv2.imwrite(args["output"], image)
