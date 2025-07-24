import numpy as np
import cv2

# Abrindo a webcam
webcam = cv2.VideoCapture(0)

while True:
    # Variável para ler a webcam
    ret, frame = webcam.read()

    # Se não conseguir capturar, para o Loop
    if not ret:
        break

    # Webcam espelhada
    espelhada = cv2.flip(frame, 1)

    # Variável de comparação entre espelhada e não espelhada
    comparacao = np.hstack((frame, espelhada))

    # Mostra o frame capturado
    cv2.imshow("Live Webcam", comparacao)

    if cv2.waitKey(1) & 0xFF == ord('p'):
        break

webcam.release()
cv2.destroyAllWindows()