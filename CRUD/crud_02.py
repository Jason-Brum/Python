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

def executarSubmenu(item): #função para executar o submenu com o parâmetro "item" para indicar qual é a operaç~]ao
    mostrarSubmenu(item) #mostra o submenu antes da escolha do usuário
    subOpcao = input("Escolha uma opção no submenu abaixo: ")
    if subOpcao == '1':
        print(f'Você escolheu INCLUIR em {item}')
    elif subOpcao == '2':
        print(f'Você escolheu LISTAR em {item}')   
    elif subOpcao == '3':
        print(f'Você escolheu ATUALIZAR em {item}')
    elif subOpcao == '4':
        print(f'Você escolheu EXCLUIR em {item}')
    elif subOpcao == '9':
        print("Você escolheu voltar ao menu principal.")

    else:
        print("Opção inválida no submenu! Tente novamente.")


while True: #laço principal que é executado até que o usuário escolha sair
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
