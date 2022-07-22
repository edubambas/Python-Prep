#

class calculadorapto8:
    """
    Esta clase permite que los objetos instanciados con una lista de numeros, accedan a
    métodos para verificar primos, hacer cambios de unidades de temperatura, calcular
    factoriales, ó buscar el mayor o menor valor modal.

    para instanciar un objeto hacemos: nombre_objeto.calculadora(clase_de_entrada)
    """

    def __init__(self, lista):
        self.lista=lista

        #entonces ahora debo definir funciones para esprimo, factorial y convtemp que puedan
        #recibir listas. Lo que hago es definir una funcion nueva para cada uno de los tres (que será
        #llamada desde afuera). Esta función iterará la lista de entrada, y en cada iteración se
        #llamará a la función interna "__" definida en el ejercicio 5)

        #Como la función moda ya estaba preparada para recibir una lista, en este caso no voy a precisar
        #una función interna "__".
        
    def esprimo(self):
        listaprimos=[]
        for i in self.lista:
            if (self.__esprimo(i)==True):
                listaprimos.append(i)
        return listaprimos

    def __esprimo(self,n):
        if (n==2 or n==3):
            return True
        for i in range(2,n//2+1):
            if (n%i==0):
                return False
                break
        return True



    def convtemp(self,x,y):
        """
        Esta función convierte el valor de temperatura desde la unidad "x" a la unnidad "y".
        Las unidades que maneja son Celcius, Farenheit ó Kelvin.
        Las unidades se introducen en el argumento como strings "c", "f", ó "k".
        """
        listatemperaturas=[]
        for i in self.lista:
            listatemperaturas.append(self.__convtemp(i,x,y))
        return listatemperaturas

    def __convtemp(self,t,x,y):
        """
        Esta función convierte el valor de temperatura "t" desde la unidad "x" a la unnidad "y".
        Las unidades que maneja son Celcius, Farenheit ó Kelvin.
        Las unidades se introducen en el argumento como strings "c", "f", ó "k".
        """
        if (x=="c" and y=="k"):
            return t+273.15
        elif(x=="k" and y=="c"):
            return t-273.15
        elif(x=="c" and y=="f"):
            return t*9/5+32
        elif(x=="f" and y=="c"):
            return (t-32)*5/9
        elif(x=="f" and y=="k"):
            return (t-32)*5/9+273.15
        elif(x=="k" and y=="f"):
            return (t-273.15)*9/5+32



    def factorial(self):
        """
        Esta función devuelve el factorial de un número.

        El factorial de un número n puede expresarse como:
        n!=n*(n-1)*(n-2)*...*(2)*(1)
        """
        listafactoriales=[]
        for i in self.lista:
            listafactoriales.append(self.__factorialR(i))
        return listafactoriales
    
    def __factorialR(self,n):
        """
        A esta función devuelve el factorial de "n", siendo este un número natural.

        El factorial de un número n puede expresarse como:
        n!=n*(n-1)*(n-2)*...*(2)*(1)
        """
        f=1
        if (n==int(n) and n>=0): #Esto es para que la función me admita enteros de tipo flotante
            n=int(n)  #convierto la entrada en caso de que sea un float
            if (n==0):
                return 1
            else:
                f=n*self.__factorialR(n-1)  #detalle importante! el "self." en la llamada recursiva
                return f
        else:
            print("el argumento n de la función factorial(n) debe ser un número entero no negativo.")



    def moda(self,p):
        """
        Esta función entrega el valor modal de una lista y su frecuencia.
        De haber más de un valor modal, el argumento "p" debe ser:
                                                                            "0" y se devuelve la moda de menor valor.
                                                                            "1" y se devuelve la moda de mayor valor.
        """  
        frec=0
        mf=[]
        for i in self.lista:
            f=self.lista.count(i)
            if (f>frec):
                frec=f
            
        for i in self.lista:
            f=self.lista.count(i)
            if (frec==f):
                mf.append(i)
        mf.sort()
        L=len(mf)
        if (p==1):
            return mf[L-1],frec
        elif (p==0):
            return mf[0],frec

    
    


#Y ya voy a dejar instanciado un objeto en esta clase. Lo voy a usar para poder acceder a los métodos.
objeto=calculadorapto8([0,1,2,3,4,5,3,4])