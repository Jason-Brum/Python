opcao = ''
while opcao != 's':
    print("MENU:")
    print("a. Opção 1")
    print("b. Opção 2")
    print("c. Opção 3")
    print("s. Sair")
    opcao = input("Digite uma opção: ")
    if opcao == 'a':
        print("Opção 1 selecionada")
    elif opcao == 'b':
        print("Opção 2 selecionada")
    elif opcao == 'c':
        print("Opção 3 selecionada")
    elif opcao == 's':
        print("Saindo...")
    else:
        print("Opção inválida.")

    #    Este código mostra um menu para o usuário e permite que ele selecione uma opção digitando a letra correspondente à opção. O programa entra em um loop enquanto o usuário não digita a opção "s" (sair). Em cada iteração do loop, o programa imprime o menu e solicita ao usuário que digite uma opção. Depois disso, o programa verifica qual opção foi selecionada pelo usuário e executa a ação correspondente. Se o usuário selecionar a opção "s", o programa encerra o loop e imprime a mensagem “Saindo…”. Se o usuário selecionar uma opção inválida, o programa imprime a mensagem “Opção inválida.” e retorna ao início do loop para apresentar o menu novamente e aguardar uma nova seleção do usuário.