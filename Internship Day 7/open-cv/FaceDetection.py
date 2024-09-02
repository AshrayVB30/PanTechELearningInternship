import cv2

# Load pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start video capture from default webcam
cap = cv2.VideoCapture(0)

while True:
    # read a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        break
    # convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+y, y+h), (255, 0, 0), 2)
    # Display the frame with detected faces
    cv2.imshow('REAL-TIME FACE DETECTION', frame)

    # break loop if user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV window
cap.release()
cv2.destroyAllWindows()