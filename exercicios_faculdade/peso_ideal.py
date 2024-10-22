genero = str(input("Informe seu gênero(M ou F): "))
altura = float(input("Informe sua altura em metros: "))

idealMasc = (altura * 72.9) - 58.0
idealFem = (altura * 62.1) - 44.70

if (genero == "F"):
    print(f'Seu peso ideal é {idealFem} Kg')
else:
    print(f'O seu peso ideal é {idealMasc} Kg')