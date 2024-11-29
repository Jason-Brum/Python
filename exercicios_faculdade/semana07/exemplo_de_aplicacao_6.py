import json

with open("pessoa.json", "r", encoding="utf-8") as arquivo:

    dados_lidos = json.load(arquivo)

print(dados_lidos)