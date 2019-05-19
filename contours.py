import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)
cv2.imshow("Blurred", image)

canny = cv2.Canny(blurred, 30, 150)
cv2.imshow("Edged", canny)

# cv2.findCountours - find contours of the outlines
# _, cnts, _ - our image after applying contour detection, the contours themselves, 
# the hierarchy of the contours
# edged.copy() - edged image
# cv2.RETR_EXTERNAL - retrives only the outermost contours (that follows the outline)
# cv2.RETR_LIST - grab all contours
# other methods include hierarchical contours - cv2.RETR_COMP, cv2.RETR_TREE
# cv2.CHAIN_APPROX_SIMPLE - method to approximate the contour; compress horizontal, vertical
# and diagonal segments into their end-points only
(_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("I count {} count in this image".format(len(cnts)))

coins = image.copy()
cv2.drawContours(coins, cnts, -1, (0, 255, 0), 2)
cv2.imshow("Coins", coins)
cv2.waitKey(0)

cv2.drawContours(coins, cnts, 0, (0, 255, 0), 2)
cv2.drawContours(coins, cnts, 1, (0, 255, 0), 2)
cv2.drawContours(coins, cnts, 2, (0, 255, 0), 2)

for (i, c) in enumerate(cnts):
	(x, y, w, h) = cv2.boundingRect(c)
	print("Coin #{}".format(i+1))
	coin = image[y:y + h, x:x + w]
	cv2.imshow("Coin", coin)
	mask = np.zeros(image.shape[:2], dtype = "uint8")
	((centerX, centerY), radius) = cv2.minEnclodingCircle(c)
	cv2.circle(mask, (int(centerX), int(centerY)), int(radius), 255, -1)
	mask = mask[y:y + h, x:x + w]
	cv2.imshow("Masked Coin", cv2.bitwise_and(coin, coin, mask = mask))
	cv2.waitKey(0)






