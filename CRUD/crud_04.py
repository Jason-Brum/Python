estudantes = [] 

def mostrarMenu():
    print("\n--- MENU PRINCIPAL ---") 
    print("(1) - Gerenciar estudantes.")
    print("(2) - Gerenciar professores.")
    print("(3) - Gerenciar disciplinas.")
    print("(4) - Gerenciar turmas.")
    print("(5) - Gerenciar matérias.")
    print("(9) - Sair.")

def mostrarSubmenu(item): 
    print(f'\n***** [{item.upper()}] MENU DE OPERAÇÕES *****') 
    print("1 - Incluir") 
    print("2 - Listar")
    print("3 - Atualizar")
    print("4 - Excluir")
    print("9 - Voltar ao menu principal")

def executarSubmenu(item):
    global estudantes 
    while True: 
        mostrarSubmenu(item) 
        subOpcao = input("Escolha uma opção do submenu: ") 

        if item == "Estudantes": 
            if subOpcao == '1': 
                codigo = int(input("Digite o código do estudante: "))
                nome = input("Digite o nome do estudante: ")
                cpf = input("Digite o CPF do estudante: ")
                estudante = {
                    "codigo": codigo, 
                    "nome": nome, 
                    "cpf": cpf} #dicionário com nome estudante que vai armazenar 3 dados: código, nome e CPF.
                estudantes.append(estudante) 
                print(f'Estudante {nome}, incluído com sucesso.') 
            elif subOpcao == '2': 
                print('\n Lista de Estudantes: ') 
                if estudantes: 
                    for estudante in estudantes:
                        print(f"Código: {estudante['codigo']}, Nome: {estudante['nome']}, CPF: {estudante['cpf']}") 
                else:
                    print("Nenhum estudante cadastrado.")
            elif subOpcao == '3':
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
            
            elif subOpcao == '4':  
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

            elif subOpcao == '9':  
                break
            else:
                print("Opção inválida no submenu! Tente novamente.")
        else:
            print("Funcionalidade em desenvolvimento")
            break
    
while True: 
    mostrarMenu()
    opcao = input("Escolha uma opção: ") 

    if opcao == '1': 
        print("Você escolheu Gerenciar Estudantes") 
        executarSubmenu("Estudantes") 
    elif opcao == '2': 
        print("Você escolheu Gerenciar Professores") 
        executarSubmenu("Professores")
    elif opcao == '3': 
        print("Você escolheu Gerenciar Disciplinas") 
        executarSubmenu("Disciplinas")   
    elif opcao == '4':
        print("Você escolheu Gerenciar Turmas") 
    elif opcao == '5':
        print("Você escolheu Gerenciar Matérias") 
    elif opcao == '9':   
        print("Saindo do programa") 
        break 
    else:
        print("Opção inválida! Tente novamente") 







