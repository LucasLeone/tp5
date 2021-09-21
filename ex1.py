"""
    Escribir una función que me permita calcular la edad de una persona.
"""

def calcular_edad(nacimiento):
    """Resta el año actual con el año de nacimiento."""
    return 2021 - nacimiento


if __name__ == '__main__':

    nacimiento = int(input('En que año nacio la persona? '))

    edad = calcular_edad(nacimiento)

    print(edad)