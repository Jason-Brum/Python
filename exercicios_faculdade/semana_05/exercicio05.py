# Dicionário para armazenar os meses e totalizar as vendas
vendas_por_mes = {
    "janeiro": 0, "fevereiro": 0, "março": 0, "abril": 0, "maio": 0, "junho": 0,
    "julho": 0, "agosto": 0, "setembro": 0, "outubro": 0, "novembro": 0, "dezembro": 0
}

while True:
    # Solicita o valor da venda e o mês
    valor_venda = input("Digite o valor da venda (ou 'sair' para encerrar): ")
    if valor_venda.lower() == 'sair':
        break
    try:
        valor_venda = float(valor_venda)
    except ValueError:
        print("Valor inválido. Por favor, insira um número.")
        continue

    mes_venda = input("Digite o mês da venda: ").strip().lower()
    
    # Verifica se o mês é válido
    if mes_venda in vendas_por_mes:
        vendas_por_mes[mes_venda] += valor_venda
    else:
        print("Mês inválido. Por favor, insira um nome de mês válido.")

# Exibe o total de vendas por mês
print("\nTotal de vendas por mês:")
for mes, total in vendas_por_mes.items():
    print(f"{mes.capitalize()}: R$ {total:.2f}")
