# Funciones
llamado o invocado. Está compuesta por un nombre, parámetros (opcionalmente), y un cuerpo que contiene las instrucciones a ejecutar. Las funciones permiten modularizar el código, facilitando su comprensión, mantenimiento y reutilización.

Cuando una función es llamada, el flujo de ejecución del programa se traslada al cuerpo de la función, donde se realizan las operaciones definidas

1. Definir la función: Utiliza la palabra clave def seguida del nombre de la función y entre paréntesis los nombres de los parámetros separados por comas.
2. Especificar los parámetros: Dentro del cuerpo de la función, utiliza los nombres de los parámetros para realizar operaciones o cálculos.
3. Llamar a la función: Cuando llames a la función, proporciona los valores para los parámetros en el mismo orden en que se definieron.

```python

def saludar(nombre, saludo):
    print(saludo, nombre)

# Llamar a la función con valores específicos para los parámetros
saludar("Juan", "Hola,")


```

## return
Es utilizado para retornar un resultado calculado dentro de la función.

- return finaliza la ejecución de una función y devuelve un valor opcional.
- El valor devuelto puede ser utilizado para asignarlo a una variable o para operaciones posteriores.

```python

def suma(a, b):
    return a + b

resultado = suma(3, 4)
print(resultado)  # Imprimirá 7

```

La sentencia print dentro de las funciones no afecta el flujo de ejecución de la función; se utiliza para propósitos de visualización.

### Ejemplo función dinámica
```python

def cantidad_pares(lista_numeros):
    cantidad = 0
    for n in lista_numeros:
        if n%2==0:
            cantidad = cantidad + 1 
        else: 
            pass
    return cantidad

```

## Argumentos Indefinidos: *args
El operador *args en Python se utiliza para pasar un número variable de argumentos posicionales a una función. Esto significa que puedes enviar una cantidad arbitraria de argumentos cuando llamas a una función que utiliza *args. Dentro de la función, estos argumentos se tratan como una tupla.

```python

def sumar(*args):
    total = 0
    for num in args:
        total += num
    return total

# Llamada a la función con diferentes números de argumentos
print(sumar(1, 2, 3))  # Imprimirá 6
print(sumar(4, 5, 6, 7))  # Imprimirá 22

```

## Argumentos Indefinidos: **kargs
El operador **kwargs en Python se utiliza para pasar un número variable de argumentos de palabra clave a una función. Similar a *args, **kwargs permite manejar un número arbitrario de argumentos, pero en este caso, se trata de argumentos de palabra clave que se pasan como un diccionario dentro de la función.

```python

'''
En este ejemplo, la función imprimir_info() acepta argumentos de palabra clave y los imprime en formato clave: valor. Puedes pasar cualquier número de argumentos de palabra clave al llamar a esta función.
'''

def imprimir_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

# Llamada a la función con diferentes argumentos de palabra clave
imprimir_info(nombre="Juan", edad=30, ciudad="Madrid")


```

### Ejemplo complejo de *args y *kargs

```python

def funcion_compleja(num1, num2, *args, **kwargs):
    # Operaciones con las variables numéricas
    suma_numeros = num1 + num2
    
    # Operaciones con las variables de tipo string
    concat_strings = ""
    for arg in args:
        concat_strings += arg + " "
    
    # Operaciones con **kwargs
    info_extra = ""
    for clave, valor in kwargs.items():
        info_extra += f"{clave}: {valor}, "
    
    # Resultado explicado
    resultado = f"Suma de números: {suma_numeros}\n" \
                f"Cadenas concatenadas: {concat_strings}\n" \
                f"Información extra: {info_extra}"
    
    return resultado

# Llamada a la función
resultado_funcion = funcion_compleja(10, 20, "Hola", "Mundo", nombre="Juan", edad=30)

print(resultado_funcion)

```

En este ejemplo de función funcion_compleja(), se realizan las siguientes operaciones:

1. Se suman los dos números num1 y num2.
2. Se concatenan todas las cadenas pasadas como argumentos posicionales *args.
3. Se recorren los argumentos de palabra clave **kwargs para obtener información adicional.
4. Se devuelve un string explicando cada operación realizada.

El resultado de la llamada a esta función con los argumentos proporcionados será un string que muestra la suma de los números, la concatenación de las cadenas y la información extra proporcionada en **kwargs.