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

print(type(image))
print(image.shape)

print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
print("channels: {}".format(image.shape[2]))

cv2.imshow("Image", image)

# call to cv2.waitKey pauses the execution of the script until we press a key
# using a parameter of 0 indicates that nay keypress will un-pause the execution
cv2.waitKey(0)

cv2.imwrite(args["output"], image)
