# *args = funciones con parametros variables.

def suma (*args):                           # *args permite que se puedan recibir tantos paremetros como se quieran, sin importar nada
    total = 0
    for arg in args:
        total = total + arg
    return total

print(suma(5,6,8,9,10))


def suma_cuadrados(*numeros):
    total = 0
    for n in numeros:
        total = total + n**2
    return total
    
suma_cuadrados(1,2,3)


def suma_absolutos(*args):
    total = 0
    for n in args:
        total = total + abs(n)
    return total

def numeros_persona(nombre, *args):
    total = sum(args)
    texto = nombre + ", la suma de tus números es "+ str(total)
    return texto

# **kargs = funciones con parametros variables con key y value.
def suma(num1, num2, *args, **kwargs):
    print(num1)
    print(num2)
    for arg in args:
        print(f"arg={arg}")
    for clave, valor in kwargs.items():
        print(f"{clave}={valor}")
    print(type(kwargs))

suma(1, 2, 50, 100, 200, x=3, y=5, z=2)

#### Ejemplo importante

args = [100, 200, 230]
kargs = {'x':1}

suma(1, 2, *args, **kargs)              ## Se puede poner como parametros los args y los kargs como listas y diccionarios pero añadiendo * o **


#
def cantidad_atributos(**kargs):
    total = 0
    for n in kargs.items():
        total = total + 1
    return total

#
def lista_atributos(**kargs):
    lista = []
    for clave, valor in kargs.items():
        lista.append(valor)
    return lista
        
#
def describir_persona(nombre, **kargs):
    print(f"Características de {nombre}:")
    for keys, value in kargs.items():
        print(f"{keys}: {value}")
    return True