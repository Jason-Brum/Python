from collections import namedtuple

# Definindo a estrutura de tupla nomeada
LocalHistorico = namedtuple('LocalHistorico', ['nome', 'latitude', 'longitude'])

# Lista para armazenar os locais históricos
locais_historicos = []

# Função para cadastrar um novo local histórico
def cadastrar_local():
    nome = input("Digite o nome do local histórico: ")
    latitude = float(input("Digite a latitude: "))
    longitude = float(input("Digite a longitude: "))
    
    # Criando uma instância de LocalHistorico
    local = LocalHistorico(nome=nome, latitude=latitude, longitude=longitude)
    
    # Adicionando o local à lista de locais históricos
    locais_historicos.append(local)
    print(f"{nome} cadastrado com sucesso!")

# Função para listar todos os locais históricos cadastrados
def listar_locais():
    if locais_historicos:
        print("\nLocais Históricos Cadastrados:")
        for local in locais_historicos:
            print(f"Nome: {local.nome}, Latitude: {local.latitude}, Longitude: {local.longitude}")
    else:
        print("Nenhum local histórico cadastrado.")

# Menu de opções
while True:
    print("\n1. Cadastrar Local Histórico")
    print("2. Listar Locais Históricos")
    print("3. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        cadastrar_local()
    elif opcao == '2':
        listar_locais()
    elif opcao == '3':
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
