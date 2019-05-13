import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# supplying NumPy array slices to extract a rectangular region of the image, starting at (240, 30) and ending at (335, 120)
cropped = image[30:120, 240:335]
cv2.imshow("Cropped", cropped)
cv2.waitKey(0)  