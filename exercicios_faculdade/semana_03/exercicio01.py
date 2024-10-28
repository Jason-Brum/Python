#Crie um algoritmo que pede ao usuário para que digite um número inicial e um número final. Em seguida, ele mostrará todos os números pares neste intervalo usando for.Exemplo: um usuário digita os números 1 e 10. O algoritmo deve retornar várias mensagens falando que os números 2, 4, 6, 8 e 10 são pares.

inicio = int(input("Insira um número para começar a contagem: "))
fim = int(input("Insira um número para terminar a contagem: "))

for num in range(inicio, fim+1):
    if num % 2 == 0:
        print(num, "é um número par")



        