'''
    Escribir un procedimiento que ingresada una 
    cadena, nos informe si la misma es palíndroma.
'''


def palindromo(cadena):
    if cadena == cadena[::-1]:
        print('Es palindromo')
    else:
        print('no es :c')


if __name__ == '__main__':

    cadena = input('Ingrese una cadena: ')

    palindromo(cadena)