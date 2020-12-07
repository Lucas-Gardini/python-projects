import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier(
    "./resources/xml/haarcascade_frontalface_default.xml")

webcam = cv2.VideoCapture(0)  # Reading Webcam (0 is default)
webcam.set(3, 640)  # width
webcam.set(4, 480)  # height
webcam.set(10, 100)  # brightnes

while True:  # Looping frames
    success, img = webcam.read()  # Reading frames
    imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow("Webcam", img)  # Showing Frames
    if cv2.waitKey(1) & 0xFF == ord('q'):  # If q is pressed it closes
        break

# for (x, y, w, h) in faces:
#    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
#
#cv2.imshow("Image", img)
# cv2.waitKey(0)
