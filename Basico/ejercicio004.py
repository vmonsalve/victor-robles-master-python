"""
    Pedir dos numeros al usuario y hacer todas las operaciones
    básicas de una calculdora.
"""

numero_uno = int(input("Ingresa un numero: "))
numero_dos = int(input("Ingresa un numero: "))

suma           = numero_uno + numero_dos
print(f"La suma entre {str(numero_uno)} y {str(numero_dos)} es {str(suma)}")
resta          = numero_uno - numero_dos
print(f"La resta entre {str(numero_uno)} y {str(numero_dos)} es {str(resta)}")
multiplicacion = numero_uno * numero_dos
print(f"La multiplicacion entre {str(numero_uno)} y {str(numero_dos)} es {str(multiplicacion)}")

if numero_dos > 0:
    division = numero_uno / numero_dos
    print(f"La division entre {str(numero_uno)} y {str(numero_dos)} es {str(division)}")
else:
    print("La division por cero no se puede hacer...")

