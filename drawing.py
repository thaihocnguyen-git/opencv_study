import cv2
import numpy as np

canvas = np.zeros((300,300,3), dtype="uint8")

green = (0,255,0)
red = (0,0,255)

cv2.line(canvas, (0,0), (300,300), green,3)
cv2.line(canvas, (300,0), (0,300), red,3)
cv2.rectangle(canvas, (10,10),(60,60), red, -1)

cv2.imshow("image", canvas)
cv2.waitKey()
