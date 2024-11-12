# Programa para cadastro de pessoas com nome, RG e CPF usando tuplas e adicionando em uma lista

# Lista para armazenar os cadastros
cadastros = []

# Função para cadastro de uma pessoa
def cadastrar_pessoa(nome, rg, cpf):
    pessoa = (nome, rg, cpf)  # Armazena os dados da pessoa em uma tupla
    cadastros.append(pessoa)  # Adiciona a tupla na lista de cadastros

# Loop para entrada de dados
while True:
    nome = input("Digite o nome: ")
    rg = input("Digite o RG: ")
    cpf = input("Digite o CPF: ")
    cadastrar_pessoa(nome, rg, cpf)

    continuar = input("Deseja cadastrar outra pessoa? (s/n): ")
    if continuar.lower() != 's':
        break

# Exibindo a lista de cadastros no final do programa
print("\nLista de pessoas cadastradas:")
for pessoa in cadastros:
    print(f"Nome: {pessoa[0]}, RG: {pessoa[1]}, CPF: {pessoa[2]}")
