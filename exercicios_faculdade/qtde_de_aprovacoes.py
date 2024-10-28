 #Construa um programa que receba a nota de 20 alunos e armazene estasnotas em uma lista. Calcule e imprima:• a média da classe;• a quantidade de alunos aprovados, isto é, com média >=7;• a quantidade de alunos reprovados, isto é, com média <7.


turma = 5
soma = 0
media = 0
aprovados = 0
reprovados = 0
notas = []

for i in range (turma):
    nota = float(input ("Digite a nota: "))
    notas.append(nota)
    if (notas[i] >= 7):
        aprovados = aprovados + 1
    elif (notas[i] < 7):
        reprovados = reprovados + 1

for i in range (turma): 
    soma = soma + notas[i]

mediaTurma = soma / turma

print (f'A média da turma é {mediaTurma}')
print (f'O total de aprovados é: {aprovados}')
print (f'O total de reprovados é {reprovados}')