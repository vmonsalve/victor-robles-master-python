"""
    Imprimir los cuadrados de los primeros 60 numeros naturales
"""
print("----- cuadrados bucle for -----")
for numero in range(1, 61):
    cuadrado = numero * numero;
    print(f"{str(cuadrado)}")

print("----- cuadrados bucle while -----")
numero_dos = 1
while numero_dos <=60:
    cuadrado_dos = numero_dos * numero_dos
    print(f"{str(cuadrado_dos)}")
    numero_dos += 1