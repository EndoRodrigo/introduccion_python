'''
Programa que lea una variable entera mes y compruebe si el valor corresponde
a un mes de 30 días. Se debe comprobar que el valor introducido esté
comprendido entre 1 y 12
'''

mes = int(input("Ingrese el numero del mes -> "))

if(mes >= 1 and mes <= 12):
    if(mes == 1):
        print("Enero")
        print("Es un mes de 31 días")
    if(mes == 2):
        print("Febrero")
        print("Es un mes de 28 días")
    if(mes == 3):
        print("Marzo")
        print("Es un mes de 31 días")
    if(mes == 4):
        print("Abril")
        print("Es un mes de 30 días")
    if(mes == 5):
        print("Mayo")
        print("Es un mes de 31 días")
    if(mes == 6):
        print("Junio")
        print("Es un mes de 30 días")
    if(mes == 7):
        print("Julio")
        print("Es un mes de 31 días")
    if(mes == 8):
        print("Agosto")
        print("Es un mes de 31 días")
    if(mes == 9):
        print("Septiembre")
        print("Es un mes de 30 días")
    if(mes == 10):
        print("Octubre")
        print("Es un mes de 31 días")
    if(mes == 11):
        print("Noviembre")
        print("Es un mes de 30 días")
    if(mes == 12):
        print("Diciembre")
        print("Es un mes de 31 días")
else:
    print("El mes ingresado es incorrecto")