frutas = ['banana', 'maçã', 'goiaba']

#outrasFrutas = list() - Esta sintaxe também é aceita para criar uma lista.
#dentro da mesma lista pode ter diversos valores distintos como string, boolean, números inteiros e reais.

for i in range(3):
    nova_fruta = input("Digite o nome de outra fruta: ")
    frutas.append(nova_fruta)

print(frutas)