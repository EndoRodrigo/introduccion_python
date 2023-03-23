'''
Programa que lea números enteros por teclado y 
para cada número introducido indique 
si es positivo o negativo y si es par o impar. 

'''

while True:
    numero = int(input('''Ingrese el siguiente numero:
                       0. Detener el programa0  -> '''))
    if numero >= 0:
        print("El numero ingresado es positivo")
    else:
        print("El numero ingresado es negativo")

    if numero % 2 == 0:
        print("Es par")
    else:
        print("Es impar")

    if numero == 0:
        break