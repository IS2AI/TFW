# import the necessary packages
import pandas as pd
import numpy as np
import argparse
import cv2
import os

# construct argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
	help="path to the dataset")
ap.add_argument("-s", "--set", type=str, default="indoor",
	help="set: indoor/outdoor")
args = vars(ap.parse_args())

if args["set"] == "indoor":
	width = 3 
else:
	width = 2

# import labels as a numpy array
labels = pd.read_csv(os.path.join(args["dataset"], "{}.csv".format(args["set"]))).to_numpy()

# initialize iterators
iter1 = 0 
iter2 = 0

# loop over the rows
while iter1 < len(labels):
	# load the image
	imageName = labels[iter1][0]
	image = cv2.imread(os.path.join(args["dataset"], args["set"], imageName))

	# convert the image to grayscale
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = np.dstack([gray] * 3)

	print("[INFO] Processing image:", imageName)

	# loop over the labels of this image
	while labels[iter1][0] == labels[iter2][0]:
		# extract coordinates of the bounding box and five facial landmarks
		xs, ys, xe, ye, p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y, p5x, p5y = labels[iter2][1:]

		# draw the bounding box and facial landmarks 
		cv2.rectangle(gray, (xs, ys), (xe, ye), (0, 255, 0), width)
		cv2.circle(gray, (p1x, p1y), width, (0, 0, 255), -1)
		cv2.circle(gray, (p2x, p2y), width, (255, 0, 0), -1)
		cv2.circle(gray, (p3x, p3y), width, (0, 255, 255), -1)
		cv2.circle(gray, (p4x, p4y), width, (255, 0, 255), -1)
		cv2.circle(gray, (p5x, p5y), width, (255, 255, 0), -1)

		iter2 += 1

		# break the loop if we exceeded
		# the last row
		if iter2 == len(labels):
			break

	# equalize iterators
	iter1 = iter2

	#cv2.imwrite("labelled_outdoor.png", gray)

	# show the image
	cv2.imshow("Image", gray)
	key = cv2.waitKey(0) & 0xFF

	# if the `q` key was pressed, 
	# break from the loop
	if key == ord("q"):
		break
