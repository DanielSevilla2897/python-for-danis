diccionario = {'c1':'valor1','c2':'valor2'}         #Valores pueden repetirse, pero las claves no (c1, c2...)
print(type(diccionario))
print(diccionario) 

resultado = diccionario['c1']
print(resultado)                                #Te devuelve el valor guardado para c1

cliente = {'nombre':'Juan','apellido':'Fuentes','peso':67,'talla':166}
consulta=cliente['apellido']
print(consulta)

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict["puntos"]["points2"][1])          #Result: 300

dic={'c1':55, 'c2':[10, 20, 30], 'c3':{'s1':100, 's2':200}}    #Esto es un diccionario donde los valores son un integer, una lista y otro diccionario
print(dic['c2'][1])                                             #Esto imprime el segundo elemento de la lista almacenada con la clave c2
print(dic['c3']['s1'])                                          #Esto imprime el valor de la clave s2 del diccionario almacenado clave c3 del diccionario principal

dic2 = {'c1': ['a','b','c'], 'c2': ['d','e', 'f'] }
print(dic2['c2'][1].upper())

dic = {1:'a', 2:'b'}
print(dic)
dic[3] = 'c'                    #Agregar valores a un diccionario. Clave 3 con valor c
print(dic)

dic[2] = 'B'                    #Sobreescribir un valor con una clave ya creada
print(dic)

print(dic.keys())               #Imprime las claves del diccionario
print(dic.values())             #Imprime los valores del diccionario
print(dic.items())              #Imprime los items (clave + valor)

mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dic["pais"]="Colombia"
mi_dic["ocupacion"]="Editora"
mi_dic["edad"]=mi_dic["edad"]+1