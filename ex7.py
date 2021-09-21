"""
    Escribir una función que reciba una matriz de valores enteros y su longitud como
    parámetros, y retorne el promedio aritmético de los valores contenidos en él.
"""


def promedio(matriz, long):
    numero = 0

    for i in range(long - 2):
        for j in matriz[i]:
            numero += j

    return numero / long


if __name__ == '__main__':

    matriz = []

    filas = int(input('Cuantas filas desea agregar? '))
    columnas = int(input('Cuantas columnas desea agregar? '))
    long = 0

    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            matriz[i].append(int(input('Ingrese un numero entero: ')))
            long += 1

    prom = promedio(matriz, long)

    print(f'El promedio es: {prom}')