nombre = "Juan"

print(nombre)                                   #Se imprime el valor de la variable

nombre = "Laura"                                #Se cambia el valor de la vairable nombre

print(nombre)                                   #Se imprime nuevo valor

nombre = "Julia"
apellido = "Roberts"
nombrecompleto = nombre + " " + apellido        #Concatenación de strings

edad = 25
edad2 = 15
print(edad + edad2)                             #Se imprime la suma

nombre_guardado = input("Dime tu nombre: ")     #Se guarda en la variable el contenido del input
print("Se ha guardado :" + nombre_guardado)

mi_numero = 1
mi_float = 5.8
print(type(mi_numero))                          #Función type() nos da el tipo de la variable en el argumento.
print(type(mi_float))

print(mi_numero + mi_float)                     #El tipo es un float

#Ejemplo de print que suele dar error. Python no permite hacer concatenaciones con variables compuestas de integer y strings. El siguiente ejemplo muestra el problema.

edad = input("Dime tu edad: ")
print("Tu edad es: " + edad)
nueva_edad = 1 + edad                           #Esto da error porque la respuesta de input() siempre es string.

num_entero = 5
print(type(num_entero))

num_decimal = 5.3
print(type(num_decimal))

num1=7.5
num2=2.5
print(type(num1+num2))                          #Esto da de resultado Float




