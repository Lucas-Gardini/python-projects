import cv2
import numpy as np

img = cv2.imread("./resources/truck.png")


# basically, get an especific object or something like that from an image using four points (the four cornes) and display it as an cropped image with a "normal" loooking perspective
width, height = 600, 200
pts1 = np.float32([[317, 87], [468, 97], [324, 141], [485, 149]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow("Image", img)
cv2.imshow("Image with perspective", imgOutput)
cv2.waitKey(0)
