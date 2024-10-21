idade = int(input("Qual é a sua idade? "))

if idade >= 21:
    print("Você pode beber nos Estados Unidos, basta apresentar seu RG.")

elif idade >= 18:
    print("Você é maior de idade, mas ainda NÃO pode beber nos EUA")

else:
    print("Você é menor de idade.")