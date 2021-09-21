"""
    Escribir un procedimiento que calcule el factorial de un número natural pasado
    como parámetro, en forma iterativa. Realizar todas las validaciones que considere
    necesarias.
"""
import sys


def calc_factorial(numero):
    return 1 if (numero==1 or numero==0) else numero * calc_factorial(numero - 1)
    


if __name__ == '__main__':

    numero = int(input('Ingrese un número natural: '))

    print(f'El factorial es: {calc_factorial(numero)}')

