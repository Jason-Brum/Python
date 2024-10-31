frutas = ['banana', 'maçã', 'goiaba', 'pera', 'pêssego', 'figo']

print(frutas)

frutas.reverse() #inverte a ordem da lista apresentada anteriormente(não tem nada a ver com ordem alfabética)
print(f'Reverse = {frutas}')

frutas.sort() #ordem alfabética ou numérica crescente
print (f'Sort = {frutas}')

lista_antiga = frutas.copy()
frutas.clear() #limpa a lista
print(f'Clear = {frutas}')

frutas.append("tangerina") #permite colocar um novo item
print(f'Append = {frutas}')

frutas.extend(['abacate', 'morango'])
print(f'Extend = {frutas}')

if 'siriguela' in frutas:
    frutas.remove('siriguela')
else:
    print('Elemento não está na lista.')    

item = 'abacate'
if item in frutas:
    frutas.remove(item)  
else:
    print('Item não está na lista')  