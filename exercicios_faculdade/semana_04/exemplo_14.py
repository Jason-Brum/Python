positivosPares = []
negativosImpares = []

for i , num in enumerate(range(-10, 11)):
    if num < 0:
        if num % 2 == 1:
            negativosImpares.append([i, num])
    else:
        if num % 2 == 0:
            positivosPares.append([i, num])
print("Números negativos ímpares: ")
for i in negativosImpares:
    print(i)
print("Números psositivos pares: ")
for i in positivosPares:
    print(i)    