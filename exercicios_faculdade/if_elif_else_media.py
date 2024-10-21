nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

media = (nota1 + nota2)/2

if media >= 7.0:
    print(f'Parabéns, sua média é {media} e você está APROVADO')
elif media >= 5.0:
    print(f'Sua média foi de {media} e você está de RECUPERAÇÃO')
else:
    print(f'Sua média foi de {media} e você foi REPROVADO')    