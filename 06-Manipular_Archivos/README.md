# Manipulación de archivos
En esta sección se va a explicar como manipular archivos y su contenido.

## Abrir archivos
Al abrir un archivo en Python, puedes utilizar la función open() para acceder a su contenido.

- open(): Esta función abre el archivo en el modo especificado (lectura, escritura, etc.).

- readline(): Lee una sola línea del archivo cada vez que se llama. Útil para procesar archivos línea por línea.

- readlines(): Lee todas las líneas del archivo y las devuelve como una lista, donde cada elemento es una línea del archivo. Es útil cuando se desea procesar todas las líneas del archivo a la vez.

- rstrip(): Elimina los caracteres de espacio en blanco al final de una cadena, como saltos de línea o espacios adicionales.

````python

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


``