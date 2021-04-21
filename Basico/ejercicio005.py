"""
    Hacer un script que muestro todos los numeros, entre dos numeros ingresados
    por el usuario.
"""

numero_uno  = int(input("Ingresa numero uno: "))
numero_dos  = int(input("Ingrese numero dos: "))

if numero_uno < numero_dos:
    for numoro in range(numero_uno, (numero_dos + 1)):
        print(numero)
else:
    for numero in range(numero_dos, (numero_uno + 1)):
        print(numero)