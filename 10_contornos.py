import cv2

# 10. Detecção de Contornos

def main():
    imagem = cv2.imread('imagem.jpg')

    if imagem is None:
        print("Erro: 'imagem.jpg' não encontrada.")
        return

    # Converte para cinza e aplica limiar (threshold)
    cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(cinza, 127, 255, 0)

    # Encontra contornos
    contornos, hierarquia = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Desenha todos os contornos na imagem original
    # -1 significa todos, (0,255,0) é verde, 3 é a espessura
    cv2.drawContours(imagem, contornos, -1, (0, 255, 0), 3)

    cv2.imshow('Contornos Detectados', imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
