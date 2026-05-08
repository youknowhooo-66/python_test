import cv2
import numpy as np

# 9. Segmentação de Cores (Filtrar Azul)

def main():
    # Podemos usar uma imagem ou webcam
    cap = cv2.VideoCapture(0)

    print("Mostre algo azul para a câmera (ou ajuste os valores HSV).")
    print("Pressione 'q' para sair.")

    while True:
        ret, frame = cap.read()
        if not ret: break

        # Converte para espaço de cor HSV (melhor para cores)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Define o intervalo da cor azul no HSV
        azul_baixo = np.array([100, 150, 0])
        azul_alto = np.array([140, 255, 255])

        # Cria uma máscara que contém apenas pixels azuis
        mask = cv2.inRange(hsv, azul_baixo, azul_alto)

        # Aplica a máscara na imagem original (Bitwise-AND)
        resultado = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow('Original', frame)
        cv2.imshow('Mascara', mask)
        cv2.imshow('Apenas Azul', resultado)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
