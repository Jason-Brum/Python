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