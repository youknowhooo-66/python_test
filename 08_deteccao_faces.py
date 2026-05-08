import cv2

# 8. Detecção de Faces com Haar Cascades

def main():
    # Carrega o classificador pré-treinado de faces
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    imagem = cv2.imread('imagem.jpg')

    if imagem is None:
        print("Erro: 'imagem.jpg' não encontrada.")
        return

    cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Detecta faces
    faces = face_cascade.detectMultiScale(cinza, 1.1, 4)

    # Desenha retângulos em volta das faces
    for (x, y, w, h) in faces:
        cv2.rectangle(imagem, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('Faces Detectadas', imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
