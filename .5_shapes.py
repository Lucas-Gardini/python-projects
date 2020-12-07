import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)  # 0 is black (matrix of zeros)
# img[:] = 255, 0, 0 # painting the whole image
# green line from beggining to end
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255),
              cv2.FILLED)  # filled rectangle
cv2.circle(img, (400, 50), 30, (255, 255, 0), 5)  # circle

cv2.imshow("Image", img)
cv2.waitKey()
