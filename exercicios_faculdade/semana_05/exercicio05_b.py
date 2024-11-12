vendas = {}
meses = [
    "janeiro",
    "fevereiro",
    "março",
    "abril",
    "maio",
    "junho",
    "julho",
    "agosto",
    "setembro",
    "outubro",
    "novembro",
    "dezembro"
]
while True:
    mes = input("Informe o mês da venda: ")
    valor = float(input("Informe o valor da venda: "))
    if not mes in meses:
        print("Mês inválido. Tente novamente!")
        continue
    if mes in vendas:
        vendas[mes] += valor
    else:
        vendas[mes] = valor
    if input("Continuar? (s/n) ") == "n":
        break
for mes in meses:
    if mes in vendas:
        print(f"{mes:>12}: R${vendas[mes]:.2f}")
    else:
        print(f"{mes:>12}: R$0.00")