import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

# canny edge detector, a remedy for noisy edges
# steps - blurring of image to remove noise, computing sobel gradient images
# in the x and y direction, suppressing edges, and hysteris thresholding stage
# that determines if a pixel is "edge-like" or not

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Blurred", image)
# 30 - any pixel value below 30 are considered non-edges
# 150 - any pixel value larger than 150 are consider edges
# values lies in between 30 and 150 are considered non-edges and edges
# based on how their intensities are connected
canny = cv2.Canny(image, 30, 150)
cv2.imshow("Canny", canny)
cv2.waitKey(0)


