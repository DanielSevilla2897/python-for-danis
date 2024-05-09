x = 6
y = 2

print(f"{x} más {y} es igual a {x+y}")
print(f"{x} menos {y} es igual a {x-y}")
print(f"{x} por {y} es igual a {x*y}")
print(f"{x} entre {y} es igual a {x/y}")

print(f"{x} truncado entre {y} es igual a {x//y}")
print(f"{x} módulo {y} es igual a {x%y}")

print(f"{x} elevado a {y} es igual a {x**y}")
print(f"{x} elevado a {3} es igual a {x**3}")
print(f"La raiz cuadrada de {x} es igual a {x**0,5}")

#Redondeo: Round() seleciona el número de decimales que se quieren mostrar redondeando hacia arriba.

print(round(90/7))                  #Result: 13
print(round(90/7, 3))               #Result: 12,857
print(type(round(90/7)))            #Result: int
print(type(round(90/7,3)))          #Result: float
