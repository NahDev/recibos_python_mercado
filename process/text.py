import re
import pandas as pd
from datetime import date


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
                    campos[0]: {
                        "produto": campos[2],
                        "valor_unt": campos[-2],
                        "valor": campos[-1],
                    }
                }
            )
    df = pd.DataFrame()

    for item in dados:
        for chave, valor in item.items():
            df = df._append(pd.Series(valor, name=chave))
    data_atual = date.today().strftime("%d-%m-%Y")

    nome_arquivo = f"./data/dados_{data_atual}.csv"

    # Salvar o DataFrame como um arquivo CSV
    df.to_csv(nome_arquivo)

    print(f"Arquivo {nome_arquivo} salvo com sucesso!")
    # Salvar o DataFrame em um arquivo CSV
    # for dado in dados:
    #     print(dado)
    # return dado
