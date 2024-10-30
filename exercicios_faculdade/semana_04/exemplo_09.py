m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(m[2][1])      # isto mostrará o número inteiro "8". Os números desta linha indicam os indices dos vetores e das matrizes

print("-------")

#Entenda uma matriz em Python como sendo uma lista de listas.

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(nums))      # isto mostrará o valor "10" - Len conta quantos elementos têm na lista

print("-------")

nome = "Python"
print(len(nome))    # isto mostrará o valor "6". A função len também é muito usada para saber quantos caracteres possui uma string.
print("-------")

nums = [17, 33, 8, 11, 8, 15, 9]
print(max(nums))        # isto mostrará o valor "33". A função max retorna o maior valor dentro de uma lista.
print("-------")

herois = ["Zorro", "Capitão América", "Hulk", "Super-Homem"]
print(max(herois))       # isto mostrará o valor "Zorro". Caso os elementos da lista sejam strings, a comparação é feita tomando por base a ordem alfabética.
print("-------")

nums = [17, 33, 8, 11, 8, 15, 9]
print(min(nums))      # isto mostrará o valor "8". A função min retorna o menor valor dentro de uma lista.
print("-------")

herois = ["Zorro", "Capitão América", "Hulk", "Super-Homem"]
print(min(herois))     # isto mostrará o valor "Capitão América". Da mesma forma que a função max, caso os elementos da lista sejam strings, a função min efetua a comparação tomando por base a ordem alfabética.
print("-------")

nums = [17, 33, 8, 11, 8, 15, 9]
print(sorted(nums))      # isto resultará em [8, 8, 9, 11, 15, 17, 33]. A função sorted retorna a lista passada em ordem crescente.
print("-------")

nums = [17, 33, 8, 11, 8, 15, 9]
print(sorted(nums, reverse=True))      # isto resultará em [33, 17, 15, 11, 9, 8, 8]. Também é possível fazer a ordenação em ordem decrescente, por meio do parâmetro reverse.
print("-------")

nome = "José dos Santos"
print(sorted(nome))
# isto resultará em [' ', ' ', 'J', 'S', 'a', 'd', 'n', 'o', 'o', 'o', 's', 's', 's', 't', 'é']. Ainda, pode-se aplicar a função sorted sobre uma string, retornando uma lista não editável, no caso, uma tupla, como será visto na próxima unidade.
print("-------")

nums = [17, 33, 8, 11, 8, 15, 9]
print(sum(nums))       # isto resultará em "101". A função sum retorna a soma de todos os elementos de uma lista.






