from random import *
# Lista inicial

palitos = ['-', '--', '---', '----']

# Mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista

# Pedirle intento
def probar_suerte():
    intento = ''

    while intento not in ['1', '2', '3', '4']:
        intento = input("Elige un número del 1 al 4: ")
    
    return int(intento)



# Comprobar intento
def checkear_intento(lista, intento):
    if lista[intento - 1] == '-':
        print("A lavar los platos")
    else:
        print("Esta vez te has salvado")
    
    print(f"Te ha tocado {lista[intento-1]}")


palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
checkear_intento(palitos_mezclados, seleccion)




############

dados = range(1, 7)

def lanzar_dados():
    tirada1 = choice(dados)
    tirada2 = choice(dados)
    
    
    return [tirada1, tirada2]

def evaluar_jugada(tiradas):
    suma_dados = tiradas[0] + tiradas[1]
    mensaje = ""
    if suma_dados  <= 6:
        mensaje = "La suma de tus dados es " +  str(suma_dados) + ". Lamentable"
    elif suma_dados>6 and suma_dados<10:
        mensaje = "La suma de tus dados es " +  str(suma_dados) + ". Tienes buenas chances"
    elif suma_dados>= 10:
        mensaje = "La suma de tus dados es " +  str(suma_dados) + ". Parece una jugada ganadora"
    return mensaje
    
tirada = lanzar_dados()
print(evaluar_jugada(tirada))


#########

moneda = ['Cara', 'Cruz']

lista_numeros = [1, 2, 3]

def lanzar_moneda():
    return choice(moneda)

def probar_suerte(primer_lanzamiento, lista_numeros):
    if primer_lanzamiento=='Cara':
        print("La lista se autodestruirá")
        return []
    else:
        print("La lista fue salvada")
        return lista_numeros