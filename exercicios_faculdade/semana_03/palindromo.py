#Escreva um algoritmo para verificar se uma palavra é um palíndromo usando o while.Exemplo: radar é um palíndromo (se ler a palavra de trás para frente resultará na mesma palavra). banana não é um palíndromo.


palavra = input("Digite uma palavra: ")
i = 0
j = len(palavra) - 1
palindromo = True

while i < j:
    if palavra[i] != palavra[j]:
        palindromo = False
        break
    i += 1
    j -= 1

if palindromo:
    print(palavra, "é um palíndromo")
else:
    print(palavra, "não é um palíndromo")