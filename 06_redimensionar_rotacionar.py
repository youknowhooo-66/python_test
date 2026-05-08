import cv2

# 6. Redimensionar e Rotacionar Imagem

def main():
    imagem = cv2.imread('imagem.jpg')

    if imagem is None:
        print("Erro: 'imagem.jpg' não encontrada.")
        return

    # 1. Redimensionar
    # largura, altura
    largura_nova = 400
    altura_nova = 300
    redimensionada = cv2.resize(imagem, (largura_nova, altura_nova))

    # 2. Rotacionar
    (h, w) = imagem.shape[:2]
    centro = (w // 2, h // 2)
    # matriz de rotação: centro, ângulo (graus), escala
    M = cv2.getRotationMatrix2D(centro, 45, 1.0)
    rotacionada = cv2.warpAffine(imagem, M, (w, h))

    cv2.imshow('Redimensionada', redimensionada)
    cv2.imshow('Rotacionada', rotacionada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
