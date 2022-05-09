import re
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
    if len(Ma1) != len(Ma2):
        raise ArithmeticError("No tienen la misma cantidad de fila")
    
    if len(Ma1[0]) != len(Ma2[0]):
        raise ArithmeticError("No tienen la misma cantidad de columna")
    
    if len(Ma1) == len(Ma1[0]):

        sumarMatriz = []
        for i in range(len(Ma1)):
            fila = []
            for j in range(len(Ma1[0])):
                fila.append(Ma1[i][j] + Ma2[i][j])
            sumarMatriz.append(fila)              
    return(sumarMatriz)
      
Ma1 = [[1, 2], [3, 4]]
Ma2 = [[4, 8], [9, 5]]

print(sumarMatrizNxN(Ma1, Ma2))



