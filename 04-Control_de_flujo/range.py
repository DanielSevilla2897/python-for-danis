for numero in range(5):                     # loop de 0 a 4
    print(numero)

for numero in range(9,15):                  #loop que emieza en 9 y acaba en 14
    print(numero)

for numero in range(0, 100, 10):            # loop que empieza en 0, acaba en 100. pero se da cada 10 pasos.
    print(numero)

lista = list(range(1, 101))                 #esto vale para generar una lista con los numeros del 1 al 100
print(lista)

mi_lista = list(range(2500, 2586))
mi_lista = list(range(3, 301, 3))           #crea en una única linea de código una lista formada por todos los números múltiplos de 3 desde el 3 al 300 (inclusive).

suma_cuadrados = 0

for numero in range(1, 16):
    suma_cuadrados = suma_cuadrados + numero**2