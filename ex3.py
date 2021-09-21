"""
    Escribir una función que me permita validar si 
    la cantidad de dígitos ingresados de un DNI son correctos.
"""


def validar_dni(dni):
    """Se valida si el dni tiene 7 u 8 caracteres."""

    if len(dni) == 7 or len(dni) == 8:
        return print('El DNI es correcto!')
    else:
        return print('DNI Incorrecto')


if __name__ == '__main__':
    
    dni = input('Ingrese su numero de documento: ')

    validar_dni(dni)