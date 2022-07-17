## Variables

#1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
v1=10
print(v1)
#2) Imprimir el tipo de dato de la constante 8.5
print(type(8.5))
#3) Imprimir el tipo de dato de la variable creada en el punto 1
print(type(v1))
#4) Crear una variable que contenga tu nombre
v4="Eduardo"
#5) Crear una variable que contenga un número complejo
v5=1+1j
#6) Mostrar el tipo de dato de la variable crada en el punto 5
print(type(v5))
#7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
v7=3.1416
#8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
v81="True"
v82=True
#9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9
print(type(v81),type(v82))
#10) Asignar a una variable, la suma de un número entero y otro decimal
v10= v1+v7
#11) Realizar una operación de suma de números complejos
v5+2+2j
#12) Realizar una operación de suma de un número real y otro complejo
2+v5
#13) Realizar una operación de multiplicación
v10*v5
#14) Mostrar el resultado de elevar 2 a la octava potencia
print(2**8)
#15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
v15=27/4
print(v15)
#16) De la división anterior solamente mostrar la parte entera

print(int(v15))
#17) De la división de 27 entre 4 mostrar solamente el resto
print(27%4)
#18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
print(4*int(v15)+27%4)
#19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
v191="Edu "
v192="croto"
print(v191+v192)
#20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
print("2"==2)
#21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
print(int("2")==2)
#22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
#Por la COMA
#23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
v23=3
v23-=1
#24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
print(1<<2)

#25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

#26) Realizar una operación válida entre valores de tipo entero y string
print(2+2, "2"+"2")