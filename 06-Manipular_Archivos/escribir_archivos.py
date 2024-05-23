## Escribir archivos
archivo = open('texto2.txt', 'r')      ## Se abre el archivo en modo lectura ('r')

archivo.close()

archivo = open('texto2.txt', 'w')      ## Se abre el archivo en modo escritura ('w'). Borra lo que había antes.
archivo.write("Este es el nuevo texto\n")     ## escribe un nuevo texto.
archivo.write("Esto tambien es del nuevo texto")  
archivo.writelines(["Hola", "que", "tal"])      ## escribe un nuevo texto, pero sin saltos de linea.

archivo.close()

lista = ["Hola", "que", "tal"]

archivo = open('texto3.txt', 'w')      ## Si no existe el archivo se crea

for l in lista:                         ## Escribe en el archivo con saltos de linea
    archivo.write(l)
    archivo.write("\n")
archivo.close()

archivo = open('texto3.txt', 'a')      ## Se abre el archivo en modo lectura ('a'). Se abre sin borrar y el puntero está al final.
for l in lista:                         ## Escribe en el archivo con saltos de linea
    archivo.write(l)
    archivo.write("\n")
archivo.close()



