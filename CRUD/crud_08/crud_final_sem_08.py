import json  #Importa o módulo JSON para manipulação de arquivos no formato JSON

# Caminhos dos arquivos para armazenar dados de cada parte do sistema
ARQUIVOS = {
    "estudantes": "estudantes.json",
    "professores": "professores.json",
    "disciplinas": "disciplinas.json",
    "turmas": "turmas.json",
    "matriculas": "matriculas.json"
}

# Função para salvar dados em um arquivo JSON
def salvarDados(tipo, lista):
    try:
        #Abre o arquivo correspondente ao tipo (ex.: estudantes.jason) em modo de escrita
        with open(ARQUIVOS[tipo], "w") as arquivo:
            #Salva a lista no arquivo JSON com indentação para fácil leitura
            json.dump(lista, arquivo, indent=4)    
        print(f"Dados de {tipo} salvos com sucesso.")
    except Exception as e:
        #Captura e exibe qualquer erro ocorrido ao salvar os dados
        print(f"Erro ao salvar dados de {tipo}: {e}")

#Função para recuperar dados de arquivo JSON
def recuperarDados(tipo):
    try:
        #Abre o arquivo correspondente ao tipo em modo de leitura
        with open(ARQUIVOS[tipo], "r") as arquivo:
            #Retorna os dados carregados do arquivo
            return json.load(arquivo)
    except FileNotFoundError:
        #Caso o arquivo não exista, retorna uma lista vazia
        return []
    except Exception as e:
        #Captura e exibe qualquer erro ocorrido ao carregar os dados
        print(f"Erro ao carregar dados de {tipo}: {e}")
        return []

# Função genérica reutilizável para incluir registros
def incluirRegistro(tipo, campos):
    try:
        #Recupera os dados já existentes no arquivo correspondente
        dados = recuperarDados(tipo)
        registro = {} #Cria um dicionário vazio para o novo registro
        #Para cada campo, solicita a entrada do usuário e armazena no dicionário
        for campo, tipo_dado in campos.items():
            valor = input(f"Digite {campo} ({tipo_dado.__name__}): ")
            registro[campo] = tipo_dado(valor) #Converte o valor para o tipo apropriado
        #Verifica se o código já existe em turmas e matrículas
        if "codigo" in campos:
            for item in dados:
                if item["codigo"] == registro["codigo"]:
                    print(f"Erro: Já existe um registro com o código {registro['codigo']}.")
                    return 
        dados.append(registro) #Adiciona o novo registro à lista
        salvarDados(tipo, dados) #Salva a lista atualizada no arquivo
        print(f"{tipo.capitalize()} incluído(a) com sucesso.") #Mensagem de inclusão bem sucedida
    except ValueError:
        #Captura e informa erros de conversão de tipo
        print(f"Erro: O tipo de dado inserido não é válido.")

#Função genérica reutilizável para listar registros
def listarRegistros(tipo):
    print(f"\n--- Lista de {tipo.capitalize()} ---") #Título da lista
    dados = recuperarDados(tipo) #Carrega os dados do arquivo correspondente
    if dados: #Verifica se há dados na lista
        for item in dados: #Faz a iteração sobre cada registro e exibe suas informações
            print(", ".join(f"{k}: {v}" for k, v in item.items()))
    else:
        #Diz que não há registros cadastrados
        print(f"Nenhum {tipo} cadastrado(a).")

#Função genérica reutilizável para editar registros
def editarRegistro(tipo):
    try:
        dados = recuperarDados(tipo)  #Carrega os dados do arquivo correspondente
        codigo = int(input(f"Digite o código do {tipo[:-1]} que deseja editar: "))
        registro_encontrado = False #Indica se o registro foi encontrado
        for item in dados:
            if item["codigo"] == codigo: #Verifica se o código está correto
                registro_encontrado = True
                print("Digite os novos dados (pressione Enter para manter os atuais):")
                #Permite editar cada campo do registro
                for chave in item.keys():
                    novo_valor = input(f"{chave} ({type(item[chave]).__name__}): ")
                    if novo_valor.strip(): #Se o usuário inserir algo, atualiza o valor
                        item[chave] = type(item[chave])(novo_valor)
                salvarDados(tipo, dados) #Salva a lista atualizada no arquivo
                print(f"{tipo[:-1].capitalize()} atualizado(a) com sucesso.")
                break
        if not registro_encontrado:
            #Msg indicando que o registro não foi encontrado
            print(f"{tipo[:-1].capitalize()} não encontrado(a).")
    except ValueError:
        #Captura e informa erros de conversão de tipo
        print(f"Erro: Código inválido.")

#Função genérica reutilizável para excluir registros
def excluirRegistro(tipo):
    try:
        dados = recuperarDados(tipo) #Carrega os dados n o arquivo JSONcorrespondente
        codigo = int(input(f"Digite o código do {tipo[:-1]} que deseja excluir: "))
        registro_encontrado = False #Indica se o registro foi encontrado
        for i, item in enumerate(dados):
            if item["codigo"] == codigo: #Verifica se o código corresponde
                registro_encontrado = True
                dados.pop(i) #Remove o registro da lista
                salvarDados(tipo, dados) #Salva a lista atualizada no arquivo
                print(f"{tipo[:-1].capitalize()} excluído(a) com sucesso.")
                break
        if not registro_encontrado:
            #Mensagem caso o registro não seja encontrado
            print(f"{tipo[:-1].capitalize()} não encontrado(a).")
    except ValueError:
        #Captura e informa erros de conversão de tipo
        print(f"Erro: Código inválido.")

#Função para gerenciar um tipo de dado específico
def gerenciarDados(tipo, campos):
    while True:
        print(f"\n--- Gerenciar {tipo.capitalize()} ---")
        print("1 - Incluir")
        print("2 - Listar")
        print("3 - Editar")
        print("4 - Excluir")
        print("9 - Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            incluirRegistro(tipo, campos)
        elif opcao == '2':
            listarRegistros(tipo)
        elif opcao == '3':
            editarRegistro(tipo)
        elif opcao == '4':
            excluirRegistro(tipo)
        elif opcao == '9':
            break
        else:
            print("Opção inválida! Tente novamente.")

#Função que exibe o Menu principal do sistema
def mostrarMenuPrincipal():
    print("\n--- MENU PRINCIPAL ---")
    print("(1) - Gerenciar Estudantes")
    print("(2) - Gerenciar Professores")
    print("(3) - Gerenciar Disciplinas")
    print("(4) - Gerenciar Turmas")
    print("(5) - Gerenciar Matrículas")
    print("(9) - Sair")

#Dicionário que define os campos e tipos esperados para cada módulo
TIPOS = {
    "estudantes": {"codigo": int, "nome": str, "cpf": str },
    "professores": {"codigo": int, "nome": str, "cpf": str},
    "disciplinas": {"codigo": int, "nome": str},
    "turmas": {"codigo": int, "codigo_professor": int, "codigo_disciplina": int},
    "matriculas": {"codigo_turma": int, "codigo_estudante": int}
}

#Função principal que controla o funcionamento do programa
def main():
    while True:
        mostrarMenuPrincipal() #exibe o menu principal
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            gerenciarDados("estudantes", TIPOS["estudantes"])
        elif opcao == '2':
            gerenciarDados("professores", TIPOS["professores"])
        elif opcao == '3':
            gerenciarDados("disciplinas", TIPOS["disciplinas"])
        elif opcao == '4':
            gerenciarDados("turmas", TIPOS["turmas"])
        elif opcao == '5':
            gerenciarDados("matriculas", TIPOS["matriculas"])
        elif opcao == '9':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    main()
