# Faça um algoritmno que:
# a) Receba a quantidade de cupons a cada mesa ocupada
# b) Informe a qtde de cupons restantes até atingir o limite do dia
# c) Mostre a mensagem: "Não devem mais ser aceitos cupons hoje" qdo o limite for atingido

limite = 10
while limite > 0:
    qtde = int(input("Quantos cupons foram apresentados? "))
    limite = limite - qtde
    if limite > 0:
        print(f'{limite} cupons ainda podem ser usados essa noite')
    else:
        print("Não podemos receber mais cupons hoje")


