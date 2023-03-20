'''
Programa que pida por teclado la fecha de nacimiento de una persona
(dia, mes, año) y calcule su número de la suerte.
'''
dia = int(input("Ingrese el dia de su nacimiento -> "))
mes = int(input("Ingrese el mes de su nacimiento -> "))
año = int(input("Ingrese el año de su nacimiento -> "))

suma = dia + mes + año

numero1 = suma // 1000
numero2 = suma // 100 % 10
numero3 = suma // 10 % 10
numero4 = suma % 10

suerte = numero1 + numero2 + numero3 + numero4

print(f"Su numero de la suerte -> {suerte}")
