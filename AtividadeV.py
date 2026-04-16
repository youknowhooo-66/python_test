import cv2

video = cv2.VideoCapture("video.mp4")

# Desafio extra: trocar o nome da janela do vídeo e exibir uma mensagem no terminal quando o vídeo terminar.
window_name = "Reprodução de Vídeo"
cv2.namedWindow(window_name)

while True:
    ret, frame = video.read()

    if not ret:
        print("Vídeo encerrado.") # Mensagem quando o vídeo terminar
        break

    cv2.imshow(window_name, frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()