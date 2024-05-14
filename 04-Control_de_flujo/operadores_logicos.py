# AND, OR Y NOT
mi_bool = 4 < 5 < 6             #Esto funciona ahora, pero no va a funcionar siempre
print(mi_bool)

mi_bool = (4 < 5) and (5 < 6)       # Si esto es Y esto es
print(mi_bool)

mi_bool = 1==10 or 3==30            # Es true si esto es O si esto es. Solo uno tiene que ser true.
print(mi_bool)

texto = "esta frase es breve"
mi_bool = ('frase' in texto) and ('breve' in texto)
print(mi_bool)

mi_bool = not 'a'=='b'              # Not significa si esto NO es. 
print(mi_bool)

num1 = 36
num2 = 72/2 
num3 = 48
mi_bool = ( num1 > num2 ) and ( num1 < num3 )   # AND
print( mi_bool )
mi_bool = ( num1 > num2 ) or ( num1 < num3 )    # OR
print( mi_bool )


### Verifica si las palabras almacenadas en las siguientes variables (palabra1 y palabra2) no se encuentran en la frase a continuación:

frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"
mi_bool = not (palabra1 in frase) and not (palabra2 in frase)