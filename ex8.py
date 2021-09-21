"""
    Escribir un procedimiento que reciba un vector de N elementos de tipo entero, y
    su longitud, y que lo retorne cargado con N números multiplicados por un valor
    constante ingresado por el usuario.
"""


def func(vector, long):
    multiplica = int(input('Cual es el numero que va a multiplicar? '))
    for i in range(long):
        vector[i] = vector[i] * multiplica

    print('El vector quedo:')
    print(vector)


if __name__ == '__main__':

    vector = []
    cant = int(input('Cuantos elementos desea agregar? '))

    for i in range(cant):
        num = int(input('Ingrese un numero entero: '))
        vector.append(num)

    func(vector, len(vector))