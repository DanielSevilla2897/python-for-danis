# Introducción: Prints e Inputs

En esta primera sección se hace una explicación de los métodos print() e input().

- El método print() se utiliza en Python para mostrar información en la consola o terminal. Puedes usarlo para imprimir mensajes, valores de variables u otros datos que desees mostrar al usuario. 
- El método input()  se utiliza para solicitar al usuario que ingrese datos desde el teclado. Esto permite la interacción entre el programa y el usuario, ya que el programa puede solicitar información al usuario y luego procesarla.

## Ejemplo de print

```python

# Imprimir un mensaje simple
print("Hola, mundo!")

# Imprimir el valor de una variable
nombre = "Juan"
print("Hola,", nombre)

# Imprimir resultados de operaciones
a = 10
b = 5
print("La suma de", a, "y", b, "es:", a + b)

```

## Ejemplo de input

```python
# Solicitar al usuario que ingrese su nombre
nombre = input("Por favor, ingresa tu nombre: ")

# Mostrar un saludo usando el nombre ingresado
print("¡Hola,", nombre, "! Bienvenido.")

```

En los archivos prints.py e inputs.py se muestra código con varios ejemplos sencillos para comprender el funcionamiento de los métodos.
El archivo cervecería.py es la implementación algo más avanzada de un ejercicio sencillo que pide dos argumentos para generar una frase completa.