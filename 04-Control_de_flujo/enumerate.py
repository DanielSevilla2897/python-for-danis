lista = ['a', 'b', 'c']


for indice, item in enumerate(range(0, 10)):        #Enumerata coge una lista y le pone indices numerales.
    print(indice, item)

mis_tuples = list(enumerate(lista))
print(mis_tuples)


lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice, nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')


lista_indices = list(enumerate("Python"))
print(lista_indices)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres):
    if nombre.startswith('M'):
        print(indice)