num = int(input("Digite um número ou digite 0 para sair: "))
while num != 0:
    if num > 0:
        print("O número é positivo")
    else:
        print("O número é negativo")
    num = int(input("Digite outro número (digite 0 para sair): "))

    #laço infinito até o usuário digitar 0 e sair do programa