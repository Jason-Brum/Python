
#Exemplo de aplicação 2: Elabore um programa que solicite ao usuário cinco números e exiba duas listas separadas: uma contendo somente números pares e outra contendo somente números ímpares. 

pares = []
impares = []
for i in range(5):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print("Números pares:", pares, "- Números ímpares:", impares)