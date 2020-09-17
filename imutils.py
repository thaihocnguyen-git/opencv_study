import numpy as np
import cv2
import matplotlib.pyplot as plt
import os 
import requests

#donwload haarcascade_frontal_model
haarcascades_url = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml"
haarcascades_fn = haarcascades_url.split("/")[-1]
if (!os.path.exists(haarcascades_fn))
downloaded_object = requests.get(haarcascades_url)
with open(haarcascades_fn, "wb") as file:
  file.write(downloaded_object.content)

#create haarcascade model 
FACE_CASECADE = cv2.CascadeClassifier(haarcascades_fn)

#detect face function
def detectFace(image):
  x,y,w,h = FACE_CASECADE.detectMultiScale(image, 1.1, 4)[0]
  faceImage = image[y:y+w, x:x+h]
  return faceImage


def translate(image, x,y):
    M = np.float32([[1,0,x],[0,1,y]])
    shifted = cv2.warpAffine(image, M, (image.shape[1],
                                        image.shape[0]))
    return shifted


def rotate(image, angle, center=None, scale=1.0):
    (h, w) = image.shape[:2]

    if center is None:
        center = (w//2, h//2)

    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpaffine(image, M, (w,h))
    return rotated


def resize(image, width=None, height=None,
           inter=cv2.INTER_AREA ):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image

    if width is None:
        r = height/h
        dim = (int(w*r), height)

    elif height is None:
        r = width/w
        dim = (width, int(r*h))

    else:
        dim = (width,height)

    resized = cv2.resize(image, dim, inter)

    return resized
