from __future__ import print_function
from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

# splittig the image into three channels i BGR
chans = cv2.split(image)
colors = ("b", "g", "r")
plt.figure()
plt.title("Flattened Color Histograms")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

# looping over each of the channels in the image
for (chan, color) in zip(chans, colors):
	hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
	plt.plot(hist, color = color)
	plt.xlim([0, 256])

plt.show()

'''
building a multi-dimensional histogram that considers two channels at a time
bins to consider: 8 x 8, 32 x 32, 64 x 64; because 256 x 256 is a wasteful resource
'''

fig = plt.figure()
ax = fig.add_subplot(131)
# passing green and blue channels
hist = cv2.calcHist([chans[1], chans[0]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D Color Histogram for G and B")
plt.colorbar(p)

ax = fig.add_subplot(131)
# passing green and red channels
hist = cv2.calcHist([chans[1], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D Color Histogram for G and R")
plt.colorbar(p)

ax = fig.add_subplot(131)
# passing blue and red channels
hist = cv2.calcHist([chans[0], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D Color Histogram for B and R")
plt.colorbar(p)

print("2D Histogram Shape: {}, with {} values".format(hist.shape, hist.flatten().shape[0]))

'''
building a multi-dimensional histogram that considers three channels at a time
bins to consider: 8 x 8, 32 x 32, 64 x 64; because 256 x 256 is a wasteful resource
'''
hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
print("3D Histogram shape: {}, with {} values".format(hist.shape, hist.flatten().shape[0]))

plt.show()
