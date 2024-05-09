#Convertir los datos en otro tipo de dato se llama Casting.

num1 = 20
num2 = 30.5

print(type(num1))       #result: int
print(type(num2))       #result: float

print(type(num1+num2))  #result: float


num1 = 5.8
num2 = str(num1)        #casting de float a integer
print(num2)             
print(type(num2))       #result: int

num1 = "7.5"
num2 = "10"
print(float(num1) + float(num2))    #Puedes hacer casting de string a float

edad = input("Dime tu edad: ")
print(type(edad))

edad = int(edad)
print(type(edad))

nueva_edad = 1 + edad
#print("Tu nueva edad va a ser " + nueva_edad)       #Esto da un error ya que no se pueden cocatenar strings y integers.

#La solución es hacer formateo.
print("Tu nueva edad va a ser: {}".format(nueva_edad))


x = 10
y = 5
print("Mis numeros son {} y {}".format(x, y))                       #Result: Mis numeros son 10 y 5
print("Mis numeros son {} y {} y su suma es".format(x, y, x+y))     #Result: Mis numeros son 10 y 5 y su suma es 15

color = "rojo"
matricula = 5419
print(f"El auto es de color {color} y su matricula es {matricula}") #Esta es otra manera de hacerlo más visual

nombre_asociado = "Jesse Pinkman"
numero_asociado = 399058
print(f"Estimado/a {nombre_asociado}, su número de asociado es: {numero_asociado}")

puntos_nuevos = 350
puntos_totales = 1225
print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos")

puntos_anteriores = 875
puntos_nuevos = 350
print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_anteriores + puntos_nuevos} puntos")