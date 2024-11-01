numeros = [3, 1, 4, 2, 5]
numeros.sort()
print(numeros)

# O código acima cria uma lista de números chamada numeros com os valores 3, 1, 4, 2 e 5. Em seguida, a função sort() é usada para ordenar a lista em ordem crescente. Dessa forma, o código irá mostrar na tela a lista ordenada em ordem crescente, que no caso é: [1, 2, 3, 4, 5].

# Se quiséssemos ordená-la de forma decrescente bastaria trocar a segunda linha para numeros.sort(reverse=True). Assim, ela iria mostrar na tela os valores na ordem decrescente ([5, 4, 3, 2, 1]).

numeros = [3, 1, 4, 2, 5]
numeros.sort(reverse=True)
print(numeros)

frutas = ['banana', 'maçã', 'goiaba', 'pera', 'pêssego', 'figo']
print(frutas) # imprime toda a lista
print(frutas[0]) # imprime banana
print(frutas[2]) #imprime goiaba
frutas.sort()
print(frutas) # imprime a lista em ordem alfabética

frutas = ['banana', 'maçã', 'goiaba', 'pera', 'pêssego', 'figo']
frutas.sort(reverse=True) # imprime a lista ao contrário da ordem alfabética
print(frutas)

lista = [1, 2, 3, 4, 5]
lista[2] = 10 # modifica o item 2 dentro da lista
print(lista)


