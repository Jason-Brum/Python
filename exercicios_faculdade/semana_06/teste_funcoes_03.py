# A criação de uma função em Python sempre segue uma mesma “receita”. Sendo assim, sempre criamos as funções em Python com a palavra-chave def, seguida do nome da função, e os parâmetros entre parênteses () e, no final, dois-pontos. Veja a sintaxe geral de uma função:

#def nomedafuncao(param1, param2, ...):
#(...)
#return resultado

def calcular_area_triangulo(base, altura):
    area = (base * altura)/2
    return area
 
print("A área do triângulo é", calcular_area_triangulo(19, 10))
print("A área do triângulo é", calcular_area_triangulo(10, 3))
print("A área do triângulo é", calcular_area_triangulo(5, 5))
print("A área do triângulo é", calcular_area_triangulo(9, 7))
print("A área do triângulo é", calcular_area_triangulo(20, 14))