idade = input("Qual a sua idade: ")
genero = input("Digite o gênero (M ou F) ")

idade = int(idade)


if (idade > 63 and genero == 'F'):
    print("Você pode se aposentar")
elif (idade > 68 and genero =='M'):
    print("Você já pode se aposentar")  
else:
    print("Você ainda não pode se aposentar")    