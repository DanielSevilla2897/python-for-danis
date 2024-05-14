from random import *

aleatorio = randint(1, 50)                      #Da un valor al azar entero
print(aleatorio)

aleatorio_decimal = uniform(1, 5)               #Da un decimal al azar
print(aleatorio_decimal)

aleatorio = random()                            #Da un valor al azar menor que 1
print(aleatorio)

colores = ['azul', 'rojo', 'amarillo', "verde"]
color_aleatorio = choice(colores)                   #De una lista elije un elemento al azar
print(color_aleatorio)                          

numeros = list(range(5, 50, 5))         
shuffle(numeros)                                    #Ordena aleatoriamente los elementos de una lista
print(numeros)

nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
sorteo = choice(nombres)