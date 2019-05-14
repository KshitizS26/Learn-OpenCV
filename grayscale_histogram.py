'''
Histogram represent the distribution of pixel intensities in an image
Gives high-level intuition of the intensity (pixel value) distribution
'''

from matplotlib import pyplot as plt
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)
# converting image from RGB to grayscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", image)
cv2.waitKey(0)

'''
plotting a histogram of pixel intensities
[image]: image to use
[0]: color channel; 0 for grayscale, [0, 1, 2] for RGB
None: mask
[256]: number of bins
[0, 256]: range of pixel intensities
'''
hist = cv2.calcHist([image], [0], None, [256], [0, 256])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)