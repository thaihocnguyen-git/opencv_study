#import libraries
from __future__ import print_function
import cv2 as cv
import argparse

#read argsments from command
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", required=True,
                help = "Path to image")
args = vars(ap.parse_args())

#read image from path
image = cv.imread(args["image"])

#change the 100x100 top left corner to green
image[:100,:100] = (255, 0, 0)
cv.imshow("Changed",image)
cv.waitKey()
