num1 = input("Digite um número: ")
num2 = input("Digite outro número: ")
num3 = input("Digite o terceiro número: ")

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

if (num1 > num2 and num1 > num3):
    print("O primeiro núemero digitado é o maior")
elif (num2 > num1 and num2 > num3):
    print("O maior número digitado foi o segundo")   
else:
    print("O maior número digitado foi o terceiro")    