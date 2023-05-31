from process.image import image_process
from process.text import text_process


caminhoimagem = "comprovantes/comprovante_dia.jpeg"

pimagem = image_process(caminhoimagem)
text_process(pimagem)
