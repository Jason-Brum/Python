def calcular_media(lista_numeros):
    if not lista_numeros:
        return "A lista está vazia. Não é possível calcular a média."
    return sum(lista_numeros) / len(lista_numeros)

# Solicita ao usuário que insira os números separados por espaço
entrada = input("Digite os números separados por espaço: ")

# Converte a entrada em uma lista de números
try:
    numeros = list(map(float, entrada.split()))
    media = calcular_media(numeros)
    print(f"A média dos números é: {media}")
except ValueError:
    print("Por favor, insira apenas números válidos.")