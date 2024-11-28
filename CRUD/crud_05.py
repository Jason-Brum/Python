estudantes = []

def mostrar_menu_principal():
    """Apresenta o menu principal."""
    print("\n--- MENU PRINCIPAL ---")
    print("(1) - Gerenciar estudantes.")
    print("(2) - Gerenciar professores.")
    print("(3) - Gerenciar disciplinas.")
    print("(4) - Gerenciar turmas.")
    print("(5) - Gerenciar matérias.")
    print("(9) - Sair.")

def mostrar_menu_operacoes(item):
    """Apresenta o menu de operações para o item selecionado."""
    print(f'\n***** [{item.upper()}] MENU DE OPERAÇÕES *****')
    print("1 - Incluir")
    print("2 - Listar")
    print("3 - Atualizar")
    print("4 - Excluir")
    print("9 - Voltar ao menu principal")

def incluir_estudante():
    """Permite incluir um novo estudante na lista."""
    codigo = int(input("Digite o código do estudante: "))
    nome = input("Digite o nome do estudante: ")
    cpf = input("Digite o CPF do estudante: ")
    estudante = {
        "codigo": codigo,
        "nome": nome,
        "cpf": cpf
    }
    estudantes.append(estudante)
    print(f'Estudante {nome}, incluído com sucesso.')

def listar_estudantes():
    """Exibe a lista de estudantes cadastrados."""
    print('\nLista de Estudantes:')
    if estudantes:
        for estudante in estudantes:
            print(f"Código: {estudante['codigo']}, Nome: {estudante['nome']}, CPF: {estudante['cpf']}")
    else:
        print("Nenhum estudante cadastrado.")

def editar_estudante():
    """Permite editar os dados de um estudante."""
    codigo = int(input("Digite o código do estudante que deseja editar: "))
    estudante_encontrado = False
    for estudante in estudantes:
        if estudante['codigo'] == codigo:
            estudante_encontrado = True
            estudante['codigo'] = int(input("Digite o novo código do estudante: "))
            estudante['nome'] = input("Digite o novo nome do estudante: ")
            estudante['cpf'] = input("Digite o novo CPF do estudante: ")
            print("Dados do estudante atualizados com sucesso.")
            break
    if not estudante_encontrado:
        print("Estudante não encontrado.")

def excluir_estudante():
    """Permite excluir um estudante da lista."""
    codigo = int(input("Digite o código do estudante que deseja excluir: "))
    estudante_encontrado = False
    for i, estudante in enumerate(estudantes):
        if estudante['codigo'] == codigo:
            estudante_encontrado = True
            estudantes.pop(i)
            print("Estudante excluído com sucesso.")
            break
    if not estudante_encontrado:
        print("Estudante não encontrado.")

def executar_submenu(item):
    """Executa o submenu correspondente ao item selecionado."""
    while True:
        mostrar_menu_operacoes(item)
        sub_opcao = input("Escolha uma opção do submenu: ")

        if item == "Estudantes":
            if sub_opcao == '1':
                incluir_estudante()
            elif sub_opcao == '2':
                listar_estudantes()
            elif sub_opcao == '3':
                editar_estudante()
            elif sub_opcao == '4':
                excluir_estudante()
            elif sub_opcao == '9':
                break
            else:
                print("Opção inválida no submenu! Tente novamente.")
        else:
            print("Funcionalidade em desenvolvimento")
            break

# Programa principal
while True:
    mostrar_menu_principal()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        print("Você escolheu Gerenciar Estudantes")
        executar_submenu("Estudantes")
    elif opcao == '2':
        print("Você escolheu Gerenciar Professores")
        executar_submenu("Professores")
    elif opcao == '3':
        print("Você escolheu Gerenciar Disciplinas")
        executar_submenu("Disciplinas")
    elif opcao == '4':
        print("Você escolheu Gerenciar Turmas")
    elif opcao == '5':
        print("Você escolheu Gerenciar Matérias")
    elif opcao == '9':
        print("Saindo do programa")
        break
    else:
        print("Opção inválida! Tente novamente.")





