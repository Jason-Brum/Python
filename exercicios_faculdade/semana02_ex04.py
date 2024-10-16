salario = float(input('Qual o valor do seu salário? '))

if salario < 5000:
    abono = salario * 0.15
else:
    abono = salario * 0.10


print(f"O Valor do seu abono de fim de ano é de: R${abono:.2f}")