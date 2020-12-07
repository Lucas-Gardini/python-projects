import cv2
import numpy as np

img = cv2.imread("./resources/img.png")
imgCropped = img[0:200, 200:500]  # height, width

cv2.imshow("Image", img)
cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(0)
