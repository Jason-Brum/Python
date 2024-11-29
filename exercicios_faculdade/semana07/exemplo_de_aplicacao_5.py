import json

dados = {
  "nome": "João",
  "idade": 25,
  "cidade": "Curitiba",
  "frutas_favoritas": 
  [
    "maçã",
    "banana",
    "laranja"
  ]

}


with open("pessoa.json", "w", encoding="utf-8") as arquivo:

    json.dump(dados, arquivo, ensure_ascii=False)