def exibir_menu():
    """
    Exibe o menu principal com as opções disponíveis.
    """
    print("\n--- AGENDA TELEFÔNICA ---")
    print("1. Inserir contato")
    print("2. Remover contato")
    print("3. Sair")

def inserir_contato(agenda):
    """
    Insere um novo contato na agenda.

    Parâmetros:
        agenda (dict): Dicionário que armazena os contatos.

    Retorno:
        None
    """
    nome = input("Digite o nome do contato: ").strip()
    if nome in agenda:
        print("Contato já existe na agenda!")
        return

    telefone = input("Digite o número de telefone: ").strip()
    agenda[nome] = telefone
    print(f"Contato '{nome}' adicionado com sucesso!")

def remover_contato(agenda):
    """
    Remove um contato da agenda.

    Parâmetros:
        agenda (dict): Dicionário que armazena os contatos.

    Retorno:
        None
    """
    nome = input("Digite o nome do contato a ser removido: ").strip()
    if nome in agenda:
        del agenda[nome]
        print(f"Contato '{nome}' removido com sucesso!")
    else:
        print("Contato não encontrado.")

def main():
    """
    Função principal que gerencia a execução do programa.
    """
    agenda = {}
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            inserir_contato(agenda)
        elif opcao == "2":
            remover_contato(agenda)
        elif opcao == "3":
            print("Saindo da agenda... Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Execução do programa
if __name__ == "__main__":
    main()
