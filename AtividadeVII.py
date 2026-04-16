import cv2
import os

# Abre a webcam
cam = cv2.VideoCapture(0)

# Define a pasta de saída e cria se não existir
pasta_saida = "Saida"
if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)

# Contador para nomear as fotos salvas
foto_contador = 1

while True:
    ret, frame = cam.read()

    if not ret:
        print("Erro ao capturar frame da webcam.")
        break

    cv2.imshow("Webcam ao Vivo", frame)

    tecla = cv2.waitKey(1)

    # Salva a imagem se a tecla 's' for pressionada
    if tecla == ord('s'):
        nome_foto = os.path.join(pasta_saida, f"foto_{foto_contador}.jpg")
        cv2.imwrite(nome_foto, frame)
        print(f"Foto salva como: {nome_foto}")
        foto_contador += 1

    # Encerra o programa se a tecla 'q' for pressionada
    if tecla == ord('q'):
        break

# Libera a webcam e fecha todas as janelas
cam.release()
cv2.destroyAllWindows()
print("Programa encerrado.")