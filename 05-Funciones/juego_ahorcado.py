from random import *
def elegir_palabra(lista):
    palabra = choice(lista)
    return palabra

def mostrar_palabra(palabra):
    oculta = ""
    for n in palabra:
        oculta = oculta + "_"
    return oculta

def pedir_letra():
    letra = input("Elige una letra: ")
    return letra

def comprobar_letra(letra, palabra, oculta):
    oculta = list(oculta)
    for indice, caracter in enumerate(palabra):

        if caracter==letra:
            print("Acertaste")
            oculta[indice] = caracter

    print("Tienes una vida menos")
    resultado = ""
    for n in oculta:
        resultado = resultado+n
    return resultado

def final(palabra, oculta):
    if palabra == oculta:
        print("Has acertado la palabra")
        return True
    else:
        return False




print("Bienvenido al ahorcado. Adivina la palabra, tienes 6 vidas.")
lista_palabras = ['casa', 'perro', 'gato']
vidas = 6

palabra_elegida = elegir_palabra(lista_palabras)
oculta = mostrar_palabra(palabra_elegida)
print(oculta)
terminado = False

while vidas>0 and terminado==False:
    resultado = comprobar_letra(input("Dime una letra: "), palabra_elegida, oculta)
    oculta = resultado
    print(resultado)
    terminado = final(oculta, palabra_elegida)
    vidas = vidas - 1

    
    
    


