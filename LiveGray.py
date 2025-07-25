import numpy as np
import cv2

webcam = cv2.VideoCapture(0)

while True:

    ret, frame = webcam.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Live Webcam", gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()