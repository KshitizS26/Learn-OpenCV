import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

# cv2.flip accomplishes flipping by providing a flip code
# 1 - flip horizontally around the y axis
flipped = cv2.flip(image, 
	1)
cv2.imshow("Flipped Horizontally", flipped)
cv2.waitKey(0)

# 0 - flip vertically around the x axis
flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped)
cv2.waitKey(0)

# -1 - flip image on both the axes
flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Horizontally and Vertically", flipped)
cv2.waitKey(0)

