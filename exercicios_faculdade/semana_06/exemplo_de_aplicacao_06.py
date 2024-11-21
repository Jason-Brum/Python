def maior_menor(*numeros):

 """
Recebe uma lista aleatória de números e calcula o maior e o menor deles
:param numeros: lista de números a ser analisados
:return: retorna o maior e o menor número da lista
"""

    maior = -1000000
    menor = 1000000
    for numero in numeros:
        if numero > maior:
        maior = numero
        if numero < menor:
        menor = numero

    return maior, menor