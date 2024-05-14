nombres = ['ana', 'juan', 'diego']
edades = [62, 45, 30]

combinados = zip(nombres, edades)       #Zip combina dos listas con el mismo tamaño
print(list(combinados))

nombres = ['ana', 'juan', 'diego']
edades = [62, 45, 30]
ciudades = ['madrid', 'lima', 'barcelona']

combinados = zip(nombres, edades, ciudades)       #Zip combina dos listas con el mismo tamaño

for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} años y viven en {ciudad}")

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

for capital, pais in zip(capitales, paises):
    print(f"La capital de {pais} es {capital}")