def RecorrerMatriz(matriz):
    Filas = len(matriz)
    Columnas = len(matriz[0])
    result = []
    
    top, bottom, left, right = 0, Filas - 1, 0, Columnas - 1
    
    while top <= bottom and left <= right:
        # Recorrido hacia la derecha
        for col in range(left, right + 1):
            result.append(matriz[top][col])
        top += 1
        
        # Recorrido hacia abajo
        for row in range(top, bottom + 1):
            result.append(matriz[row][right])
        right -= 1
        
        # Comprobar si todavía hay elementos por recorrer
        if top <= bottom:
            # Recorrido hacia la izquierda
            for col in range(right, left - 1, -1):
                result.append(matriz[bottom][col])
            bottom -= 1
        
        if left <= right:
            # Recorrido hacia arriba
            for row in range(bottom, top - 1, -1):
                result.append(matriz[row][left])
            left += 1
    
    return result

def imprimirMatriz(matriz):
    print("Matriz:      ")
    for fila in matriz:
        for elemento in fila:
            print("[",elemento,"]", end=" ")  # Imprime el elemento seguido de un espacio
        print()  # Cambia de línea después de cada fila

def llenarMatriz():
    matriz=[]
    tamaño_str = input("ingresa cantidad de filas de la matriz cuadrada: ")
    tamaño = int(tamaño_str)
    a=1
    
    for _ in range(tamaño):
        fila = []
        for _ in range(tamaño):
            valor = a
            a=a+1
            fila.append(valor)
        matriz.append(fila)
    imprimirMatriz(matriz)
    return matriz

result = RecorrerMatriz(llenarMatriz())
print("\nVector resultante:   ",result) 

'''

Salida esperada: 
en caso de que el valor de la matriz sea mxm m=3 [1, 2, 3, 6, 9, 8, 7, 4, 5]

Este código define la función RecorrerMatriz que recibe una matriz como entrada
y devuelve una lista con los elementos recorridos en forma de espiral.
 
El recorrido comienza en la posición i=0, j=0 y se mueve hacia la derecha i=0, j=1,
en forma de espiral siguiendo la dirección de las agujas del reloj hasta completar el recorrido.

'''



