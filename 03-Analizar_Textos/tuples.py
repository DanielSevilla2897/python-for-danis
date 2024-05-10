mi_tuple = (1,2,3,4)                #se puede definir tambien como: mi_tuple = 1,2,3,4
print(type(mi_tuple))

print(mi_tuple[0])                  #result: 0
print(mi_tuple[-2])                 #result: 3

mi_tuple2 = (1,2,3,(10,20),4)
print(mi_tuple2[3][0])              #result: 10

mi_tuple2 = list(mi_tuple2)
print(mi_tuple2)

t=(1, 2, 3)
x, y, z = t

print(x)
print(y)
print(z)

print(len(t))
print(t.count(3))               #Result: 1. Devuelve el numero de veces que hay un valor en una tupla.
print(t.index(3))               #Result: 2. Devuelve la posición en el tuple del valor 3

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tupla.count(2))        #Result: 6

mi_tupla = (1, 2, 3, 4)
a, b, c, d = mi_tupla
