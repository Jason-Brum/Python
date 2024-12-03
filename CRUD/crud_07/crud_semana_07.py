import json  # Módulo para manipulação de arquivos JSON

# Caminho do arquivo onde os dados serão armazenados
ARQUIVO_ESTUDANTES = "estudantes.json"

# Função para salvar a lista de estudantes no arquivo JSON
def salvarEstudantes(lista):
    try:
        with open(ARQUIVO_ESTUDANTES, "w") as arquivo:
            json.dump(lista, arquivo, indent=4)
        print("Dados salvos com sucesso no arquivo.")
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")

# Função para recuperar a lista de estudantes do arquivo JSON
def recuperarEstudantes():
    try:
        with open(ARQUIVO_ESTUDANTES, "r") as arquivo:
            return json.load(arquivo)  # Retorna a lista de estudantes
    except FileNotFoundError:
        # Se o arquivo não existe, retorna uma lista vazia
        return []
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")
        return []

# Função para incluir um novo estudante
def incluirEstudante():
    try:
        codigo = int(input("Digite o código do estudante (número inteiro): "))
        nome = input("Digite o nome do estudante: ")
        cpf = input("Digite o CPF do estudante: ")

        # Recupera a lista existente
        estudantes = recuperarEstudantes()

        # Adiciona o novo estudante
        estudante = {"codigo": codigo, "nome": nome, "cpf": cpf}
        estudantes.append(estudante)

        # Salva a lista atualizada
        salvarEstudantes(estudantes)

        print(f'Estudante {nome}, incluído com sucesso.')
    except ValueError:
        print("Erro: Código deve ser um número inteiro.")

# Função para listar todos os estudantes
def listarEstudantes():
    print('\n--- Lista de Estudantes ---') 
    # Recupera a lista do arquivo
    estudantes = recuperarEstudantes()

    if estudantes:
        for estudante in estudantes:
            print(f"Código: {estudante['codigo']}, Nome: {estudante['nome']}, CPF: {estudante['cpf']}")
    else:
        print("Nenhum estudante cadastrado.")

# Função para editar um estudante existente
def editarEstudante():
    try:
        codigo = int(input("Digite o código do estudante que deseja editar: "))
        estudantes = recuperarEstudantes()  # Recupera a lista do arquivo

        estudante_encontrado = False
        for estudante in estudantes:
            if estudante['codigo'] == codigo:
                estudante_encontrado = True
                estudante['codigo'] = int(input("Digite o novo código do estudante: "))
                estudante['nome'] = input("Digite o novo nome do estudante: ")
                estudante['cpf'] = input("Digite o novo CPF do estudante: ")

                # Salva a lista atualizada
                salvarEstudantes(estudantes)
                print("Dados do estudante atualizados com sucesso.")
                break

        if not estudante_encontrado:
            print("Estudante não encontrado.")
    except ValueError:
        print("Erro: Código deve ser um número inteiro.")

# Função para excluir um estudante existente
def excluirEstudante():
    try:
        codigo = int(input("Digite o código do estudante que deseja excluir: "))
        estudantes = recuperarEstudantes()  # Recupera a lista do arquivo

        estudante_encontrado = False
        for i, estudante in enumerate(estudantes):
            if estudante['codigo'] == codigo:
                estudante_encontrado = True
                estudantes.pop(i)  # Remove o estudante da lista

                # Salva a lista atualizada
                salvarEstudantes(estudantes)
                print("Estudante excluído com sucesso.")
                break

        if not estudante_encontrado:
            print("Estudante não encontrado.")
    except ValueError:
        print("Erro: Código deve ser um número inteiro.")

# Função para exibir o menu principal
def mostrarMenu():
    print("\n--- MENU PRINCIPAL ---") 
    print("(1) - Gerenciar estudantes.")
    print("(2) - Gerenciar professores.")
    print("(3) - Gerenciar disciplinas.")
    print("(4) - Gerenciar turmas.")
    print("(5) - Gerenciar matérias.")
    print("(9) - Sair.")

# Função para exibir o submenu de operações
def mostrarSubmenu(item): 
    print(f'\n***** [{item.upper()}] MENU DE OPERAÇÕES *****') 
    print("1 - Incluir") 
    print("2 - Listar")
    print("3 - Atualizar")
    print("4 - Excluir")
    print("9 - Voltar ao menu principal")

# Função para gerenciar estudantes
def gerenciarEstudantes():
    while True:
        mostrarSubmenu("Estudantes")
        subOpcao = input("Escolha uma opção do submenu: ")
        if subOpcao == '1':
            incluirEstudante()
        elif subOpcao == '2':
            listarEstudantes()
        elif subOpcao == '3':
            editarEstudante()
        elif subOpcao == '4':
            excluirEstudante()
        elif subOpcao == '9':
            break
        else:
            print("Opção inválida no submenu! Tente novamente.")

# Função principal que controla o menu principal
def main():
    while True: 
        mostrarMenu()
        opcao = input("Escolha uma opção: ") 
        if opcao == '1': 
            print("Você escolheu Gerenciar Estudantes") 
            gerenciarEstudantes()
        elif opcao == '2': 
            print("Você escolheu Gerenciar Professores") 
            print("Funcionalidade em desenvolvimento.")
        elif opcao == '3': 
            print("Você escolheu Gerenciar Disciplinas") 
            print("Funcionalidade em desenvolvimento.")
        elif opcao == '4': 
            print("Você escolheu Gerenciar Turmas") 
            print("Funcionalidade em desenvolvimento.")
        elif opcao == '5': 
            print("Você escolheu Gerenciar Matérias") 
            print("Funcionalidade em desenvolvimento.")
        elif opcao == '9': 
            print("Saindo do programa") 
            break
        else:
            print("Opção inválida! Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    main()
