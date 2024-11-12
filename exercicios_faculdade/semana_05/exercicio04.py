# Inicializando o dicionário para armazenar os produtos e preços
produtos = {}

while True:
    # Solicita o nome do produto
    produto = input("Digite o nome do produto (ou 'sair' para encerrar): ").strip()
    
    if produto.lower() == 'sair':
        break
    
    # Solicita o preço do produto
    preco = float(input("Digite o preço do produto: "))
    
    # Verifica se o produto já está cadastrado
    if produto in produtos:
        # Se já existir, pergunta se o usuário deseja atualizar o preço
        atualizar = input(f"O produto '{produto}' já existe. Deseja atualizar o preço? (s/n): ").strip().lower()
        
        if atualizar == 's':
            produtos[produto] = preco
            print(f"Preço do produto '{produto}' atualizado para {preco:.2f}.")
        else:
            print("Preço não atualizado.")
    else:
        # Caso o produto não exista, adiciona ao dicionário
        produtos[produto] = preco
        print(f"Produto '{produto}' adicionado com preço {preco:.2f}.")

# Imprime o dicionário formatado como lista de produtos e preços
print("\nLista de produtos e preços:")
for produto, preco in produtos.items():
    print(f"{produto}: R$ {preco:.2f}")
