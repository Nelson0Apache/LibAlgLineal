from logging import exception
import numpy as np


def matrizCuadrada():
    """
    Esta función toma un número del usuario el cual dará el tamaño de la matriz, luego le pide al usuario
    los números que quiere que vaya en la matriz, también tiene la configuración de excepciones el cual 
    funcionará si el usuario escribe un str en vez de un float o un int
    """
    try:
        cuad = int(input("Ingrese el tamaño que quiere para su matriz cuadrada: "))
    except:
        print("Ingrese un numero entero")
    else:
        try:
            matriz = []
            for i in range(cuad):
                i = i + 1
                fila = []
                for j in range(cuad):
                    j += 1
                    numeros = (eval(input("Introducir los componentes de la matriz ({}, {}): " .format(i , j)))) 
                    fila.append(numeros)
                matriz.append(fila)
        except:
            print("Ingreso un str y el codigo solo sirve para numeros ya sean int o float")  
    return(matriz)  
         

def sumarMatrizNxN(Ma1, Ma2):
    """
    Toma dos matrices como entrada, primero verifica si tienen la misma dimesion, luego si la matriz es cuadrada y si es así devuelve 
    la suma de las dos matrices.
    """
    try:
        if len(Ma1) != len(Ma2):
            raise exception("No tienen la misma cantidad de fila")
    except exception as error:
        print(error) 
    try:
        if len(Ma1[0]) != len(Ma2[0]):
            raise exception("No tienen la misma cantidad de columna")
    except exception as error:
        print(error)
    
    if len(Ma1) == len(Ma1[0]):

        sumarMatriz = []
        for i in range(len(Ma1)):
            fila = []
            for j in range(len(Ma1[0])):
                fila.append(Ma1[i][j] + Ma2[i][j])
            sumarMatriz.append(fila)              
    return(sumarMatriz)
      
def multiplicarMatricesNxN(Ma1, Ma2):
    """
    Toma dos matrices como entrada, primero verifica si tienen la misma dimesion, luego si la matriz es cuadrada y si es así devuelve 
    la multiplica  las dos matrices.
    """
    try:
        if len(Ma1) != len(Ma2):
            raise exception("No tienen la misma cantidad de fila")
    except exception as error:
        print(error) 
    try:
        if len(Ma1[0]) != len(Ma2[0]):
            raise exception("No tienen la misma cantidad de columna")
    except exception as error:
        print(error) 
    
    if len(Ma1) == len(Ma1[0]):
        mult_M1M2 = []
        for i in range (len(Ma1)):
            mult_M1M2.append([])
            for j in range (len(Ma2[0])):
                mult_M1M2[i].append(0)

        for i in range(len(Ma1)): 
            for j in range(len(Ma2[0])):
                for d in range(len(Ma1[0])):
                    mult_M1M2[i][j] += Ma1[i][d]*Ma2[d][j]
        return mult_M1M2

def multiplicarMatrizVector(Ma1, Vec):
    """
    Toma una matriz y un vector como entrada y devuelve el producto de los dos
    """
    if len(Ma1[0]) == len(Vec):
        mult_M1M2 = [] 
        for i in range (len(Ma1)):
            mult_M1M2.append([])
            for p in range (len(Vec[0])):
                mult_M1M2[i].append(0)
        for i in range(len(Ma1)): 
            for p in range(len(Vec[0])):  
                for d in range(len(Ma1[0])):
                    mult_M1M2[i][p] += Ma1[i][d]*Vec[d][p]
        
        return mult_M1M2

def matricesConmutativa(Ma1, Ma2):
    """
    Toma dos matrices como entrada, primero las multiplica en un orden, después las multiplica en el
    orden contrario; si el producto de las dos matrices son iguales, imprime las matrices son conmutables
    si no son iguales imprime que no son conmutable
    """
    multiplicacion1 = multiplicarMatrizVector(Ma1, Ma2)
    multiplicacion2 = multiplicarMatrizVector(Ma2, Ma1)
    if multiplicacion1 == multiplicacion2:
        print("Las matrices {} y {} son conmutables" .format(multiplicacion1, multiplicacion2))
    else:
        print("Las matrices no son conmutables")
    return exit()


"""
def cramer(A , b):
    n = len(b)
    D = np.linalg.det(A)
    x = np.zeros(n)
    for i in range(n):
        Ai = A.copy()
        Ai[:, i] = b
        Di = np.linalg.det(Ai)
        x[i] =Di/D
    return("x", i+1, "=", round(x[i], 10))
"""


def sistemaEcuacionesMatrizInversa():    
    """
   Toma una matriz cuadrada y un vector y devuelve la solucion de sistema de ecuaciones llamando a la funcion
   del producto matriz con vector, si el sistema de ecuaciones tiene solucion arroja el resultado y si no tiene 
   solucion arroja la palabra del else.
    """
    
    
    matriz = matrizCuadrada()
    matrizInv = np.linalg.inv(matriz) 
    
    N = eval(input("ingrese el tamaño del vector: "))
    vector = []
    for i in range(N):
        i += 1
        numero = eval(input("Introducir los componentes del vector ({}): " .format(i)))
        vector.append([numero])
        resultado = multiplicarMatrizVector(matrizInv, vector)
    if resultado != None:
        print("La solucion del sistema de ecuaciones es: ", resultado)
    else:
        print("No tiene solucion unica")  
    return exit()



