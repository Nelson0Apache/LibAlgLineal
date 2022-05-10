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

def matricesConmutativa(Ma1, Ma2):
    """
    Toma dos matrices como entrada, primero las multiplica en un orden, después las multiplica en el
    orden contrario; si el producto de las dos matrices son iguales, imprime las matrices son conmutables
    si no son iguales imprime que no son conmutable
    """
    multiplicacion1 = multiplicarMatricesNxN(Ma1, Ma2)
    multiplicacion2 = multiplicarMatricesNxN(Ma2, Ma1)

    if multiplicacion1 == multiplicacion2:
        print("Las matrices {} y {} son conmutables" .format(multiplicacion1, multiplicacion2))
    else:
        print("Las matrices no son conmutables")



    

