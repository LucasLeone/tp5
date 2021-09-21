"""
    El precio por cada llamada tiene una tarifa telefónica ingresado por el
    administrador en euros. Si hablamos durante 5 minutos, la llamada nos cuesta
    4,35 euros si el precio es 0,87 euros por minuto y la llamada es realizada desde
    España. Halla la función que nos da el precio total de la llamada según los
    minutos que estemos hablando, el país, y el precio ingresado por el administrador
    al ingresar al programa.
"""

def func(tarifa, minutos, pais):

    print(f'El precio total de la llamada fue ${tarifa * minutos} y fue hecha desde {pais}')


if __name__ == '__main__':

    tarifa = float(input('Ingrese la tarifa telefonica: $'))
    minutos = float(input('Ingrese la cantidad de minutos hablados: '))
    pais = input('Ingrese el pais: ')

    func(tarifa, minutos, pais)