#Crie um programa que solicite ao usuário duas listas com cinco elementos cada e, como resultado, crie uma terceira lista que intercale os elementos das anteriores.

# Inicializa uma lista vazia para armazenar os números digitados pelo usuário
nums = [] 
# Inicializa listas vazias para armazenar números maiores e menores que a média

maiores = []
menores = []
# Inicializa a variável soma com 0 para acumular a soma dos números
soma = 0
# Loop para solicitar ao usuário que insira 6 números
for _ in range (6):
    num = int(input("Digite 6 números: ")) # Lê um número inteiro do usuário
    nums.append(num) # Adiciona o número na lista 'nums'
    soma = soma + num # Atualiza a soma com o número digitado
# Calcula a média dividindo a soma total pelo número de entradas (6)
media = soma / 6
# Loop para classificar os números em 'maiores' ou 'menores' de acordo com a média

for num in nums: # Loop para classificar os números em 'maiores' ou 'menores' de acordo com a média

    if num >= media:
        maiores.append(num) # Adiciona o número à lista 'maiores' se for maior ou igual à média
    else:
        menores.append(num) # Adiciona o número à lista 'menores' se for menor que a média
print(f'A média dos 6 números é {media}')
print(f'Os números iguais ou maiores que a média são {maiores}')
print(f'Os números menores que a média são {menores}')                