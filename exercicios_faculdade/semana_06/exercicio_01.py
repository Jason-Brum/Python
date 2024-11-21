def calcular_fatorial(numero):
    if numero < 0:
        return "Fatorial não é definido para números negativos."
    elif numero == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial

# Solicita ao usuário que insira um número
numero = int(input("Digite um número para calcular seu fatorial: "))
resultado = calcular_fatorial(numero)

# Exibe o resultado
print(f"O fatorial de {numero} é: {resultado}")