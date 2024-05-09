texto = "Este es el texto de Daniel"

resultado = texto.upper()           #Pone en mayuscula todos los caracteres
print(resultado)

resultado = texto[2].upper()        #Pone en mayuscula el caracter de la posición 2 del texto
print(resultado)                    #Result: T

resultado = texto.lower()           #Pone en minusculas todos los caracteres
print(resultado)

resultado = texto.split()           #Separa el texto cuando encuentra un espacio. La variable se convierte en una lista
print(resultado)                    #Result: ['Este', 'es', 'el', 'texto', 'de', 'Daniel']
print(type(resultado))              #Resultado: list

resultado = texto.split("t")        #Separa el texto cuando encuentra una "t". La variable se convierte en una lista
print(resultado)                    #Result: ['Es', 'e es el ', 'ex', 'o de Daniel']

a = "Aprender"
b = "Python"
c = "es"
d = "divertido"
e = " ".join([a, b, c, d])          #Une una lista de elementos con un nexo " " entre cada elemento. La variable es un string.
print(e)                            #Result: Aprender Python es divertido
print(type(e))                      #Result: str

lista_palabras = ["La","legibilidad","cuenta."]
print(" ".join(lista_palabras))

resultado = texto.find("g")         #Igual que index() pero sin generar un error si no encuentra el caracter. Si no lo encuentra devuelve un -1
print(resultado)

resultado = texto.replace("Daniel", "Roi")  #Remplaza en una cadena una serie de caracteres por otra, si la encuentra
print(resultado)       

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
print(frase.replace("difícil", "fácil").replace("mala", "buena"))       #Remplaza dificil por facil y mala por buena. Result: Si la implementación es fácil de explicar, puede que sea una buena idea.

