nomes = ("Ana", "Carlos", "Beatriz", "Daniel")
nomes_ordenados = tuple(sorted(nomes))
print(nomes_ordenados) # saída: ('Ana', 'Beatriz', 'Carlos', 'Daniel')

# Aqui, o funcionamento é igual: temos uma tupla chamada nomes e que possui uma lista de strings que não está ordenada alfabeticamente. Então, usamos a sorted() para ordenar. O resultado da sorted() é uma lista ordenada alfabeticamente. Para converter esta lista de volta em tupla utilizamos o tuple().