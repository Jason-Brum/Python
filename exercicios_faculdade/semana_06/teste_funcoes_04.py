def quadrado(numero):
    resultado = numero ** 2
    return resultado

for i in range(21):

    print(f"{i} * {i} = {quadrado(i)}")