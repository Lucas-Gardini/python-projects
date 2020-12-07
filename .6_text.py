import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
cv2.putText(img, "OPENCV - Vem pro cv!", (50, 100),
            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1)
cv2.imshow("Image", img)
cv2.waitKey(0)
