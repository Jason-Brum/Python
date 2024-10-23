soma = 0

qtde = int (input("Quantos números deseja informar? "))

for c in range(qtde):
    n = float(input ("Informe um valor: "))
    metade = n /2
    print (metade) 
    soma = soma + metade

print (f'Soma: {soma}')

  