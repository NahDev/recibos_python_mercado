import re


def text_process(texto):
    linhas = texto.split("\n")
    padrao_numeros = r"^\d{3}"
    padrao_total = r"^TOTAL"
    dados = []

    for linha in linhas:
        if re.match(padrao_numeros, linha) or re.match(padrao_total, linha):
            campos = linha.split(" ")
            # if len(campos) <= 8:
            dados.append(
                {
                    "id": campos[0],
                    "produto": campos[2],
                    "valor_unt": campos[-2],
                    "valor": campos[-1],
                }
            )

    return dados
