primeiro_numero = 1.01

segundo_numero = -2.95

with open("nome.txt", "a") as f:

    f.write("\n" + str(primeiro_numero))

    f.write("\n" + str(segundo_numero))