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

## Fragmentación de cadenas de texto
El uso de la sintaxis [::] en Python permite fragmentar cadenas de texto utilizando la técnica conocida como "slicing".

### Slicing básico
```python

cadena = "Python es genial"
resultado = cadena[2:6]  # Extrae desde el tercer hasta el sexto carácter
print(resultado)  # Salida: thon

```

### Slicing con paso
```python

cadena = "Python es genial"
resultado = cadena[::2]  # Extrae cada segundo carácter
print(resultado)  # Salida: Pto sgnl

```

### Slicing en orden inverso
```python

cadena = "Python es genial"
resultado = cadena[::-1]  # Invierte la cadena
print(resultado)  # Salida: laing seg se nohtyP

```

### Sligin con índices negativos
```python

cadena = "Python es genial"
resultado = cadena[-5:-1]  # Extrae desde el quinto carácter desde el final hasta el segundo desde el final
print(resultado)  # Salida: enia

```

### Slicing con índices fuera de rango
```python

cadena = "Python es genial"
resultado = cadena[20:]  # Extrae desde el vigésimo carácter hasta el final
print(resultado)  # Salida: ''

```

