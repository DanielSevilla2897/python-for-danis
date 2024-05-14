palabra = 'python'
lista = [ letra for letra in palabra ]          #se simplifica
print(lista)

lista = [n for n in range(0, 21, 2)]
print(lista)

lista = [n for n in range(0, 21, 2) if n*2<10]          #se puede añadir el if a la derecha. pero si tiene else tiene que ser a la izquierda
print(lista)


lista = [n if n*2<10 else 'no' for n in range(0, 21, 2) ]       #ejemplo de un else, se pone a la izquierda todo
print(lista)

pies = list(range(10, 50, 10))
metros = [n*3.281 for n in pies]
print(metros)

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [n**2 for n in valores]
valores_pares = [n for n in valores if n%2==0]

temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(n-32)*(5/9) for n in temperatura_fahrenheit]