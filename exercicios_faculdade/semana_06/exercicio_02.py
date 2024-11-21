def calcular_fatorial(numero):
    if numero < 0:
        return "Fatorial não é definido para números negativos."
    elif numero == 0 or numero == 1:
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)

# Solicita ao usuário que insira um número
numero = int(input("Digite um número para calcular seu fatorial: "))
resultado = calcular_fatorial(numero)

# Exibe o resultado
print(f"O fatorial de {numero} é: {resultado}")
