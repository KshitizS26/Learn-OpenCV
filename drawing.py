import numpy as np
import cv2
import argparse

# ap = argparse.ArgumentParser()
# ap.add_argument("-f", "--flag", required = True, help = "Pass 1 to draw a circle")
# args = vars(ap.parse_args())
# print(args)

# pass 0 to --flag to draw lines and rectangle
# if not args["flag"]:

'''
dimension of the canvas: 300x300 with 3 color channels
dtype = 'uint8': 8 bit unsigned integer whoses range is 0-255
other common dtypes: 32-bit integers, 32-bit, 64-bit floats
'''
canvas = np.zeros((300, 300, 3), dtype = "uint8")

# define a tuple to represent the color "green"
green = (0, 255, 0)

# draw a green line from point (0, 0) to point (300, 300)
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# define a tuple to represen the color "red"
red = (0, 0, 255)

# draw a red line from point (300, 0) to point (0, 300) with thickness of 3 pixels
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# draw a green rectangle from point (10, 10) to point (60, 60) defining a region of 50x50 pixels
cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

blue = (255, 0, 0)

# drawing a filled rectangle by passing -1 argument to thickness
cv2.rectangle(canvas, (200, 50), (255, 125), blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# pass 1 to --flag to draw a circle
# elif args["flag"]:

# initializing a fresh canvas
canvas = np.zeros((300, 300, 3), dtype = "uint8")

# represent the (x, y) coordinates of the center of the image
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)

white = (255, 255, 255)

# looping over a number of radius values, starting from 0 and ending at 150 incrementing by 25 at each step
for r in range(0, 175, 25):
	# (centerX, centerY): center; r: radius; white: color of the circle
	cv2.circle(canvas, (centerX, centerY), r, white)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# pass 2 to --flag to draw abstract image
# elif args["flag"] == 2:

# initializing a fresh canvas
canvas = np.zeros((300, 300, 3), dtype = "uint8")

# drawing 25 random circles
for i in range(0, 25):

	# generating a radius in the range [5, 200); this value controls how large our circle will be
	radius = np.random.randint(5, high = 200)
	# randomly generating a list containing color in the range [0, 255] with 3 color channels 
	color = np.random.randint(0, high = 256, size = (3,)).tolist()
	# generating (x, y) point to draw the circle; generating a point in the range [0, 300)
	pt = np.random.randint(0, high = 300, size = (2,))
	# thickness = -1: solid color circles
	cv2.circle(canvas, tuple(pt), radius, color, -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)