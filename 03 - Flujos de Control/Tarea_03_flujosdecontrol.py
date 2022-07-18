## Flujos de Control

#1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

n=int(input("ingrese un número entero: "))
if (n < 0):
    print("el número ",n," es menor que cero")
elif (n > 0):
    print("el número ",n," es mayor que cero")
else:
    print("el número ",n," es igual a cero")

#2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

n1=3
n2="hola"
if (type(n1)==type(n2)):
    print(n1," y ",n2, " son del mismo tipo")
else:
    print(n1," y ",n2, " son de distinto tipo")

#3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar
a=int(input("indicar paridades hasta el número: "))
for x in range(1,a+1):
    if (x%2==0):
        print(x," es par")
    else:
        print(x," es impar")

#4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

for y in range(6):
    print(y," elevado al cubo es ",y**3)

#5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

c=int(input("Ingrese el número de ciclos:"))
for i in range(1,c+1):
    print("ciclo ",i)

#6) Utilizar un ciclo while para realizar el factorial de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

f=float(input("ingrese el número del cual desea saber el factorial:"))
g=int(f)
if (f==g)&(f>0):
    while (g!=1):
        f=f*(g-1)
        g=g-1
    print("El factorial es ",int(f))
else:
    print("el número debe ser un entero positivo")

#otro modo:


f=float(input("ingrese el número del cual desea saber el factorial:"))
g=int(f)
if (f==g)&(f>0):
    if (f==1):
        print("El factorial es ",g)
    else:
        i=g-1
        while (i!=1):
            g=g*i
            i=i-1
        print("El factorial es ",g)
else:
    print("el número debe ser un entero positivo")


#7) Crear un ciclo for dentro de un ciclo while


w=int(input("ingrese los ciclos del while: "))
f=int(input("ingrese los ciclos del for: "))
contador=0
j=1
while (j<=w):
    j=j+1
    for i in range(1,f+1):
        contador=contador+1
print("el número total de ciclos son el producto de ",w," ciclos de while x ",f," ciclos de for = ",contador)



#8) Crear un ciclo while dentro de un ciclo for


f=int(input("ingrese los ciclos del for: "))
w=int(input("ingrese los ciclos del while: "))
contador=0
for i in range(1,f+1):
    j=1
    while (j<=w):
        contador=contador+1
        j=j+1
print("el número total de ciclos son el producto de ",f," ciclos de for x ",w," ciclos de while = ",contador)


#9) Imprimir los números primos existentes entre 0 y 30
c=0
h=int(input("numeros primos igual o menores que: "))
for i in range(1,h+1):
    k=0
    for j in range(1,i//2+1):
        c=c+1
        if (i%j==0):
            k=k+1
    if (k==1):
        print(i)
print("ciclos ejecutados= ",c)
    
#10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

c=0
h=int(input("numeros primos igual o menores que: "))
for i in range(1,h+1):
    k=0
    for j in range(1,i//2+1):
        c=c+1
        if (i%j==0)&(k!=2):
            k=k+1
        elif (k==2):
            break
    if (k==1):
        print(i)
print("ciclos ejecutados= ",c)


#11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

#12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?

for t in range(1,4):
    h=10**t
    c1=0
    for i in range(1,h+1):
        k=0
        for j in range(1,i//2+1):
            c1=c1+1
            if (i%j==0):
                k=k+1

    c2=0
    for i in range(1,h+1):
        k=0
        for j in range(1,i//2+1):
            c2=c2+1
            if (i%j==0)&(k!=2):
                k=k+1
            elif (k==2):
                break
    print("los ciclos disminuyen en un  ", (c1-c2)*100/c1,"% para ",h)


#13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

#la manera más ladri que se me ocurre:
i=1
p=1
while (p<=300):
    p=i*12
    i=i+1
    if (p>100)&(p<=300):
        print(p)

#pero usando el continue:

n=99
while (n<=300):
    n=n+1
    if (n%12!=0):
        continue
    print(n)

#14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente
t=5
r=input("Los primeros primos son el 2, el 3 y el 5. Le interesa buscar el siguiente? (s/n): ")

while (r=="s"):
    while (r=="s"):
        k=0
        t=t+2
        for d in range(3,t//2+1,2):

            if (t%d==0):
                k=1
                break
        if (k==0):
            break
    print("El siguiente primo es ",t)
    r=input("Le interesa buscar el siguiente? (s/n): ")



#15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

#si es múltiplo de 6 entonces es divisible por tres

n=100
while (n<=300):
    if (n%6==0):
        print("el primer número es: ",n)
        break
    n=n+1
