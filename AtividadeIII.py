import cv2
import os

img = cv2.imread("foto.jpg")

# Desafio: fazer 2 recortes diferentes da mesma imagem e salvar cada recorte com um nome diferente.
# Criar a pasta Saida/ se não existir
pasta_saida = "Saida"
if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)

# Primeiro recorte
recorte1 = img[100:300, 200:400]
cv2.imshow("Recorte 1", recorte1)
cv2.imwrite(os.path.join(pasta_saida, "recorte1.jpg"), recorte1)

# Segundo recorte
recorte2 = img[50:150, 50:150] # Novas coordenadas para o segundo recorte
cv2.imshow("Recorte 2", recorte2)
cv2.imwrite(os.path.join(pasta_saida, "recorte2.jpg"), recorte2)

cv2.waitKey(0)
cv2.destroyAllWindows()