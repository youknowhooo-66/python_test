import cv2

# 3. Converter imagem para Tons de Cinza e salvar

def main():
    imagem = cv2.imread('imagem.jpg')

    if imagem is None:
        print("Erro: 'imagem.jpg' não encontrada.")
        return

    # Converte para tons de cinza
    cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Salva a nova imagem
    cv2.imwrite('imagem_cinza.jpg', cinza)
    print("Imagem salva como 'imagem_cinza.jpg'")

    # Exibe original e cinza
    cv2.imshow('Original', imagem)
    cv2.imshow('Tons de Cinza', cinza)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
