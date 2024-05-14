# Control de flujo
En esta sección se va a explicar todo lo relacionado con los controles de flujo con comparadores lógicos/comparación para generar loops o condiciones dentro la aplicación.

## Operadores lógicos
Los operadores lógicos son herramientas fundamentales en programación para evaluar expresiones booleanas y controlar el flujo del programa.

### AND 
Devuelve True si ambas condiciones son verdaderas.

```python

x = 5
y = 10
resultado = (x < 10) and (y > 5)
print(resultado)  # Salida: True


```

### OR 
Devuelve True si al menos una de las condiciones es verdadera.

```python

x = 5
y = 3
resultado = (x < 10) or (y > 5)
print(resultado)  # Salida: True

```

### AND 
Invierte el valor de verdad de una expresión.

```python

x = 5
resultado = not (x == 5)
print(resultado)  # Salida: False

```

## Control de flujo. Sentencia if
La sentencia if en Python es una estructura de control de flujo que permite ejecutar bloques de código condicionalmente, dependiendo de si una condición es verdadera o falsa.

### Estructura básica
- La estructura básica de la sentencia if es: if condicion:, donde condicion es una expresión que se evalúa como verdadera o falsa.
- Si la condición es verdadera, el bloque de código indentado que sigue al if se ejecuta. Si es falsa, se ignora y el programa continúa con la siguiente instrucción.
```python

x = 10
if x > 5:
    print("x es mayor que 5")

```

### Estructura If-Else
- La sentencia if se puede combinar con else para manejar casos alternativos.
- Si la condición del if es falsa, se ejecuta el bloque de código indentado bajo else.
```python

x = 3
if x > 5:
    print("x es mayor que 5")
else:
    print("x es menor o igual que 5")

```

### Estructura If-Elif-ELse
- La sentencia elif (abreviatura de "else if") se utiliza para agregar múltiples condiciones alternativas.
- Se evalúan en orden y se ejecuta el primer bloque cuya condición sea verdadera.
```python

x = 0
if x > 0:
    print("x es positivo")
elif x < 0:
    print("x es negativo")
else:
    print("x es cero")

```

## Control de flujo. Sentencia for
El bucle for en Python se utiliza para iterar sobre secuencias de datos como listas, tuplas, diccionarios o incluso cadenas de texto. 

### Listas
```python

lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(elemento)


```

### Tuplas
```python

tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
    print(elemento)


```

### Diccionarios
Al iterar sobre un diccionario, se pueden acceder tanto a las claves como a los valores.

```python
diccionario = {"a": 1, "b": 2, "c": 3}
for clave, valor in diccionario.items():
    print(clave, valor)
```

### Strings
Se puede recorrer una cadena de texto caracter por caracter utilizando un bucle for.

```python

cadena = "Python"
for caracter in cadena:
    print(caracter)


```

## Control de flujo. Sentencia while
El bucle while en Python se utiliza para ejecutar un bloque de código mientras se cumpla una condición.

### Estructura básica
```python

suma = 0
i = 1
while i <= 10:
    suma += i
    i += 1
print("La suma es:", suma)


```
### Estructura con pass
La declaración pass se utiliza para representar un bloque de código vacío. A menudo se usa como marcador de posición cuando no se desea ejecutar ninguna instrucción dentro del bucle.

```python

i = 0
while i < 5:
    pass
    i += 1


```

### Estructura con break
La instrucción break se utiliza para salir del bucle mientras la condición aún se cumple, incluso si la condición del bucle while sigue siendo verdadera.

```python

i = 0
while i < 5:
    if i == 3:
        break
    print(i)
    i += 1



```

### Estructura con continue
La declaración continue se utiliza para omitir el resto del código dentro del bucle y continuar con la próxima iteración del bucle.

```python

i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

```

## Método range
La función range() en Python se utiliza para generar secuencias de números enteros.

- Cuando se proporciona un solo argumento a range(), crea una secuencia que va desde 0 hasta ese número, excluyendo el número final. Ejemplo: range(5) genera la secuencia de números [0, 1, 2, 3, 4].
- Al pasar dos argumentos a range(), especificas el inicio y el final de la secuencia (excluyendo el número final). Ejemplo: range(2, 7) produce la secuencia [2, 3, 4, 5, 6].
- Cuando se proporcionan tres argumentos, range() genera una secuencia que comienza en el primer argumento, termina antes del segundo argumento y avanza en incrementos dados por el tercer argumento Ejemplo: range(1, 10, 2) genera la secuencia [1, 3, 5, 7, 9].

Para crear una lista utilizando range(), puedes convertir la secuencia generada por range() en una lista utilizando la función list().

```python

lista1 = list(range(5))      # [0, 1, 2, 3, 4]
lista2 = list(range(2, 7))    # [2, 3, 4, 5, 6]
lista3 = list(range(1, 10, 2))  # [1, 3, 5, 7, 9]

```

## Método enumerate
La función enumerate() en Python se utiliza para iterar sobre una secuencia (como una lista, tupla o cadena) mientras se mantiene un contador para el índice. 

## Ejemplo general
Se puede utilizar enumerate() para crear una lista de tuplas donde cada tupla contiene un índice y un valor.

```python

lista = ["a", "b", "c"]
lista_enum = list(enumerate(lista))
print(lista_enum)

```

## Ejemplo con for

```python

palabras = ["manzana", "banana", "cereza"]
for indice, palabra in enumerate(palabras):
    print(f"La palabra en el índice {indice} es: {palabra}")

### Siendo el resultado:

La palabra en el índice 0 es: manzana
La palabra en el índice 1 es: banana
La palabra en el índice 2 es: cereza


```

## Método zip
El método zip() en Python combina elementos de dos o más iterables en una serie de tuplas. Cada tupla contiene elementos correspondientes de los iterables originales, emparejados en el mismo índice. 
- El método zip() se usa con la sintaxis zip(iterable1, iterable2, ...).
- zip() crea un iterador que produce tuplas donde el i-ésimo elemento de cada iterable se combina en la i-ésima tupla.

```python

numeros = [1, 2, 3]
letras = ['a', 'b', 'c']
for numero, letra in zip(numeros, letras):
    print(numero, letra)

### Result:

1 a
2 b
3 c

```

## Min y Max
El método min() y max() en Python son funciones integradas que permiten encontrar el valor mínimo y máximo, respectivamente, dentro de un iterable, como una lista, tupla o conjunto.

### min
Devuelve el valor mínimo de un iterable.

```python

lista = [3, 1, 5, 2]
print(min(lista))  # Output: 1

```

### max
Retorna el valor máximo de un iterable.

```python

tupla = (10, 7, 15, 20)
print(max(tupla))  # Output: 20

```

## Librería Random
La biblioteca random en Python proporciona funciones para generar números pseudoaleatorios y realizar operaciones relacionadas con la aleatoriedad.La biblioteca random en Python proporciona funciones para generar números pseudoaleatorios y realizar operaciones relacionadas con la aleatoriedad.

### randint
Genera un número entero aleatorio en el rango [a, b], ambos inclusive.

```python

from random import *
num = random.randint(1, 10)
print(num)  # Output: Un número entero aleatorio entre 1 y 10

```

### uniform
Genera un número real aleatorio en el rango [a, b)

```python

from random import *
num = random.uniform(0, 1)
print(num)  # Output: Un número real aleatorio entre 0 (inclusive) y 1 (exclusivo)


```

### random
Devuelve un número real aleatorio en el rango [0, 1).

```python

from random import *
num = random.random()
print(num)  # Output: Un número real aleatorio entre 0 (inclusive) y 1 (exclusivo)


```

### choice
Devuelve un elemento aleatorio de la secuencia seq.

```python

from random import *
lista = ['a', 'b', 'c', 'd']
elem = random.choice(lista)
print(elem)  # Output: Un elemento aleatorio de la lista

```

### shuffle
Mezcla los elementos de la secuencia x de forma aleatoria.

```python

from random import *
lista = [1, 2, 3, 4, 5]
random.shuffle(lista)
print(lista)  # Output: La lista con sus elementos mezclados aleatoriamente

```