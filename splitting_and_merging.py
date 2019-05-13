import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

# unpacking the RGB tuple in reverse channel order due to OpenCV's support of BGR
(B, G, R) = cv2.split(image)

# showing each channel individually
cv2.imshow("Red", R)
cv2.waitKey(0)
cv2.imshow("Green", G)
cv2.waitKey(0)
cv2.imshow("Blue", B)
cv2.waitKey(0)

# merging individual channels
merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

# alternate method to visualize the actual color of the channel of an image

# constructing NumPy array of same width and height as the image
zeros = np.zeros(image.shape[:2], dtype = "uint8")
# constructing the red channel representation
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
# constructing the green channel representation
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
# constructing the blue channel representation
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
cv2.waitKey(0)


