nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
faltas = int(input("Digite sua quantidade de faltas: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7 and faltas <= 10:
    print("Você está APROVADO")

elif media >= 7 and faltas > 10:
    print("Você está REPROVADO por faltas.")

else 
    print("Você está REPROVADO, pois não atingiu a média mínima.")



print(f"A média do estudante é: {media:.2f}")