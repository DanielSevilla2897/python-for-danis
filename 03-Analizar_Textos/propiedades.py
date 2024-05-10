nombre = "Dani"          
print(nombre*5)
print("Repetición"*15)

texto_con_saltos = """Mil pequeños peces blancos        
comosi hirviera
el color del agua"""                                #Con triples dobles comillas se pueden poner saltos de linea
print(texto_con_saltos)
print("agua" in texto_con_saltos)                   #Comprueba que está
print("agua" not in texto_con_saltos)               #Comprueba que no está

print(len(texto_con_saltos))                        #len te devuelve el número de caracteres del string.

texto = "electroencefalografista"
print(len(texto))