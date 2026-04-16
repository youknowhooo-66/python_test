import cv2
print(cv2.__version__)

# Imagem 1
imagem1 = cv2.imread("./17.jpeg")
cv2.imshow("Imagem 1", imagem1)

# Imagem 2 (adicionado para o desafio)
imagem2 = cv2.imread("./18.jpeg")
cv2.imshow("Imagem 2", imagem2)

cv2.waitKey(0) # Aguarda até que uma tecla seja pressionada
cv2.destroyAllWindows() # Fecha todas as janelas abertas