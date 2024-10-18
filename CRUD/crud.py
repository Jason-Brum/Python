def mostrar_menu():
    print("\n--- MENU PRINCIPAL ---")
    print("(1) - Gerenciar estudantes.")
    print("(2) - Gerenciar professores.")
    print("(3) - Gerenciar disciplinas.")
    print("(4) - Gerenciar turmas.")
    print("(5) - Gerenciar disciplinas.")
    print("(9) - Sair.")

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        print("Você escolheu a Opção 1")
    elif opcao == '2':
        print("Você escolheu a Opção 2")
    elif opcao == '3':
        print("Você escolheu a Opção 3")
    elif opcao == '4':
        print("Saindo do programa...")
        break  # Encerra o loop e sai do programa
    else:
        print("Opção inválida! Tente novamente.")