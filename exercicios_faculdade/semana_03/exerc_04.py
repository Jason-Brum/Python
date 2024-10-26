num = int(input("Informe um número: "))
print(f'Tabuada do {num}')
for i in range(1, 11):
    mult = i * num
    print(f'{num} x {i} = {mult} ')