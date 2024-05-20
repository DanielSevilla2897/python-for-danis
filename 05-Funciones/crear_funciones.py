''''
Definición de funciones
'''

def saludar_persona(nombre):
    '''Esta función sirve para saludar a un usuario'''
    print("Hola " + nombre)

def saludar():
    print("¡Hola mundo!")

def cuadrado(un_numero):
    print(un_numero**2)

usuario = "Fernando"
saludar_persona(usuario)

''''
Return en las funciones
'''

def multiplicar(num1, num2):
    return num1*num2

multiplicar(1, 2)                           #esto no hace nada, solo invoca la funcion. se debe guardar en una variable.

print(multiplicar(1, 2))                    #Se puede imprimir directamente
total = multiplicar(1, 2)                   #Se guarda en total

def multiplicar2(num1, num2):
    total = num1*num2
    return total

def potencia(num1, num2):
    return num1**num2

def usd_a_eur(dinero):
    return dinero*0.90
    
dolares = usd_a_eur(100)

def invertir_palabra(palabra):                  #Invertir palabra función y además las escribe en mayuscula
    palabra = palabra.upper()
    return palabra[::-1]
    
palabra = invertir_palabra("hola")

'''
Funciones dinámicas
'''
def chequear_3_cifras(numero):
    return numero in range(100, 1000)

resultado = chequear_3_cifras(20)


def chequear_3_cifras_lista(lista):

    lista_3_cifras = []

    for n in lista:

        if n in range(100,1000):
            lista_3_cifras.append(n)
            return True                         #Cuando llega al return una vez, se acaba la ejecución
        else:
            pass

    return False

resultado = chequear_3_cifras_lista([200, 55000, 10000])
print(resultado)

def chequear_3_cifras_lista_guardar(lista):

    lista_3_cifras = []

    for n in lista:

        if n in range(100,1000):
            lista_3_cifras.append(n)
            
        else:
            pass

    return lista_3_cifras

resultado = chequear_3_cifras_lista_guardar([200, 55000, 10000])
print(resultado)

def todos_positivos(lista):
    for n in lista:
        if n >= 0:
            pass
        else:
            return False
    return True

def suma_menores(lista_numeros):
    suma = 0
    for n in lista_numeros:
        if n in range(0, 1000):
            suma = suma + n
        else:
            pass
    return suma

def cantidad_pares(lista_numeros):
    cantidad = 0
    for n in lista_numeros:
        if n%2==0:
            cantidad = cantidad + 1 
        else: 
            pass
    return cantidad