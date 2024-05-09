
# Variables y conversiones

En esta sección se detallan las variables, sus operaciones y conversiones.

## Variables y sus tipos
Las variables son espacios de memoría que se puede llenar con el valor deseado, incluso dejarlas vacias. 
Estos espacios pueden ser de distintos tipos:

### Strings
Se utilizan para almacenar texto, como nombres, mensajes o cualquier otra cadena de caracteres.

```python

nombre = "Juan"
apellido = "Pérez"
mensaje = "¡Hola, mundo!"

```

### Integer y Floats
Pueden contener números enteros (int), números de punto flotante (float) o números complejos. Los enteros son números sin decimales, como 5 o -10. Los números de punto flotante tienen decimales, como 3.14 o -0.001.

```python

edad = 25               #integer
altura = 1.75           #float
saldo_cuenta = 1000.50  #float

```

### Booleans
Solo pueden tener dos valores: Verdadero (True) o Falso (False). Se usan para expresar condiciones lógicas, como si algo es cierto o falso.

```python

activo = True
validado = False

```

### Listas
Son colecciones ordenadas de elementos. Pueden contener cualquier tipo de dato, y los elementos pueden modificarse una vez que se crean.

```python

numeros = [1, 2, 3, 4, 5]
colores = ["rojo", "verde", "azul"]

```

### Tuplas
Son similares a las listas, pero son inmutables, lo que significa que no se pueden modificar una vez creadas. Se definen utilizando paréntesis en lugar de corchetes.

```python

coordenadas = (10, 20)
dimensiones = (100, 200, 50)


```

### Diccionarios
Son colecciones no ordenadas de pares clave-valor. Cada elemento del diccionario tiene una clave única y un valor asociado. Se utilizan para almacenar información estructurada.

```python

persona = {"nombre": "María", "edad": 30, "ciudad": "Madrid"}
producto = {"nombre": "Portátil", "precio": 799.99, "disponible": True}


```

### Set
Son colecciones desordenadas de elementos únicos. Se utilizan para realizar operaciones de conjuntos, como unión, intersección o diferencia. 

```python

vocales = {"a", "e", "i", "o", "u"}
numeros_primos = {2, 3, 5, 7, 11}

```

## Diferenciar tipos de variables
El método type() en Python se utiliza para obtener el tipo de un objeto o variable. Proporciona información sobre qué tipo de dato es una variable o un objeto en particular. Aquí hay un ejemplo:

```python

# Definir una variable numérica
numero = 10

# Definir una lista
lista = [1, 2, 3, 4, 5]

# Definir una variable de texto
texto = "Hola, mundo!"

# Utilizar type() para obtener el tipo de la variable
print(type(numero))  # Salida: <class 'int'>

# Utilizar type() para obtener el tipo de la variable
print(type(lista))  # Salida: <class 'list'>

# Utilizar type() para obtener el tipo de la variable
print(type(texto))  # Salida: <class 'str'>

```

## Conversiones
En Python, el casting de tipos es el proceso de convertir un tipo de datos en otro. Esto puede ser implícito, donde Python realiza la conversión automáticamente según sea necesario, o explícito, donde el usuario especifica la conversión utilizando funciones predefinidas.

- Casting implícito: Python convierte automáticamente un tipo de datos en otro según la operación que se esté realizando, sin que el usuario lo especifique explícitamente. Por ejemplo, al sumar un entero y un flotante, Python convierte automáticamente el entero en flotante para realizar la operación.
- Casting explícito: También conocido como conversión de tipo, el usuario especifica la conversión utilizando funciones predefinidas. Por ejemplo, para convertir un número entero en una cadena, se puede utilizar la función str(), o para convertir una cadena en un entero, se puede usar int().

### Casting de string a entero

```python

cadena = "123"
entero = int(cadena)


```

### Casting de entero a cadena

```python

entero = 123
cadena = str(entero)

```

### Casting de cadena a flotante

```python

cadena = "3.14"
flotante = float(cadena)

```

### Casting de flotante a entero

```python

flotante = 3.14
entero = int(flotante)


```

### Casting de entero a flotante (para preservar los decimales)

```python

entero = 5
flotante = float(entero)

```

## Método format()

El método format() en Python se utiliza para formatear cadenas de texto. Permite insertar valores en una cadena de formato y personalizar la salida de manera más flexible que el método de concatenación convencional.

El método format() funciona colocando llaves {} dentro de una cadena donde se desea insertar los valores y luego pasando esos valores como argumentos al método format().

### Formato básico

```python

nombre = "Juan"
edad = 30
mensaje = "Hola, me llamo {} y tengo {} años.".format(nombre, edad)
print(mensaje)  # Salida: Hola, me llamo Juan y tengo 30 años.


```

### Especificando el orden de los valores

```python

mensaje = "{1} tiene {0} años.".format(edad, nombre)
print(mensaje)  # Salida: Juan tiene 30 años.


```

### Nombrando las variables

```python

mensaje = "El {animal} es {adjetivo}.".format(animal="perro", adjetivo="fiel")
print(mensaje)  # Salida: El perro es fiel.



```

## Operadores
Los operadores matemáticos en Python se utilizan para realizar operaciones aritméticas básicas. Aquí tienes una explicación de los operadores más comunes junto con ejemplos:

```python

#Suma:
a = 5
b = 3
resultado = a + b  # resultado será 8

#Resta:
a = 10
b = 7
resultado = a - b  # resultado será 3

#Multiplicación
a = 4
b = 6
resultado = a * b  # resultado será 24

#División
a = 20
b = 5
resultado = a / b  # resultado será 4.0

#División entera. Devuelve el cociente entero
a = 20
b = 6
resultado = a // b  # resultado será 3

#Módulo
a = 17
b = 5
resultado = a % b  # resultado será 2

#Potencia
a = 2
b = 3
resultado = a ** b  # resultado será 8


```

## Redondeo. Round()

El método round() en Python se utiliza para redondear un número a una cantidad específica de dígitos decimales. Aquí tienes una explicación y varios ejemplos:

### Uso básico

```python

numero = 3.14159
resultado = round(numero, 2)  # Redondea el número a 2 dígitos decimales
print(resultado)  # Salida: 3.14

```

### Redondeo al entero mas cercano

```python

numero = 6.8
resultado = round(numero)  # Redondea al entero más cercano
print(resultado)  # Salida: 7


```

### Redonde con valor negativo

```python

numero = 25.987
resultado = round(numero, -1)  # Redondea al múltiplo de 10 más cercano
print(resultado)  # Salida: 30.0

```

### Redondeo con número grandes

```python

numero = 123456.789
resultado = round(numero, -3)  # Redondea al múltiplo de 1000 más cercano
print(resultado)  # Salida: 123000.0

```
