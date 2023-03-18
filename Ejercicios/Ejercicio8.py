'''
Programa que tome como dato de entrada un número que corresponde 
a la longitud del radio una esfera y nos calcula y 
escribe el volumen de la esfera que se corresponden con dicho radio.

La fórmula para calcular el volumen de la esfera es
v = (4/3)*PI*r^3
'''
import math

radio = int(input("Ingrese la onguitud de radio de la esfera -> "))
valumen = (4/3) * math.pi * radio**3
print("El volumen de la esfera es -> ",valumen)

#Solucion de chatgpt
#import math

radio = float(input("Introduce el radio de la esfera: "))
volumen = (4/3) * math.pi * radio ** 3
print("El volumen de la esfera es:", volumen)
