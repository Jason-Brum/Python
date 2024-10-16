num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
oper = input('Qual operação deseja executar? ( +, -, * ou / )')

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2

if oper == '+':
    print(f"A soma de {num1} com {num2} é de {soma}")
elif oper == "-":
    print(f"A subtração de {num1} por {num2} é de {subtracao}")
elif oper == "*":
    print(f"A multiplicação de {num1} por {num2} é de {multiplicacao}")
elif oper == "/":
    print(f"A divisão de {num1} por {num2} é de {divisao}")    



