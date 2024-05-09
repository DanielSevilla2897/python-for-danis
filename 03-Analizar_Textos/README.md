# Analizar de textos
En esta sección se va a explicar los metodos utilizados para analizar y procesar textos.

## Posición de caracteres. Index()

El método index() en Python se utiliza también con cadenas de texto para encontrar la posición de la primera ocurrencia de un subtexto dentro de una cadena más grande. Tener cuidado porque si no encuentra el caracter, la aplicación se detendrá.

### Uso básico.

```python

cadena = "Hola mundo, ¿cómo estás?"
indice = cadena.index("mundo")  # Encuentra la posición de la palabra "mundo"
print(indice)  # Salida: 5


```

### Búsqueda en una porción de la cadena.

```python

cadena = "Hola mundo, ¿cómo estás?"
indice = cadena.index("mundo", 6)  # Busca "mundo" después del índice 6
print(indice)  # Salida: 5


```

### Búsqueda en una porción específica

```python

cadena = "Hola mundo, mundo feliz"
indice = cadena.index("mundo", 6, 14)  # Busca "mundo" entre los índices 6 y 14
print(indice)  # Salida: 11

```

### En caso de no encontrar el elemento
Si el método index() no encuentra el elemento en una cadena lanza una excepción. Para manejarlo se puede usar un código como el del ejemplo.

```python

cadena = "Hola mundo, ¿cómo estás?"
try:
    indice = cadena.index("Python")  # Intenta encontrar la posición de "Python"
    print(indice)
except ValueError:
    print("Subtexto no encontrado")  # Salida: Subtexto no encontrado


```

#### Método rindex()
El método rindex() en Python se usa para encontrar la última ocurrencia de un carácter o subcadena dentro de una cadena de texto. Similar a index() pero busca de derecha a izquierda.

```python

cadena = "Hola mundo, ¿cómo estás?"
indice = cadena.rindex("o")  # Encuentra la última posición de la letra "o"
print(indice)  # Salida: 18


```