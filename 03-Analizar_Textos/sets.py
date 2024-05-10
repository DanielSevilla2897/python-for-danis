mi_set = set([1,2,3,4,5])
print(type(mi_set))                     #Result: 'set'

otro_set = {1, 2, 3}
print(type(otro_set))

mi_set = set([1,2,3,4,5,1,3,4,5,6])
print(mi_set)                          #Result: 1, 2, 3, 4, 5, 6. En sets no hay repeticiones.

otro_set = ([1,2,3,(1,2,3)])            #Solo permite añadir tuples porque son inmutables.
print(otro_set)

print(len(mi_set))                      #Result: 6
print(2 in mi_set)                      #Result: true

s1 = {1, 2, 3}
s2 = {3, 4, 5, 6}
s3 = s1.union(s2)
print(s3)                               #Result: {1, 2, 3, 4, 5, 6}

mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5} 
mi_set_3 = mi_set_1.union(mi_set_2)
print(mi_set_3)                         #Result: {1, 2, 'tres', 4, 5, 'cuatro'}

s1.add(4)
print(s1)                               #Result:{1, 2, 3, 4}

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.add("Damián")

s1.remove(4)                            #Borra un elemento del set. Si no está da error. Mejor usar discard
print(s1)

s1.discard(4)                   
print(s1)

s1.pop()                               #Pop con los sets elimina uno aleatorio
print(s1)

