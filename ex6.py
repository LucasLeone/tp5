"""
    Escribir una función que reciba como parámetros un vector de números reales y
    su longitud, y devuelva al máximo valor contenido en él.
"""


def max_valor(vector, longitud):

    mayor = 0

    for i in range(0, longitud):
        if i == 0:
            mayor = vector[0]
        else:
            if vector[i] > mayor:
                mayor = vector[i]

    return mayor


if __name__ == '__main__':

    vector = []

    long = int(input('Cuantos numeros desea ingresar? '))

    for i in range(0, long):
        vector.append(int(input('Ingrese el numero: ')))

    mayor = max_valor(vector, len(vector))

    print(f'El maximo valor es: {mayor}')