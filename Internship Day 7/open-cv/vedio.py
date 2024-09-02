import cv2

video_path = 'images/namaste.mp4'

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print('Error: Ur video is not found')
    exit()

# Loop through the frames of the video
while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # if the frame was not read successfully, exit the loop
    if not ret:
        break

    # display the frame
    cv2.imshow('Frame ',frame)

    # wait for the key press to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()