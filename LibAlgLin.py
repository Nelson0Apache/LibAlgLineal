import numpy as np



def matrizCuadrada():
    """
    Esta función toma un número del usuario el cual dará el tamaño de la matriz, luego le pide al usuario
    los números que quiere que vaya en la matriz, también tiene la configuración de excepciones el cual 
    funcionará si el usuario escribe un str en vez de un float o un int
    """
    try:
        cuad = eval(input("Ingrese el tamaño que quiere para su matriz cuadrada: "))
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
    else:
        print(matriz)  
    finally:
        print("Fin :D")        

print(matrizCuadrada())
            


