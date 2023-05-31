from process.image import image_process
from process.text import text_process


caminhoimagem = "comprovantes/comprovante_dia.jpeg"

pimagem = image_process(caminhoimagem)

dados = text_process(pimagem)
for dado in dados:
    print(len(dado))
# print(analise)
