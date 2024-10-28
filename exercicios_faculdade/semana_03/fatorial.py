#Crie um algoritmo para calcular o fatorial de um número usando o for.Exemplo: um usuário digita 5. O algoritmo deve retornar 120 (5!=5∗4∗3∗2∗1=120).


num = int(input("Digite um número: "))

fatorial = 1
for i in range(1, num+1):
    fatorial *= i

print("O fatorial de", num, "é", fatorial)