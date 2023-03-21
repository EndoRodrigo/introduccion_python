'''
 Programa que lea un número entero por teclado y calcule si es par o impar.
'''

numero = int(input("Ingrese un numero entero -> "))

if(numero % 2 == 0):
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")
