import cv2
import numpy as np

# Capture video from the default camera
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video capture
    ret, frame = cap.read()

    # Display the original color video frame
    cv2.imshow('ORIGINAL VIDEO COLOR', frame)

    # Resize the frame to 350x350 pixels
    frame = cv2.resize(frame, (350, 350))
    cv2.imshow('RESIZED FRAME', frame)

    # Convert the resized frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('GREY CONVERSION VIDEO', gray)

    # Apply a binary threshold to the grayscale frame
    ret, bw = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    cv2.imshow('BLACK AND WHITE CONVERSION', bw)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
