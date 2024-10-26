maiorNumero = -1000000;
menorNumero = 1000000;
for i in range (5):
    num = int(input("Digite um número inteiro: "))
    if num < menorNumero:
        menorNumero = num
    if num > maiorNumero:
        maiorNumero = num

    print(f'O maior número digitado foi {maiorNumero} e o menor foi {menorNumero}')        


