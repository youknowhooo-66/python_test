import cv2

# 1. Carregar e exibir uma imagem
# Certifique-se de ter uma imagem chamada 'imagem.jpg' no mesmo diretório ou mude o caminho.

def main():
    # Carrega a imagem
    imagem = cv2.imread('imagem.jpg')

    if imagem is None:
        print("Erro: Não foi possível carregar a imagem. Verifique se 'imagem.jpg' existe.")
        return

    # Exibe a imagem em uma janela
    cv2.imshow('Minha Imagem', imagem)

    # Espera qualquer tecla para fechar
    print("Pressione qualquer tecla na janela da imagem para fechar...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
