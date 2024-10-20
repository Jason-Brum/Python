def mostrar_menu():
    print("\n--- MENU PRINCIPAL ---")
    print("(1) - Gerenciar estudantes.")
    print("(2) - Gerenciar professores.")
    print("(3) - Gerenciar disciplinas.")
    print("(4) - Gerenciar turmas.")
    print("(5) - Gerenciar disciplinas.")
    print("(9) - Sair.")

def mostrar_submenu():
    print("\n***** [PROFESSORES] MENU DE OPERAÇÕES *****")
    print("1 - Incluir")
    print("2 - Listar")
    print("3 - Atualizar")
    print("4 - Excluir")
    print("9 - Voltar ao menu principal")

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        print("Você escolheu a Opção 1")
    elif opcao == '2':
        while True:
            mostrar_submenu()  
            sub_opcao = input("Escolha uma opção do submenu: ")

            if sub_opcao == '1':
                print("Você escolheu 'Incluir'")
            elif sub_opcao == '2':
                print("Você escolheu 'Listar'")
            elif sub_opcao == '3':
                print("Você escolheu 'Atualizar'")
            elif sub_opcao == '4':
                print("Você escolheu 'Excluir'")
            elif sub_opcao == '9':
                print("Voltando ao menu principal...")
                break 
            else:
                print("Opção inválida no submenu! Tente novamente.")
    elif opcao == '3':
        print("Você escolheu a Opção 3")
    elif opcao == '4':
        print("Você escolheu a Opção 4") 
    elif opcao == '3':
        print("Você escolheu a Opção 5")       
    elif opcao == '9':
        print("Saindo do programa...")
        break  
    else:
        print("Opção inválida! Tente novamente.")