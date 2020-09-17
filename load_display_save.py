from __future__ import print_function
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
        help = "Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

print("Width: {} pixels".format(image.shape[1]))
print("Height: {} pixels".format(image.shape[0]))
print("Channel: {} ".format(image.shape[2]))

cv2.imshow("Image", image)
cv2.waitKey()

cv2.imwrite("newImage.jpg", image)

