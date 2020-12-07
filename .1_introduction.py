import cv2

# import and show image
# img = cv2.imread("./resources/img.png") # Reading image
# cv2.imshow("Output", img) # Displaying image
# cv2.waitKey(0) # Show image for unlimited time adn wait for key to shut down

# import and show video
# video = cv2.VideoCapture("./resources/video.mp4")  # Reading Video
# while True:  # Looping frames
#     success, img = video.read()  # Reading frames
#     cv2.imshow("Video", img)  # Showing Frames
#     if cv2.waitKey(1) & 0xFF == ord('q'):  # If q is pressed it closes
#         break

# import and show webcam
# webcam = cv2.VideoCapture(0)  # Reading Webcam (0 is default)
# webcam.set(3, 640) # width
# webcam.set(4, 480) # height
# webcam.set(10, 100) # brightnes
# while True:  # Looping frames
#    success, img = webcam.read()  # Reading frames
#    cv2.imshow("Webcam", img)  # Showing Frames
#    if cv2.waitKey(1) & 0xFF == ord('q'):  # If q is pressed it closes
#        break
