import cv2

# 7. Suavização (Blur)

def main():
    imagem = cv2.imread('imagem.jpg')

    if imagem is None:
        print("Erro: 'imagem.jpg' não encontrada.")
        return

    # Suavização Gaussiana (ajuda a remover ruído)
    # (5, 5) é o tamanho do kernel (deve ser ímpar)
    gaussiano = cv2.GaussianBlur(imagem, (5, 5), 0)

    # Suavização por Mediana (ótimo para ruído 'sal e pimenta')
    mediana = cv2.medianBlur(imagem, 5)

    cv2.imshow('Original', imagem)
    cv2.imshow('Blur Gaussiano', gaussiano)
    cv2.imshow('Blur Mediana', mediana)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
