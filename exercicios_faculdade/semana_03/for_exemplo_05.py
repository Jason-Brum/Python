mult = 1
for i in range(6):
    num = int(input("Digite o " + str(i + 1) + " número: "))
    if num == 0:
        continue
    mult = mult * num
print("A multiplicação dos números é", mult)