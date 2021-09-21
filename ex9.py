"""
    Escribir un procedimiento, que ingresando 2 números, calcule (sus 2 posibles
    operaciones matemáticas): sumas, restas, multiplicaciones, divisiones, potencias, raíces
"""

def func(n1, n2):
    print(f'Suma: {n1 + n2}')
    print(f'Restas: {n1 - n2} y {n2 - n1}')
    print(f'Multiplicación: {n1 * n2}')
    print(f'Divisiones: {n1 / n2} y {n2 / n1}')
    print(f'Potencias: {n1**n2} y {n2**n1}')
    print(f'Raices: {n1**(0.5)} y {n2**(0.5)}')


if __name__ == '__main__':

    num1 = float(input('Ingrese un numero: '))
    num2 = float(input('Ingrese otro numero: '))

    func(num1, num2)