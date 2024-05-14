monedas = 5

while monedas>0:                            #Mientras que monedas es mayor que 0 se ejecuta lo que tengo abajo. Si monedas no es mayor que 0, se ejecuta el else.
    print(f"Tengo {monedas} monedas")
    monedas = monedas - 1
else:
    print("No tengo más monedas")           #Monedas no es mayor que 0


respuesta = 's'
while respuesta == 's':
    respuesta = input('quieres seguir? (s/n)')
else:
    print("gracias")

respuesta = 's'
while respuesta == 's':
    pass

print("hola")

respuesta = 's'
while respuesta == 's':
    respuesta = input('quieres seguir? (s/n)')
    break
else:
    print("se escogió no")

numero = 10
while numero>=0:
    print(numero)
    numero = numero - 1

numero = 50
while numero>=0:
    if numero%5==0:
        print(numero)
    numero = numero - 1 

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for numero in lista_numeros:
    if numero>=0:
        print(numero)
    else:
        break
