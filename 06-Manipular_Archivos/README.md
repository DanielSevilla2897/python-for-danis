# Manipulación de archivos
En esta sección se va a explicar como manipular archivos y su contenido.

## Abrir archivos
Al abrir un archivo en Python, puedes utilizar la función open() para acceder a su contenido.

- open(): Esta función abre el archivo en el modo especificado (lectura, escritura, etc.).

- readline(): Lee una sola línea del archivo cada vez que se llama. Útil para procesar archivos línea por línea.

- readlines(): Lee todas las líneas del archivo y las devuelve como una lista, donde cada elemento es una línea del archivo. Es útil cuando se desea procesar todas las líneas del archivo a la vez.

- rstrip(): Elimina los caracteres de espacio en blanco al final de una cadena, como saltos de línea o espacios adicionales.

```python

# Abrir el archivo en modo de lectura ('r')
with open('archivo.txt', 'r') as archivo:
    # Leer una sola línea
    linea_unica = archivo.readline()
    print("Primera línea:", linea_unica)

    # Leer todas las líneas y guardarlas en una lista
    lineas = archivo.readlines()
    print("Todas las líneas:")
    for linea in lineas:
        print(linea.rstrip())  # Eliminar los espacios en blanco al final de cada línea

# Nota: El archivo se cierra automáticamente al salir del bloque 'with'


```

## Escribir archivos
Al escribir en un archivo en Python, puedes utilizar la función open() para acceder a su contenido. Open puede tener varias funcionalidades según el segundo argumento que recibe:
### Write (w)
- Abre el archivo para escritura.
- Si el archivo no existe, se crea uno nuevo.
- Si el archivo existe, su contenido se sobrescribe.
```python

with open('archivo.txt', 'w') as f:
    f.write("Hola, mundo!\n")

```

### Read (r)
- Abre el archivo para lectura.
- Genera un error si el archivo no existe.

```python

with open('archivo.txt', 'r') as f:
    contenido = f.read()
    print(contenido)

```

### Append (a)
- Abre el archivo para añadir contenido al final.
- Si el archivo no existe, se crea uno nuevo.

```python

with open('archivo.txt', 'a') as f:
    f.write("Nueva línea añadida al final.\n")

```

#### Funciones de escritura

- write(): Escribe una cadena de texto en el archivo.

```python 
with open('archivo.txt', 'a') as f:
    f.write("Esto se añade al final del archivo.\n")
```

- writelines(): Acepta una lista de cadenas de texto y las escribe al final del archivo.

```python 
lineas_nuevas = ["Línea 1\n", "Línea 2\n", "Línea 3\n"]
with open('archivo.txt', 'a') as f:
    f.writelines(lineas_nuevas)

```