"""
    Crear una función, que ingresa una cadena como parámetro, y calcule la longitud
    de la misma. No se permite el uso de la función interna LEN.
"""


def calcular_longitud(cadena):
    """Se pasa la cadena a una lista y se usa un ciclo for y un contador."""
    cadena = list(cadena)

    long = 0

    for i in cadena:
        long += 1

    return long


if __name__ == '__main__':

    cadena = input('Ingrese un texto: ')

    long = calcular_longitud(cadena)

    print(f'La longitud de la cadena es: {long}')