'''
Programa Java que convierte millas a kilómetros. 
El programa pide que se introduzca una cantidad de millas y 
calcula y muestra su equivalente en Kilómetros. El proceso se repite 
hasta que se introduzca un 0 como valor para las millas.
'''
while True:
    millas = float(input("Ingrese la cantidad de millas -> "))

    if millas != 0:
        km = millas * 1.6093
        print(f"{millas} millas equivale a {km}")
        print()
    else:
        break



