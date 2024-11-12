pessoas = []
while True:
    nome = input("Digite o nome da pessoa: ")
    rg = input("Digite o número do RG: ")
    cpf = input("Digite o número do CPF: ")
    pessoa = (nome, rg, cpf)
    pessoas.append(pessoa)
    if input("Gostaria de cadastrar mais uma pessoa (s/n): ") == "n":
        break
print(pessoas)