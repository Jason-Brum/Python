salarioMinimo = 1412.00
teuSalario = float(input("Digite o valor do seu salário: R$"))

proporcional = teuSalario / salarioMinimo

print (f'Você recebe {proporcional} salários mínimos')

novoSalario = teuSalario * 1.25
correspondente = novoSalario / salarioMinimo

print(f'Seu novo salário é no valor de R${novoSalario}')
print(f'Esse valor corresponde a {correspondente} salários mínimos')