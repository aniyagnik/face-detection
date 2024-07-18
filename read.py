import cv2 as cv
#img = cv.imread('photos/berserk7.jpg')
#cv.imshow('berserk', img)
capture = cv.VideoCapture('videos/1.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.realease()
cv.destroyAllWindows()
