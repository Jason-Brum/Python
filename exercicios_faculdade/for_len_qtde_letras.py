# percorra uma lista de nomes de animais e mostre apenas os que tem menos de 7 letras

lista = ["gato", "girafa", "cachorro", "galo", "hipopótamo", "boi", "coelho", "elefante"]

for animal in lista:
    tamanho = len(animal)
    if tamanho < 7:
        print(animal)

  