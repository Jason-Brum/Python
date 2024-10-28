#Dada uma lista A com 10 elementos de inteiros, observe a seguinte lei de formação: quando o índice de A for par multiplicar o elemento por 2 do contrário calcular o seu quadrado. Imprimir a lista A modificada.

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range (len(A)):
    if(i % 2 == 0):
        A[i] = A[i] *2
    else:
        A[i]= A[i]*A[i]

for i in range(len(A)):
    print(A[i])
        