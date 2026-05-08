import cv2

# 4. Detecção de Bordas (Algoritmo Canny)

def main():
    imagem = cv2.imread('imagem.jpg')

    if imagem is None:
        print("Erro: 'imagem.jpg' não encontrada.")
        return

    # Converte para cinza primeiro (geralmente melhor para bordas)
    cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Aplica o detector de bordas Canny
    # 100 e 200 são os limites de limiar (thresholds)
    bordas = cv2.Canny(cinza, 100, 200)

    cv2.imshow('Bordas Detectadas', bordas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
