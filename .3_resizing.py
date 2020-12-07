import cv2
import numpy as np

img = cv2.imread("./resources/img.png")
print(img.shape)

imgResized = cv2.resize(img, (300, 200))
print(imgResized.shape)

cv2.imshow("Image", img)
cv2.imshow("Image Resized", imgResized)
cv2.waitKey(0)
