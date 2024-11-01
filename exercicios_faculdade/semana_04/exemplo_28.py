# DICIONÁRIOS

# criação de um dicionário com algumas informações
estoque = {
    'banana': 10,
    'maçã': 5,
    'laranja': 8
}

# percorrendo as chaves e valores do dicionário e exibindo informações sobre o estoque
for chave, valor in estoque.items():
    print(f"Temos {valor} unidades de {chave} em estoque.")

# Aqui, temos um dicionário chamado estoque que armazena a quantidade de frutas disponíveis em um estabelecimento. A estrutura do dicionário é formada pelas chaves (que representam o nome das frutas) e pelos valores (que representam a quantidade de cada fruta).

# Para percorrer o dicionário, o código utiliza o método items() para obter uma lista de tuplas (lembra delas?) contendo as chaves e valores do dicionário. Em seguida, um loop for é utilizado para percorrer cada uma das tuplas e exibir a quantidade de cada fruta disponível em estoque.

# O código utiliza a função print() para exibir as informações na tela. Veja como formatamos uma frase mais bonita usando f-strings na última linha do código para facilitar a exibição das informações. Outra forma de mostrar os mesmos valores seria:

print(---------------------)

for chave in estoque.keys():
    print(f"Temos {estoque[chave]} unidades de {chave} em estoque.")