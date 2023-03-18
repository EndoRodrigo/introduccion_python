'''
* Programa que calcule el área de un triángulo en función de las 
longitudes de sus lados (a, b, c)                    
 * según la siguiente fórmula: area=raiz2(p(p-a)(p-b)(p-c)) 
 donde p = (a+b+c)/2
'''
import math

lado_a = int(input("Ingrese el valo del lado a -> "))
lado_b = int(input("Ingrese el valo del lado b-> "))
lado_c = int(input("Ingrese el valo del lado c -> "))

p = (lado_a + lado_b + lado_c) / 2

area = math.sqrt(p+(p - lado_a) * (p-lado_b) * (p-lado_c))

print("El area del trigandilo es -> ",area)

#Solucion de chatgpt
#import math

a = float(input("Introduce la longitud del lado a: "))
b = float(input("Introduce la longitud del lado b: "))
c = float(input("Introduce la longitud del lado c: "))

# Calculamos el semiperímetro
s = (a + b + c) / 2

# Calculamos el área utilizando la fórmula de Herón
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print("El área del triángulo es:", area)
