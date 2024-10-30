#Exemplo de aplicação 6: Solicite ao usuário que digite três coordenadas (x, y), armazenando-as em uma matriz bidimensional.

coordenadas = []
for i in range(3):
    x = int(input("Insira um valor de x: "))
    y = int(input("Insira um valor de y: "))
    coordenadas.append([x, y])
print(coordenadas)

#Entenda uma matriz em Python como sendo uma lista de listas.
