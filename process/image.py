import cv2
import pytesseract


def image_process(caminho_imagem):
    imagem = cv2.imread(caminho_imagem)

    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    texto = pytesseract.image_to_string(imagem_cinza, lang="por")

    return texto
