'''
Programa que lea un carácter por teclado y compruebe si es un número
'''

numero = input("Ingrese un caracter -> ")

if(numero.isnumeric()):
    print("El valor ingresado es numerico")
else:
    print("El valor ingresado no es numerico")