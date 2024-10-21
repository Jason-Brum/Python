nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

if nota1 >= 7:
    if nota2 >= 7:
        if nota3 >= 7:
            print("Parabéns, você foi aprovado(a)!")
        else:
            print("Sua nota na terceira avaliação foi abaixo da média.")
    else:
        print("Sua nota na segunda avaliação foi abaixo da média.")
else:
    print("Sua nota na primeira avaliação foi abaixo da média.")