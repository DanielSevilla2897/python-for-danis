lista = ['a', 'b', 'c', 'd']            #Para hacer un loop se necesita un elemento iterable

for letra in lista:                     #Aqí se utiliza el for metiendo cada elemento en laa variable letra.
    numero_letra = lista.index(letra) + 1
    print(f"Letra {numero_letra}: {letra} ")



lista = ['pablo', 'laura', 'fede', 'luis', 'julia']

for nombre in lista:
    if nombre.startswith('l'):          #startswidth: para saber si una string empieza con un caracter
        print(nombre)

alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
for alumno in alumnos_clase:
    print("Hola " + alumno)


numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero
    print(mi_valor)

print(mi_valor)

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0

for numero in lista_numeros:
    suma_numeros = suma_numeros + numero

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for numero in lista_numeros:
    if numero%2>0:
        suma_impares = suma_impares + numero
    else:
        suma_pares = suma_pares + numero


palabra = 'python'                  #Los for tambien recorren string letras por letras. Es una buena forma de recorrer strings.

for letra in palabra:
        print(letra)                #El resultado cada vez es un caracter.
for letra in "python":
        print(letra)

for numero, numero2 in [[1,5],[3, 4], [4, 5]]:      #Numero y numero2 son cada elemento de cada lista anidada. En la segunda iteración numero = 1 y numero 2  = 5
    print(numero)
    print(numero2)

dic = {'c1': '1', 'c2': '2', 'c3':'3'}
for item in dic:
    print(item)                             #Cuando se recorre se devuelven las claves.
    print(dic[item])                        #Se muestran los valores de esta manera
for item in dic.values():
    print(item)
for a, b in dic.items():                    #Esta es la mejor manera para recorrer diccionarios
     print(a, b)
     