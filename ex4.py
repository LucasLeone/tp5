"""
    Escriba una función que reciba un valor de temperatura en precisión real, y la
    escala de temperaturas de destino, y realice la conversión paramétrica del valor.
"""
import sys


def celcius_kelvin(temp):
    return temp + 273.15


def celcius_fahrenheit(temp):
    return (temp * 9/5) + 32


def kelvin_celcius(temp):
    return temp - 273.15


def kelvin_fahrenheit(temp):
    return (temp - 273.15) * 9/5 + 32


def fahrenheit_celcius(temp):
    return (temp - 32) * 5/9


def fahrenheit_kelvin(temp):
    return (temp - 32) * 5/9 + 273.15


if __name__ == "__main__":

    temp = int(input('Ingrese una temperatura: '))
    print('''
        [1] Celcius
        [2] Kelvin
        [3] Fahrenheit
    ''')
    escala = int(input('Ingrese la escala: '))
    if escala > 3 or escala < 1:
        print('Escala incorrecta.')
        sys.exit()

    if escala == 1:
        print(f'La temperatura en kelvin es: {celcius_kelvin(temp)}')
        print(f'La temperatura en fahrenheit es: {celcius_fahrenheit(temp)}')
    elif escala == 2:
        print(f'La temperatura en celcius es: {kelvin_celcius(temp)}')
        print(f'La temperatura en fahrenheit es: {kelvin_fahrenheit(temp)}')
    elif escala == 3:
        print(f'La temperatura en celcius es: {fahrenheit_celcius(temp)}')
        print(f'La temperatura en kelvin es: {fahrenheit_kelvin(temp)}')