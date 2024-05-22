#Vendedores ganan de comisiones del 13% de las ventas totales. Pregunta del nombre e total.
nombre = input("Cual es tu nombre: ")
ventas = float(input("Cuanto has vendido en total este mes:  "))

print("El total de tu sueldo de comisiones es igual a: {} €".format(round(ventas*13/100, 2)))
