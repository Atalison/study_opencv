import numpy as np
import cv2

# Carrega o Haarcascade
frontal_face = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

webcam = cv2.VideoCapture(0)

while True:
    # Variável para leitura da webcam
    ret, frame = webcam.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = frontal_face.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)


    # Desenha os retangulos
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 255, 0), 2)


    # Exibe frame com rostos marcados
    cv2.imshow("Rostos", frame)

    # Sai do loop após precionar 'p'
    if cv2.waitKey(1) & 0xFF == ord('p'):
        break

webcam.release()
cv2.destroyAllWindows()

