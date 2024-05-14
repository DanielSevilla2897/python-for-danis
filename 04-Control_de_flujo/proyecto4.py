# pregunta su nombre, 8 intentos de adivinar un numero. no permitido, menor, mayor y si acertó y el numero de intentos.
from random import *

usuario = input("Dime tu nombre: ")
intentos = 8
numero_secreto = randint(0,101)

while intentos>0:
    intento = int(input("Dime un número: "))
    if intento<0 or intento>100:
        print("Este número no es valido")
    elif intento>numero_secreto:
        print("El número secreto es menor")
    elif intento<numero_secreto:
        print("El número secreto es mayor")
    elif intento==numero_secreto:
        print("Has ganado")
        break
    intentos = intentos - 1

print(f"No has averiguado el numero. El número era: {numero_secreto}")
    

    