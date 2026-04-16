import cv2
import os

# Abre a webcam
cam = cv2.VideoCapture(0)

# Define a pasta de saída e cria se não existir
pasta_saida = "Saida"
if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)

# Define as coordenadas para o recorte (região central aproximada)
# Estas coordenadas podem precisar ser ajustadas dependendo da resolução da webcam
altura_frame = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
largura_frame = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))

# Exemplo: Recorte central de 200x200 pixels
centro_y, centro_x = altura_frame // 2, largura_frame // 2
altura_recorte, largura_recorte = 200, 200

x_inicio = max(0, centro_x - largura_recorte // 2)
y_inicio = max(0, centro_y - altura_recorte // 2)
x_fim = min(largura_frame, centro_x + largura_recorte // 2)
y_fim = min(altura_frame, centro_y + altura_recorte // 2)

# Desenha um retângulo na tela para indicar a área de recorte (Desafio)
# A cor é BGR (Azul, Verde, Vermelho). Aqui usamos Verde.
cor_retangulo = (0, 255, 0)
espessura_retangulo = 2

while True:
    ret, frame = cam.read()

    if not ret:
        print("Erro ao capturar frame da webcam.")
        break

    # Desenha o retângulo na imagem atual para visualizar a área de recorte
    # O retângulo será desenhado sobre o frame antes de exibi-lo
    frame_com_retangulo = frame.copy() # Copia o frame para não modificar o original antes do recorte
    cv2.rectangle(frame_com_retangulo, (x_inicio, y_inicio), (x_fim, y_fim), cor_retangulo, espessura_retangulo)

    cv2.imshow("Webcam com area de recorte", frame_com_retangulo)

    tecla = cv2.waitKey(1)

    # Captura e salva a imagem e o recorte se a tecla 's' for pressionada
    if tecla == ord('s'):
        # Salva a imagem original (Desafio)
        nome_original = os.path.join(pasta_saida, "imagem_original_capturada.jpg")
        cv2.imwrite(nome_original, frame)
        print(f"Imagem original salva como: {nome_original}")

        # Recorta a área especificada do frame original
        recorte = frame[y_inicio:y_fim, x_inicio:x_fim]

        # Salva o recorte
        nome_recorte = os.path.join(pasta_saida, "recorte_central.jpg")
        cv2.imwrite(nome_recorte, recorte)
        print(f"Recorte salvo como: {nome_recorte}")

    # Encerra o programa se a tecla 'q' for pressionada
    if tecla == ord('q'):
        break

# Libera a webcam e fecha todas as janelas
cam.release()
cv2.destroyAllWindows()
print("Programa encerrado.")