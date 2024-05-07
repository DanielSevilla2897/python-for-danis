
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