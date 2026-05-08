import cv2
import numpy as np

# 5. Desenhando Formas Geométricas

def main():
    # Cria uma imagem preta de 512x512 pixels
    img = np.zeros((512, 512, 3), np.uint8)

    # Desenha uma linha diagonal azul (BGR: 255, 0, 0)
    cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

    # Desenha um retângulo verde
    cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

    # Desenha um círculo vermelho
    cv2.circle(img, (447, 63), 63, (0, 0, 255), -1) # -1 preenche o círculo

    # Escreve texto na imagem
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, 'OpenCV Python', (10, 500), font, 2, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('Desenhos', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
