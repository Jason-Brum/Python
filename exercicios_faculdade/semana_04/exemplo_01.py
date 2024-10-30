#Exemplo de aplicação 1: Elabore um programa que solicite ao usuário cinco números, armazene-os em uma lista e exiba como resultado os dados obtidos.

nums = [0, 0, 0, 0, 0]
for i in range(5):
    num = int(input("Digite um número: "))
    nums[i] = num
print(nums)