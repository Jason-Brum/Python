estudantes = []

def mostrarMenu(): #função que definiu o menu principal
    print("\n--- MENU PRINCIPAL ---")
    print("(1) - Gerenciar estudantes.")
    print("(2) - Gerenciar professores.")
    print("(3) - Gerenciar disciplinas.")
    print("(4) - Gerenciar turmas.")
    print("(5) - Gerenciar matérias.")
    print("(9) - Sair.")

def mostrarSubmenu(item): #Dunção para o submenu. o parâmetro anterior estava vazio, agora nomeei como "item" para ser usado em cada um dos submenus, sem precisar repetir tudo
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
                nome = input("Digite o nome do estudante: ")
                estudantes.append(nome)
                print(f'Estudante {nome}, incluído com sucesso.')
            elif subOpcao == '2':
                print('\n Lista de Estudantes: ')
                if estudantes: 
                    for i, estudante in enumerate(estudantes, start=1):
                        print(f'{i}.{estudante}')
                else:
                    print("Nenhum estudante cadastrado.") 
            elif subOpcao in ['3', '4']:
                print("Funcionalidade em desenvolvimento")
                break
            else:
                print("Esse é uma opção inválida no submenu! Tente novamente")
        else:
            print("Funcionalidade em desenvolvimento")
            break


while True: #laço principal que é executado até que o usuário escolha sair//enquanto verdadeiro, FAÇA!
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
        executarSubmenu("Turmas")   
    elif opcao == '5':
        print("Você escolheu Gerenciar Matérias") 
        executarSubmenu("Matérias")  
    elif opcao == '9':   
        print("Saindo do programa")  
        break
    else:
        print("Opção inválida! Tente novamente")






#PRÓXIMOS PASSOS A PARTIR DA SEMANA 4
#  Desenvolva as funcionalidades de incluir e listar estudantes
    # apenas o nome do estudante deve ser perguntado ao usuário
    # os nomes dos estudantes devem ser armazenados em uma lista
    # caso o usuário escolha professores, disciplinas, turmas ou matérias, o sistema deve mostrar a mensagem "em desenvolvimento" - Ou seja, só vai funcionar para estudantes.
    # caso o usuário escolha as opções atualizar ou excluir no menu de operações do estudante o sistema deve mostrar a msg "em desenvolvimento" e mostrar novamente o menu de operações
