funcionarios = []
while True:
    nome = input("Digite o nome do funcionário: ")
    matricula = input("Digite a matrícula do funcionário: ")
    dependentes = tuple()
    while True:
        dependente = input("Digite o nome do dependente (0 para sair): ")
        if dependente == "0":
            break
        dependentes += (dependente,)
    funcionario = (nome, matricula, dependentes)
    funcionarios.append(funcionario)
    if input("Gostaria de cadastrar mais um funcionário (s/n): ") == "n":
        break
print(funcionarios)