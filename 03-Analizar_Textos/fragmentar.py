texto = "ABCDEFGHIJKLM"
fragmento = texto[2:5]      #Fragmenta el texto desde la posición 2 y coge hasta la posición 5
print(fragmento)

fragmento = texto[2:]       #Fragmenta el texto desde la posición 2 hasta el final
print(fragmento)

fragmento = texto[2:10:2]   #Fragmenta el texto desde la posición 2 hasta la 10 y guarda los valores saltando por el tercer argumento.
print(fragmento)            #Result: CEGI

frase = "Controlar la complejidad es la esencia de la programación"
print(frase[0:9])           #Result: Controlar

frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
print(frase[8::3])          #Imprime cada tercer caracter empezando desde el noveno hasta el final de la frase

frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
print(frase[::-1])          #Imprime la posición de todos los caracteres de la siguiente frase y muestra el resultado en pantalla