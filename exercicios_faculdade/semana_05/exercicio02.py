def cadastrar_funcionario():
    # Dicionário para armazenar dados dos funcionários
    funcionarios = {}

    while True:
        # Coleta de dados do funcionário
        matricula = input("Digite a matrícula do funcionário: ")
        nome = input("Digite o nome do funcionário: ")

        # Tupla para armazenar dependentes
        dependentes = ()

        # Adiciona dependentes dinamicamente
        while True:
            dependente = input("Digite o nome do dependente (ou deixe em branco para finalizar): ")
            if dependente == "":
                break
            dependentes += (dependente,)  # Adiciona o dependente à tupla

        # Armazena os dados do funcionário no dicionário
        funcionarios[matricula] = {'Nome': nome, 'Dependentes': dependentes}

        # Pergunta se deseja cadastrar outro funcionário
        continuar = input("Deseja cadastrar outro funcionário? (s/n): ")
        if continuar.lower() != 's':
            break

    # Exibe todos os funcionários e seus dependentes cadastrados
    print("\nFuncionários cadastrados:")
    for matricula, dados in funcionarios.items():
        print(f"Matrícula: {matricula}, Nome: {dados['Nome']}, Dependentes: {', '.join(dados['Dependentes']) if dados['Dependentes'] else 'Nenhum'}")

# Executa o cadastro de funcionários
cadastrar_funcionario()
