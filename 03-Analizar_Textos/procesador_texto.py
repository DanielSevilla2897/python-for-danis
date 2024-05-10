texto = input("Dame un texto: ")
texto_lista = list(texto.lower())
primer_caracter = input("Dime una primera letra: ")
segundo_caracter = input("Dime una segunda letra: ")
tercer_caracter = input("Dime una tercera letra: ")


print("El caracter {} aparece {} veces".format(primer_caracter, texto_lista.count(primer_caracter)))
print("El caracter {} aparece {} veces".format(segundo_caracter, texto_lista.count(segundo_caracter)))
print("El caracter {} aparece {} veces".format(tercer_caracter, texto_lista.count(tercer_caracter)))
print("Hay un total de {} palabras".format(len(texto.split(" "))))
print("La primera letra del texto es {} y la última es {}".format(texto_lista[0], texto_lista[-1]))
print("El texto al revés se vería asi: {}".format(texto[::-1]))
print("Existe la palabra python en el texto: {}".format(bool(0 < texto.find('python'))))