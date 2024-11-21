def fatorial(numero):
    # segundo as propriedades de fatorial
    if numero == 0:
        return 1
 
    fat = 1
    for i in range(numero, 0, -1):
        fat *= i
    return fat
 
numero = int(input("Digite um número inteiro para calcular seu fatorial: "))
fat = fatorial(numero)
print(f"O fatorial de {numero} é {fat}")