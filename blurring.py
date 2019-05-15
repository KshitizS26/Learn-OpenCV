import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

'''
blurring algorithm #1: averaging

define a k x k sliding window on top of input image

k is always an odd number

sliding window is called "a convolutional kernel" or "kernel"

kernel will slide over the image left-to-right and top-to-bottm

pixel at the center of this matrix is set to be the average of all pixels surronding it

size of kernel is proportional to level of blur
'''

# average blurring an image; requires image and size of the kernel
# np.hstack stacks our output images together horizontally

blurred = np.hstack([
	cv2.blur(image, (3, 3)),
	cv2.blur(image, (5, 5)),
	cv2.blur(image, (7,7))])

cv2.imshow("Averaged", blurred)
cv2.waitKey(0)

'''
blurring algorithm #2: gaussian

uses weighted mean; pixels closer to the center contribute more weight

yields naturally blurred images
'''

# gaussian blurring an image; accepts a third parameter "standard deviation" in the x-axis direction
# a value of 0 instructs OpenCV to automatically compute them based on our kernel size

blurred = np.hstack([
	cv2.GaussianBlur(image, (3, 3), 0),
	cv2.GaussianBlur(image, (5, 5), 0),
	cv2.GaussianBlur(image, (5, 5), 0)])

cv2.imshow("Gaussian", blurred)
cv2.waitKey(0)

'''
blurring algorithm #3: median

replace the central pixel with the median of the neighborhood

effective at removing salt-and-pepper style noise from an image

because each central pixel is always replaced with a pixel intensity 
that exists in the image

substantially reduces noise
'''

# median blurring an image; accepts the input image and kernel size

blurred = np.hstack([
	cv2.medianBlur(image, 3),
	cv2.medianBlur(image, 5),
	cv2.medianBlur(image, 7)])

cv2.imshow("Median", blurred)
cv2.waitKey(0)

'''
blurring algorithm #4: bilateral

reduces noise while still maintains edges

accomplishes this by introducing two gaussian distribution

first gaussian function only considers spatial neighbors - pixels that appear
close together in the (x, y) coordinate space of the image

second gaussian models the pixel intensity of the neighborhood - only
pixels with similar intensity are included in the actual computation of the blur

slower than other methods
''' 
# bilateral blurring; accepts input image, diameter of pixel neighborhood, color standard deviation, space standard deviation
# larger value of color deviation means more colors in the neighborhood will be considered when computing the blur
# larger value of space deviation means that pixels farther out from the central pixel will influence the blurring calculation,
# provided that their colors are similar enough

blurred = np.hstack([
	cv2.bilateralFilter(image, 5, 21, 21),
	cv2.bilateralFilter(image, 7, 31, 31),
	cv2.bilateralFilter(image, 9, 41, 41)])

cv2.imshow("Bilateral", blurred)
cv2.waitKey(0)











