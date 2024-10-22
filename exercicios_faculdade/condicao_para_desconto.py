num1 = input("Qual o valor dessa camisa? ")

num1 = float(num1)
desconto = num1 * 0.9

if (num1 > 100.00):
    print(f'O preço com desconto é: {desconto}')
else:
    print(f'O preço da camisa é {num1}')    