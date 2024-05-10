mi_lista = ['a', 'b', 'c']
otra_lista = ['a', 55, 'b']
print(type(mi_lista))
print(type(otra_lista))

print(len(mi_lista))        #Te devuelve el número de elementos de la lista

print(mi_lista[0])          #Te devuelve el primer elemento de la lista

print(mi_lista[1:])         #Te devuelve los elementos desde la posición 1 hasta el final

print(mi_lista + otra_lista)    #Concatenación de listas

otra_lista.append('c')          #Agrega elemento a la lista
print(otra_lista)

otra_lista.pop()                #Eliminar ultimo elemento
print(otra_lista)

otra_lista.pop(1)                #Eliminar elemento de la posicion 1
print(otra_lista)

otra_lista = ['a', 55, 'b']
eliminado = otra_lista.pop()       #Elimina el último elemento de la lista y lo guarda en una variable
print(eliminado)        

lista_desordenada = ['h', 'i', 'w', 'a', 'c']
lista_desordenada.sort()                        #Ordena la lista y la sigue guardando en la misma variable.
print(lista_desordenada)
lista_ordenada = lista_desordenada.sort()
print(lista_ordenada)                           #Esto devuelve un None, ya que no se puede guardar en otra variable
lista_desordenada.reverse()                     #Esto devuelve la lista ordenada alfabeticamente pero al revés
print(lista_desordenada)


my_list = ['a', False, 55, True, '3']

medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append("motocicleta")
print(medios_transporte)

frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado = frutas.pop(2)
print(eliminado)