# DICIONÁRIOS

# criação de um dicionário com algumas informações
pessoa = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}

# percorrendo as chaves do dicionário
for chave in pessoa:
    print(chave)
    
for chave in pessoa.keys():
    print(chave)
    
# percorrendo os valores do dicionário
for valor in pessoa.values():
    print(valor)
    
# percorrendo as chaves e valores do dicionário ao mesmo tempo
for chave, valor in pessoa.items():
    print(chave, valor)