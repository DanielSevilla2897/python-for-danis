## Abrir archivo

mi_archivo = open('texto1.txt')
print(mi_archivo)                   ## Esto no muestra nada que nos sirva
print(mi_archivo.read())            ## Esto si que lee el archivo y lo puedes imprimir. Lo lee una vez, el puntero se queda al final. Hay que cerrar el archivo.
mi_archivo.close()                  ## Se cierra el archivo

mi_archivo = open('texto1.txt')     ## Se vuelve a abrir el archivo
print(mi_archivo.readline())        ## Se lee la primera linea. Se guarda el puntero al final de la primera linea.
print(mi_archivo.readline())        ## Se lee la segunda linea. Se guarda el puntero al final de la segunda linea.
print(mi_archivo.readline())        ## Se lee la tercera linea. Se guarda el puntero al final de la tercera linea.
mi_archivo.close()                  ## Se cierra el archivo

mi_archivo = open('texto1.txt')              ## Se vuelve a abrir el archivo. 
print(mi_archivo.readline().rstrip())        ## Hace lo mismo pero sin saltos de linea gracias al metodo rstrip()
print(mi_archivo.readline().rstrip())        
print(mi_archivo.readline().rstrip())        
mi_archivo.close()  

mi_archivo = open('texto1.txt')
for l in mi_archivo:                ## Se puede usar un for para recorrer todas las lineas
    print("Aqui dice: " + l)
mi_archivo.close()

mi_archivo = open('texto1.txt')
todas = mi_archivo.readlines()      ##Esto lee todo el fichero y lo mete en una lista. readlines()
print(todas)
todas = todas.pop()
print(todas)
mi_archivo.close()

### 
mi_archivo = open('texto1.txt')
lista = mi_archivo.readlines()
print(lista[1])                     # Esto imprime la segunda linea del archivo
mi_archivo.close()


##
mi_archivo = open('texto1.txt')
print(mi_archivo.read())
mi_archivo.close()

mi_archivo = open('texto1.txt')
print(mi_archivo.readline());
mi_archivo.close()