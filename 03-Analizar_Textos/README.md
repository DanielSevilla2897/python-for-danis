# Analizar de textos
En esta sección se va a explicar los metodos utilizados para analizar y procesar textos.

## Propiedades
Las propiedades de las cadenas de texto son las siguientes:

- Inmutabilidad: Un string no puede cambiar sus caracteres en la misma variable
- Concatenable.
- Multiplicables: Se puede multiplicar un string concatenandolo x veces. 
```python

nombre = "Dani"
print(nombre*5) #Sailda: DaniDaniDaniDaniDani

```
- Multilineales: Añadiendo 3 dobles comillas se puede escribir el texto con saltos de linea.
```python
texto_con_saltos = """Mil pequeños peces blancos        
comosi hirviera
el color del agua"""
```
- Verificar si contiene: Se puede imprimir si una cadena se encuentra dentro de un string.
```python
nombre = "Daniel Sevilla"
print("Sevilla" in nombre)   #Result: true
print("Carlos" in nombre)    #Result: false
```
- Longitud de un string: Con el metodo len(string) te devuelve el número de caracteres.
```python
texto_con_saltos = """Mil pequeños peces blancos        
comosi hirviera
el color del agua"""                                #Con triples dobles comillas se pueden poner saltos de linea

print(len(texto_con_saltos))                        #Result: 68
```

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

## Métodos String

### upper()
Este método convierte todos los caracteres de una cadena en mayúsculas. Ejemplo: "hello".upper() devuelve "HELLO".

### lower()
Convierte todos los caracteres de una cadena en minúsculas. Ejemplo: "Hello".lower() devuelve "hello".

### split()
Divide una cadena en subcadenas utilizando un separador especificado y devuelve una lista de las subcadenas. Ejemplo: "apple,banana,orange".split(",") devuelve ['apple', 'banana', 'orange'].

### join()
Une los elementos de un iterable (como una lista) usando la cadena como separador. Ejemplo: " ".join(['apple', 'banana', 'orange']) devuelve "apple banana orange".

### find()
Encuentra la primera ocurrencia de una subcadena dentro de una cadena y devuelve su índice. Ejemplo: "hello".find("l") devuelve 2.

### replace()
Reemplaza todas las ocurrencias de una subcadena con otra en una cadena y devuelve una nueva cadena. Ejemplo: "hello".replace("l", "L") devuelve "heLLo".


# Analizar Listas
En esta sección se va a explicar los metodos utilizados para analizar y procesar listas. Comparten la mayoría de las funcionalidades con las de los string, pero tienen alguna propiedades diferentes bastantes utiles. 

## Métodos Listas

### len()
Devuelve la longitud de una lista, es decir, el número de elementos que contiene. Ejemplo: my_list = [1, 2, 3] y len(my_list) devuelve 3.

### sort()
Ordena los elementos de una lista en su lugar, de forma ascendente por defecto, o según un criterio especificado. Ejemplo: my_list = [3, 1, 2] y my_list.sort() resulta en my_list siendo [1, 2, 3].

### reverse(): 
Invierte el orden de los elementos en una lista. Ejemplo: my_list = [1, 2, 3] y my_list.reverse() resulta en my_list siendo [3, 2, 1].

### pop(index): 
Elimina y devuelve el elemento en la posición indicada de una lista. Si no se proporciona un índice, elimina y devuelve el último elemento. Ejemplo: my_list = [1, 2, 3] y my_list.pop(1) devuelve 2 y my_list se convierte en [1, 3].

#### append(element): 
Agrega un elemento al final de una lista. Ejemplo: my_list = [1, 2] y my_list.append(3) resulta en my_list siendo [1, 2, 3].

# Analizar Diccionarios
Los diccionarios son como listas pero sin indices, solo con claves y valor.

# Analizar Diccionarios
Los diccionarios en Python son estructuras de datos que permiten almacenar pares clave-valor. Cada elemento en un diccionario consiste en una clave única y su correspondiente valor asociado. Se definen utilizando llaves {} y los elementos se separan por comas.
En esta sección se va a explicar los metodos utilizados para analizar y procesar diccionarios. 

```python

mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

```

## Métodos Diccionarios

### get()
Para obtener el valor asociado a una clave se puede hacer de dos maneras:
```python

mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
print(mi_diccionario.get("nombre"))  # Salida: Juan
print(mi_diccionario['nombre']) # Salida: Juan

```
### keys()
```python

mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
print(mi_diccionario.keys())  # Salida: dict_keys(['nombre', 'edad', 'ciudad'])

```
### values()
```python

mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
print(mi_diccionario.values())  # Salida: dict_values(['Juan', 30, 'Madrid'])

```
### items()
```python

mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
print(mi_diccionario.items())  # Salida: dict_items([('nombre', 'Juan'), ('edad', 30), ('ciudad', 'Madrid')])

```

# Analizar Tuples
Las tuplas en Python son secuencias ordenadas e inmutables de elementos. Se definen utilizando paréntesis () y pueden contener cualquier tipo de datos, incluidos números, cadenas, listas u otras tuplas. A diferencia de las listas, las tuplas no pueden modificarse una vez creadas, lo que significa que no se pueden agregar, eliminar o modificar elementos individualmente.
Las tuplas son útiles cuando se necesita una secuencia ordenada de elementos que no debe modificarse, como coordenadas geográficas, fechas o valores constantes.

```python

mi_tupla = (1, 2, "a", "b", True)

```

## Métodos Tuples

### len()


```python

mi_tupla = (1, 2, "a", "b", True)
print(len(mi_tupla))  # Salida: 5


```

### count()

```python

mi_tupla = (1, 2, "a", "b", True)
print(mi_tupla.count("a"))  # Salida: 1


```


### index()

```python

mi_tupla = (1, 2, "a", "b", True)
print(mi_tupla.index(2))  # Salida: 1

```

# Analizar Sets
Los sets en Python son una colección desordenada de elementos únicos. Se definen utilizando llaves {} o la función set(). Los sets no admiten elementos duplicados y son útiles para eliminar duplicados de otras colecciones, así como para realizar operaciones de conjuntos como unión, intersección y diferencia.

```python

mi_set = {1, 2, 3, 4, 5}

```

## Métodos Sets

### add()
Agrega un elemento al set.

```python

mi_set = {1, 2, 3, 4, 5}
mi_set.add(6)
print(mi_set)  # Salida: {1, 2, 3, 4, 5, 6}


```

### pop()
Elimina y devuelve un elemento aleatorio del set

```python

mi_set = {1, 2, 3, 4, 5}
elemento_eliminado = mi_set.pop()
print(elemento_eliminado)  # Salida: 1


```

### remove()
Elimina un elemento específico del set. Si el elemento no existe, arroja un error.

```python

mi_set = {1, 2, 3, 4, 5}
mi_set.remove(3)
print(mi_set)  # Salida: {1, 2, 4, 5}


```

### discard()
Elimina un elemento específico del set si existe. Si el elemento no está presente, no se produce ningún error.

```python

mi_set = {1, 2, 3, 4, 5}
mi_set.discard(10)  # No produce ningún cambio ya que 10 no está en el set


```

### union()
Devuelve un nuevo set que contiene todos los elementos presentes en ambos sets.

```python

mi_set = {1, 2, 3, 4, 5}
otro_set = {4, 5, 6, 7, 8}
union_set = mi_set.union(otro_set)
print(union_set)  # Salida: {1, 2, 3, 4, 5, 6, 7, 8}


```


### len()
Devuelve la cantidad de elementos en el set.

```python

mi_set = {1, 2, 3, 4, 5}
print(len(mi_set))  # Salida: 5


```

# Analizar Booleanos
Los booleanos son un tipo de dato en programación que puede tener uno de dos valores: Verdadero (True) o Falso (False). Estos valores son fundamentales para la lógica de control de flujo y las operaciones de comparación en muchos lenguajes de programación. Se pueden decinir con el metodo bool()

```python

resultado_menor = 5 < 3
print(resultado_menor)  # Salida: False

resultado_mayor = bool(5 > 3)
print(resultado_mayor)  # Salida: True

resultado_igual = 5 == 3
print(resultado_igual)  # Salida: False

```
