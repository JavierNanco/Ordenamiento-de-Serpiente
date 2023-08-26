'''
Titulo      : Ordenamiento de Serpiente

Autor       : Javier Nanco
Curso       : Grafos 2023-2
Profesor    : Michael Cristi

Creado con el objetivo de solucionar la problematica del trabajo 1, con soluciones 
brotadas en base a la rubrica entregada el 20/08/2023 con plazo planificado el dia
viernes 10 de junio 2022 a las 22:00 horas.

Compilado en Visual Studio Code 2022, Python versión 3.11.0 64-bit

Fecha de creación: 23/08/2023. 
Fecha de la última modificación: 25/08/2023.

################################################################################################
Se solicita un programa que simule el camino de una serpiente dentro de una matriz, la cual va
imprimiendo en pantalla cada elemento incluido dentro de la celda en que va avanzando. El
programa debe realizar lo siguiente:
1. Pedir ingresar un número al usuario. Este número representará la dimensión de una matriz
cuadrada de mxm.
2. Automáticamente el programa llenará cada celda de la matriz M con un número correlativo
iniciando desde el 1 en la celda 1,1 (Fila, Columna).
3. Desde allí con movimientos en favor de los punteros del reloj. Vea la imagen como
referencia
################################################################################################

Se debe recorrer una matriz cuadrada en forma de espiral con una direccion horaria.
Posteriormente se debe imprimir en pantalla un vector resultante del recorrido anterior.

Para esto se pide al usuario que ingrese el valor de la matriz cuadrada, gracias a la funcion
llenar matriz, que tiene como objetivo crear la matriz con el tamaño indicado para luego pasar a la
funcion recorrer matriz, que pasara directamente los datos a un vector del tamaño de la matriz ixj.

'''

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



