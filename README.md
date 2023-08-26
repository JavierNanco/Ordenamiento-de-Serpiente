# Ordenamiento-de-Serpiente
'''
Titulo      : Ordenamiento de Serpiente

Autor       : Javier Nanco
Curso       : Grafos 2023-2
Profesor    : Michael Cristi

Creado con el objetivo de solucionar la problematica del trabajo 1, con soluciones 
brotadas en base a la rubrica entregada el 20/08/2023 con plazo planificado el dia
sabado 26 de agosto de 2023 a las 11:20

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
