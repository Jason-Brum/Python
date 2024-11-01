tupla = ('a', 'b', 'c', 'd', 'e')
subtupla = tupla[1:4]
print(subtupla)  # saída: ('b', 'c', 'd')

# Perceba a segunda linha: a subtupla é criada a partir da indexação dos elementos da tupla original usando o operador de fatiamento (slice). Nesta segunda linha, o operador de slice é utilizado para selecionar uma parte da tupla original. No caso, a subtupla vai conter todos os elementos de índice 1, 2 e 3 da tupla original ('b', 'c', 'd').

# A sintaxe para selecionar um range de elementos em uma tupla é [start:end], onde start é o índice do primeiro elemento a ser incluído na sub-tupla e end é o índice do primeiro elemento a ser excluído da sub-tupla.