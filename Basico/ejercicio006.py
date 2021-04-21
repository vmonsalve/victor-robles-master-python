"""
    Crear tablas de multiplicacion del 1 al 10
    Mostrando el titulo de cada de las tablas.
"""
for numero in range(1, 11):
    print(f"\nLa tabla del {numero}")
    for numero2 in range(1, 11):
        print(f"{numero} x {numero2} = {numero*numero2}")