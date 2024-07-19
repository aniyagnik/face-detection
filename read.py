import cv2
# frames = cv2.imread('photos/2.jpg')
# cv2.imshow('image', img)

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture('./videos/a.mp4')

if not (video_capture.isOpened()):
    print("Could not open video source")

while True:
    # Capture frame-by-frame
    ret, frames = video_capture.read()

    #resized_frames = cv2.resize(frames,(255,255))
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=10,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frames)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# cv2.waitKey(0)
video_capture.release()
cv2.destroyAllWindows()
