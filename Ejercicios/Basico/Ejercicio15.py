'''
 Programa que lea dos variables enteras N y m y le quite a N sus m ultimas cifras.
 Por ejemplo, si N = 123456 y m = 2 el nuevo valor de N será 1234
'''
import math

n = int(input("Ingrese el valor de n -> "))
m = int(input("Ingrese ek valor de m -> "))

valor_n = n // int(math.pow(10,m))

print("El numero modificado es -> ",valor_n)