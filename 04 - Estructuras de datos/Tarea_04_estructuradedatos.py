## Estructuras de Datos

#1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla

lista1=["La Plata","Brasilia","Asunción","La Paz", "Lima", "Bogotá"]
print(lista1)

#2) Imprimir por pantalla el segundo elemento de la lista

print(lista1[1])

#3) Imprimir por pantalla del segundo al cuarto elemento

print(lista1[1:4])
 
#4) Visualizar el tipo de dato de la lista

print(type(lista1))

#5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento

print(lista1[2:])

#6) Visualizar los primeros 4 elementos de la lista

print(lista1[:4])

#7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?

lista1.append("La Plata")
lista1.append("Quito")
#si quero meter los dos al mismo tiempo lo hago con lista1.extend(["La Plata","Quito"])

#8) Agregar otra ciudad, pero en la cuarta posición

lista1.insert(3,"Santiago")
print(lista1)
#9) Concatenar otra lista a la ya creada

lista1.extend(["Salta","Posadas"])
print(lista1)
#10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?

print(lista1.index("La Plata"))  #sólo me entrega el índice de la primera coincidencia que encuentra

#11) ¿Qué pasa si se busca un elemento que no existe?

#print(lista1.index("Caracas"))    ValueError: 'Caracas' is not in list

###una manera de buscar sin que tire error puede ser:
# if ("Caracas" in lista1):
#   print(lista1.index("Caracas"))

#y así no tira error si no está en la lista

#12) Eliminar un elemento de la lista

lista1.remove("La Plata")
print(lista1) #nuevamente recorre la lista desde el índice 0 y sólo remueve el primero que encuentra.

#13) ¿Qué pasa si el elemento a eliminar no existe?

#lista1.remove("Río")    ValueError: list.remove(x): x not in list

###del mismo modo se podría hacer:
# if("Río" in lista1):
#   lista1.remove("Río")

#y así no tira error si no está en la lista

#14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo

ulti=lista1.pop()
print(lista1,ulti)

#15) Mostrar la lista multiplicada por 4
print(lista1*4)

#16) Crear una tupla que contenga los números enteros del 1 al 20

listanum=[1]
for i in range(2,21):
    listanum.append(i)
print(listanum)
tup=tuple(listanum)
print(tup)

####mucho más facil hacer:
####tup2=tuple(range(1,21))
###print(tup2)
###tambien se puede hacer para las listas:
###list2=list(range(1,21))
###lo ví después en el video de clase

#17) Imprimir desde el índice 10 al 15 de la tupla

for i in range(10,16):
    print(tup.index(i))

#18) Evaluar si los números 20 y 30 están dentro de la tupla
estael20=False
estael30=False
for i in range(0,20):
    if (tup[i]==20):
        estael20=True
        print("El número 20 se encuentra en el índice ", i, " de la tupla")
    elif (tup[i]==30):
        estael30=True
        print("El número 30 se encuentra en el índice ", i, " de la tupla")
if (estael20==False):
    print("El número 20 no se encuentra en la tupla")
elif (estael30==False):
    print("El número 30 no se encuentra en la tupla")

### podría haber usado tambien la forma "20 in tup" y no necesitaría el for.

if (20 in tup):
    print("El número 20 se encuentra en la tupla")
else:
    print("El número 20 no se encuentra en la tupla")
if (30 in tup):
    print("El número 30 se encuentra en la tupla")
else:
    print("El número 30 no se encuentra en la tupla")
        

#19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.
l=len(lista1)
estaparis=False
for i in range(0,l):
    if (lista1[i]=="París"):
        estaparis=True
        print("París se encuentra en el índice ",i)
if (estaparis ==False):
    lista1.append("París")
    print("Se ha agregado a París al final de la lista, ya que no estaba.")
    print(lista1)

###acá tambien podría usar "París" in lista1 y me evito el for:

if ("París" in lista1):
    print("París se encuentra en la lista.")
else:
    lista1.append("París")
    print("Se ha agregado a París al final de la lista, ya que no estaba.")
    print(lista1)

#20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista

c=0
l=len(lista1)
estaciudad=False
ciudad=input("Escriba la ciudad que desea buscar en la lista: ")
for i in range(0,l):
    if (lista1[i]==ciudad):
        estaciudad=True
        c=c+1
if (estaciudad ==False):
    print("La ciudad ", ciudad, " no se encuentra en la lista")
elif (c==1):
    print("La ciudad ", ciudad, " se encuentra una vez en la lista")
else:
    print("La ciudad ", ciudad, " se encuentra ", c, " veces en la lista")


numero=float(input("Ingrese el número que desea buscar en la tupla: "))
n=tup.count(numero)
if (n==0):
    print("El número ", numero, " no se encuentra en la tupla.")
elif (n==1):
    print("El número ", numero, " aparece una vez en la tupla.")
else:
    print("El número ", numero, " aparece ",n, " veces en la tupla.")

###La funcion count seguro se puede usar tambien para listas:

ciudad=input("Escriba la ciudad que desea buscar en la lista: ")
n=lista1.count(ciudad)
if (n==0):
    print("La ciudad ", ciudad, " no se encuentra en la lista")
elif (n==1):
    print("La ciudad ", ciudad, " se encuentra una vez en la lista")
else:
    print("La ciudad ", ciudad, " se encuentra ", n, " veces en la lista")


#21) Convertir la tupla en una lista

listan=list(tup)
print(tup)
print(listan)

#22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables

v1,v2,v3 = tup[:3] #porque sino sigue recorriendo el resto de la tupla, en donde no asigné valores y da error
print(v1, v2, v3)

#23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".
p=["Argentina","Chile","Brasil","Perú"]
c=["América","Europa","Asia"]
dic={"ciudad": lista1, "país":p,"continente":c}
print(dic)

#24) Imprimir las claves del diccionario
print(dic.keys())
#25) Imprimir las ciudades a través de su clave
print(dic["ciudad"])