'''
Programa lea la longitud de los catetos de un triángulo rectángulo 
y calcule la longitud de la hipotenusa según el teorema de 
Pitágoras.

'''
import math

altura = int(input('Ingrese la longuitud del primer lado -> '))
base = int(input('Ingrese la longuitud del segundo lado -> '))

longuitud_hipotenusa = math.sqrt(math.pow(altura, 2) + math.pow(base, 2))
print("La hipenusa es -> ",longuitud_hipotenusa)

#solucion chatgpt

#import math

cateto_a = float(input("Introduce la longitud del cateto a: "))
cateto_b = float(input("Introduce la longitud del cateto b: "))

hipotenusa = math.sqrt(cateto_a ** 2 + cateto_b ** 2)

print("La longitud de la hipotenusa es:", hipotenusa)
