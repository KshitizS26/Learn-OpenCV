import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

# applying Laplacian method to compute the gradient magnitude
# image by calling cv2.Laplacian function
# image - image we want to compute the gradient magnitude representation for
# cv2.CV_64F - data type for the output image (64-bit float)
lap = cv2.Laplacian(image, cv2.CV_64F)
# taking an absolute of the gradient and converting it back to 8-bit unsigned interger
lap = np.uint8(np.absolute(lap))
cv2.imshow("Laplacian", lap)
cv2.waitKey(0)

# using sobel operator to compute gradient magnitude representations
# along the x and y axis allowing us to find both horizontal and vertical
# edge-like regions
# image - image that we want to compute the gradient representation for
# cv.CV_64F - data type of the output image
# 1, 0; 0, 1 - order of the derivatives in the x and y direction, respectively
# 1, 0 - specify vertical edge-like regions; 0, 1 - specify horizontal edge-like regions
sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
spbelY = np.uint8(np.absolute(sobelY))

# combing the gradient images in both the x and y direction by
# applying a bitwise OR
sobelCombined = cv2.bitwise_or(sobelX, sobelY)

cv2.imshow("Sobel X", sobelX)
cv2.imshow("Sobel Y", sobelY)
cv2.imshow("Sobel Combined", sobelCombined)
cv2.waitKey(0)


