qtdePares = 0;
qtdeImpares = 0;
for i in range (10):
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0:
        qtdePares = qtdePares + 1;
    else:
        qtdeImpares = qtdeImpares + 1;
print (f'Você digitou {qtdePares} números pares e {qtdeImpares} números ímpares')
