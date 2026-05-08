import cv2

# 2. Capturar vídeo da webcam

def main():
    # Abre a conexão com a webcam (0 é o índice padrão)
    cap = cv2.VideoCapture(0)

    # Define a nova resolução (largura, altura)
    width = 1280
    height = 720

    # Aplica as configurações de resolução
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    print("Instruções:")
    print("1. Aperte 'p' para pausar e selecionar a área.")
    print("2. Use o mouse para desenhar o retângulo.")
    print("3. Aperte 'ENTER' ou 'SPACE' para confirmar o corte.")
    print("4. Aperte 'q' para sair.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('Camera - Aperte P para selecionar', frame)
        key = cv2.waitKey(1)

        if key == ord('p'):
            # Abre a interface de seleção (ROI)
            # showCrosshair=True mostra uma cruz no meio da seleção
            # fromCenter=False permite desenhar do canto para o outro
            roi = cv2.selectROI('Camera - Aperte P para selecionar', frame, showCrosshair=True)
            
            # roi retorna (x, y, largura, altura)
            x, y, w, h = roi

            # Verifica se o usuário realmente selecionou algo (evita erro de área zero)
            if w > 0 and h > 0:
                # Recorta a imagem usando os valores da ROI
                recorte = frame[int(y):int(y+h), int(x):int(x+w)]
                
                # Salva o arquivo
                cv2.imwrite('recorte_manual.jpg', recorte)
                print(f"Área salva com sucesso! Dimensões: {w}x{h}")
                
                # Mostra o que foi salvo por 2 segundos
                cv2.imshow('Recorte Salvo', recorte)
                cv2.waitKey(2000)
                cv2.destroyWindow('Recorte Salvo')

        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
