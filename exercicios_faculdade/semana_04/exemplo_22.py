# TUPLAS. São utilizados parênteses e seus elementos não podem ser modificados
# Listas. São utilizados colchetes e seus elementos são mutáveis
# Em uma lista, os elementos são armazenados em uma estrutura mutável, ou seja, é possível adicionar, remover e alterar elementos depois que a lista é criada. Já em uma tupla, os elementos são armazenados em uma estrutura imutável, ou seja, uma vez criada, a tupla não pode ser alterada.

coordenadas = (40.7128, -74.0060)
dias_da_semana = ("segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo")
pontuacao_jogo = (1200, 3)

animais = ("gato", "cachorro", "papagaio", "peixe")

for animal in animais:
    print(animal)

carros = ("fusca", "fiesta", "oggi", "uno")

if "fusca" in carros:
    print("O fusca está na lista")
else:
    print("O fusca não está na lista")