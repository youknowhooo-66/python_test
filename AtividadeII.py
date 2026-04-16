import cv2
import os

imagem = cv2.imread("foto.jpg")

# Desafio extra: criar uma pasta chamada Saida/ e salvar a nova imagem dentro dela
pasta_saida = "Saida"
if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)

cv2.imwrite(os.path.join(pasta_saida, "copia.jpg"), imagem)