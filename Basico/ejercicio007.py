"""
    Hacer un programa que pida dos numeros a los usuarios
    y que muestre todos los numeros impares que hay entre
    ellos
"""

numero_uno = int(input("Ingresa un numero: "))
numero_dos = int(input("Ingresa un numero: "))

if numero_uno < numero_dos:
    for numero in range(numero_uno, (numero_dos+1)):
        if numero % 2 != 0:
            print(numero)
else:
    for numero in range(numero_dos, (numero_uno+1)):
        if numero % 2 != 0:
            print(numero)