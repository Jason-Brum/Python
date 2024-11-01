# Aqui, temos uma tupla chamada tupla1 com três elementos. Para adicionar o número 4 dentro desta tupla tivemos que criar uma nova tupla chamada tupla2, que é formada pela concatenação (veja o símbolo +) da tupla1 com uma nova tupla contendo apenas o número 4.

tupla1 = (1, 2, 3)
tupla2 = tupla1 + (4,)
print(tupla2)  # saída: (1, 2, 3, 4)

#A adição da vírgula depois do número 4 é importante para indicar que se trata de uma tupla de um único elemento. Caso contrário, o Python entenderia apenas como um inteiro comum e a operação de concatenação com a tupla1 não seria possível. Agora, e se fosse para remover? Teríamos que fazer algo como:

tupla1 = (10, 20, 30, 40, 50)
tupla2 = (tupla1[0], tupla1[2], tupla1[4])
print(tupla2)  # saída: (10, 30, 50)

# Aqui, ordenamos uma tupla chamada numeros com o uso da função sorted(), que já vimos antes. Só que temos um problema: o resultado dessa sorted() não retorna uma tupla, mas sim uma lista. Então, usamos a função tuple() para converter uma lista em tuplas. Epa, pera: