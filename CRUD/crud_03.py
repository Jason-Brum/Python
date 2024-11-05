estudantes = [] #lista vazia que armazena os nomes dos estudantes

def mostrarMenu(): #função para definição do menu principal
    print("\n--- MENU PRINCIPAL ---") #da linha 4 deste código até à linha 10 são comandos "print", para mostrar na tela as mensagens literais digitadas.
    print("(1) - Gerenciar estudantes.")
    print("(2) - Gerenciar professores.")
    print("(3) - Gerenciar disciplinas.")
    print("(4) - Gerenciar turmas.")
    print("(5) - Gerenciar matérias.")
    print("(9) - Sair.")

def mostrarSubmenu(item): #Dunção para o submenu. O parâmetro anterior estava vazio, agora nomeei como "item" para ser usado em cada um dos submenus, sem precisar repetir tudo
    print(f'\n***** [{item.upper()}] MENU DE OPERAÇÕES *****') #Exibe a opção escolhida em letras maiúsculas
    print("1 - Incluir") #linha 14 a linha 18, mostra na tela as mensagens
    print("2 - Listar")
    print("3 - Atualizar")
    print("4 - Excluir")
    print("9 - Voltar ao menu principal")

def executarSubmenu(item): #função de execuação do submenu criada anteriormente.
    global estudantes #serve para recorrer a uma variável global, fora deste escopo local, no caso "estudantes", criada no início do programa

    while True: #laço principal que é executado até que o usuário escolha sair
        mostrarSubmenu(item) #chama a função de mostrar o submenu passando "item" como argumento, ou seja, mostra o menu de operações (incluir, listar, atualizar e excluir) para o item "ESTUDANTES", por exemplo
        subOpcao = input("Escolha uma opção do submenu: ") #comando para o usuário escolher uma opção do submenu.

        if item == "Estudantes": #condicional para escolha de "estudantes"
            if subOpcao == '1': #condicional para opção incluir
                nome = input("Digite o nome do estudante: ")
                estudantes.append(nome) #append é um método de inclusão na lista, neste caso inclui o nome do estudante dentro da variável estudante
                print(f'Estudante {nome}, incluído com sucesso.') #imprime uma string literal, concatenada com a variável nome digitada pelo usuário
            elif subOpcao == '2': #condicional para listar os estudantes
                print('\n Lista de Estudantes: ') #título para a lista de estudantes que será exibida.
                if estudantes: 
                    for i, estudante in enumerate(estudantes, start=1): #indica que cada posição da lista estudante(i) será numerada, começando pelo número 1
                        print(f'{i}.{estudante}') #mostra na tela os números e os nomes dos estudantes 
                else:
                    print("Nenhum estudante cadastrado.") #mostra essa msg na tela quando não foi cadastrado ainda nenhum estudante
            elif subOpcao in ['3', '4']: #condicional para as opções 3 e 4 do submenu que ainda não foram desenvolvidas
                print("Funcionalidade em desenvolvimento")
                break #para a execução e retorna ao menu prinipal
            else:
                print("Esse é uma opção inválida no submenu! Tente novamente") #condicional para qualquer coisa que o usuário digitar que não seja nenhuma das opções indicadas
        else:
            print("Funcionalidade em desenvolvimento") #mostra na tela esta msg caso o usuário tenha escolhido as opções que ainda estão sendo criadas
            break #para a execução e retorna


while True: #laço principal que é executado até que o usuário escolha sair//enquanto verdadeiro, FAÇA!
    mostrarMenu()#chama novamente a função criada no início do programa
    opcao = input("Escolha uma opção: ") #função para que o usuário escolha uma das opções do menu

    if opcao == '1': #condicional para a opção 1(estudantes)
        print("Você escolheu Gerenciar Estudantes") #mostra essa msg na tela
        executarSubmenu("Estudantes") #executa o submenu para estudantes, ou seja, incluir, listar, atualizar e excluir.
    elif opcao == '2': #condicional para a opção 2(profgessores)
        print("Você escolheu Gerenciar Professores") #mostra essa msg na tela
        executarSubmenu("Professores")#executa o submenu para professores, ou seja, incluir, listar, atualizar e excluir.
    elif opcao == '3': #condicional para a opção3 (disciplinas)
        print("Você escolheu Gerenciar Disciplinas") #mostra essa msg na tela
        executarSubmenu("Disciplinas")   #executa o submenu para disciplinas, ou seja, incluir, listar, atualizar e excluir.
    elif opcao == '4': #condicional para a opção 4(turmas)
        print("Você escolheu Gerenciar Turmas")  #mostra essa msg na tela
        executarSubmenu("Turmas")   #executa o submenu para turmas, ou seja, incluir, listar, atualizar e excluir.
    elif opcao == '5': #condicional para a opção 5(matérias)
        print("Você escolheu Gerenciar Matérias") #mostra essa msg na tela
        executarSubmenu("Matérias")  #executa o submenu para estudantes, ou seja, incluir, listar, atualizar e excluir.
    elif opcao == '9':   #condicional para a opção 9(sair)
        print("Saindo do programa")  #mostra essa msg na tela
        break #para e sai do programa
    else:
        print("Opção inválida! Tente novamente") #msg caso o usuário escolha qualquer outra opção 







