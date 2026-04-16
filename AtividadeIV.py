import cv2
import os

img = cv2.imread("foto.jpg")

# Criar a pasta Saida/ se não existir
pasta_saida = "Saida"
if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)

# Primeiro detalhe: placa
detalhe_placa = img[150:250, 300:400]
cv2.imwrite(os.path.join(pasta_saida, "detalhe_placa.jpg"), detalhe_placa)

# Segundo detalhe: roda (exemplo, ajuste as coordenadas conforme a imagem)
detalhe_roda = img[350:450, 50:150] # Novas coordenadas para um segundo detalhe
cv2.imwrite(os.path.join(pasta_saida, "detalhe_roda.jpg"), detalhe_roda)