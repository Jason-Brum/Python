# DICIONÁRIOS

# Para adicionar um novo item ao dicionário, podemos simplesmente atribuir um valor a uma nova chave, como por exemplo:

pessoa = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}

pessoa["profissao"] = "engenheiro"
print(pessoa)

#Isso adiciona a chave profissao ao dicionário pessoa com o valor "engenheiro". Simples assim!

meu_dicionario = {
    "a": 1,
    "b": 2,
    "c": 3
}

print("------------")

del meu_dicionario["b"]
print(meu_dicionario)