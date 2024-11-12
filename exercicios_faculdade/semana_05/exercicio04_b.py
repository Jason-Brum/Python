produtos = {}
while True:
    nome = input("Digite o nome do produto: ")
    valor = float(input("Digite o valor do produto: "))
    if nome in produtos:
        if input(f"Produto já cadastrado com o valor {produtos[nome]}. Deseja alterar o valor? (s/n)") == "n":
            continue
    produtos[nome] = valor
    if input("Cadastrar um novo produto? (s/n)") == "n":
        break
for produto in produtos:
    print(f"{produto:>20}: R${produtos[produto]:.2f}")