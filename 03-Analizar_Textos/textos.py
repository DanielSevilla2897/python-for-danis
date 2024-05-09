mi_texto = "Esta es una prueba"
resultado = mi_texto[0]             #De esta manera se almacena el caracter que ocupa la posición 0 del string.
print(resultado)                    #Result: E

resultado = mi_texto.index("n")     #De esta manera se almacena la posición que ocupa la "n" en el string.
print(resultado)                    #Result: 9

resultado = mi_texto.index("prueba")    #De esta manera se almacena la posición donde empieza el texto busca.
print(resultado)                        #Result: 12

### Es sensible a mayusculas y minusculas.

resultado = mi_texto.index("a")        
print(resultado)                        #Te da la posición del primer caracter del texto (izquierda a derecha). Resultado: 3

resultado = mi_texto.index("a", 5)      #El segundo argumento indica desde donde se empieza a contar. Te da la posición del string, no desde donde se empezó a contar
print(resultado)

resultado = mi_texto.index("a", 5, 11)  #Te da la posición del caracter "a" desde la posición del primer argumento hasta el segundo.
print(resultado)

resultado = mi_texto.rindex("a")        #El metodo rindex() hace lo mismo pero de derecha a iziquierda
print(resultado)



palabra = "ordenador"
print(palabra[4])                       #Devuelve la quinta posición

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(frase.index("práctica"))          #Result: 26  
print(frase.rindex("práctica"))         #Result: 57



