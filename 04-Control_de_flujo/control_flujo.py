if 10 > 9:                                  #Esto es un if sencillo. Importante las tabulaciones.
    print('Es correcto')


x = True
if x:
    print("x es True")


if 5==2:
    print("Es correcto")
else:
    print("No es correcto")

mascota = "perro"
if mascota == "gato":
    print("Es gato")
elif mascota == "perro":                    #Sintaxis para si es un perro. elif (condiccion)
    print("Es un perro")
elif mascota == "pez":
    print("Es un pez")
else:
    print("No se que animal es")


edad = 16
calificacion = 9
if edad < 18:
    print('Eres menor de edad')
    if calificacion > 5:
        print("Has aprobado")
    else:
        print("No has aprobado")
else:
    print('Eres mayor de edad')


num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))

if num1>num2:
    print(f"{num1} es mayor que {num2}")
elif num2>num1:
    print(f"{num2} es mayor que {num1}")
elif num2==num1:
    print(f"{num1} y {num2} son iguales")

edad = 16
tiene_licencia = False

if edad > 18 and tiene_licencia:
    print("Puedes conducir")
elif edad < 18 and tiene_licencia == False:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
elif edad>18 and tiene_licencia:
    print("No puedes conducir. Necesitas contar con una licencia")


habla_ingles = True
sabe_python = False

if habla_ingles and sabe_python:
    print("Cumples con los requisitos para postularte")
elif not habla_ingles and not sabe_python:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
elif habla_ingles and not sabe_python:
    print("Para postularte, necesitas saber programar en Python")
elif not habla_ingles and sabe_python:
    print("Para postularte, necesitas tener conocimientos de inglés")