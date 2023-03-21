'''
Programa que lea tres números enteros H, M, S que contienen hora, minutos y
segundos respectivamente, y comprueba si la hora que indican es una hora válida.
'''

h = int(input("Ingrese la hora -> "))
m = int(input("Ingrese la hora -> "))
s = int(input("Ingrese la hora -> "))

if(h > 0 and h < 24 and m > 0 and m < 60 and s > 0 and s < 60):
    print("Formato de la hoa correcto")
else:
    print("El formato de la hora es incorrecto")