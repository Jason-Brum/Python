# Dados das pessoas em formato de lista de dicionários

pessoas = [
    {'nome': 'João', 'altura': 1.75, 'peso': 70},
    {'nome': 'Maria', 'altura': 1.60, 'peso': 55},
    {'nome': 'Carlos', 'altura': 1.80, 'peso': 90}
]

# Cálculo do IMC para cada pessoa

for pessoa in pessoas:
    altura = pessoa['altura']
    peso = pessoa['peso']
    imc = peso / (altura ** 2)
    print(f'O IMC de {pessoa["nome"]} é {imc:.2f}')

print("Continuando o cálculo para uma nova lista de pessoas.")
print("Este aqui é só um print para demonstrar o código.")

# Dados das pessoas em formato de lista de dicionários

novas_pessoas = [
    {'nome': 'Cézar', 'altura': 1.78, 'peso': 79},
    {'nome': 'Marta', 'altura': 1.61, 'peso': 52},
    {'nome': 'Ana', 'altura': 1.65, 'peso': 70}
]

# Cálculo do IMC para cada pessoa

for pessoa in novas_pessoas:
    altura = pessoa['altura']
    peso = pessoa['peso']
    imc = peso / (altura ** 2)
    print(f'O IMC de {pessoa["nome"]} é {imc:.2f}')


print("Agora, vamos para a lista final.")

# Dados das pessoas em formato de lista de dicionários

mais_pessoas = [
    {'nome': 'Kauane', 'altura': 1.53, 'peso': 51}
]

# Cálculo do IMC para cada pessoa

for pessoa in mais_pessoas:
    altura = pessoa['altura']
    peso = pessoa['peso']
    imc = peso / (altura ** 2)
    print(f'O IMC de {pessoa["nome"]} é {imc:.2f}')