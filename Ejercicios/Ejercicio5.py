# Ejercicio 5. Programa que lee por teclado el valor del radio de una circunferencia y calcula y muestra por pantalla la longitud
# y el área de la circunferencia. 
#Longitud de la circunferencia = 2*PI*Radio, Area de la circunferencia = PI*Radio^2
import math

radio = int(input('Ingrese el valor del radio -> '))
longuitud_circunferencia = 2 * math.pi * radio
area_circunferencia = math.pi * radio**2

print(f'La longuitud de la circunferencia es -> {longuitud_circunferencia}')
print(f'El area de la circunferencia es -> {area_circunferencia}')

# Solucion de chargpt
#import math

radio = float(input("Ingrese el valor del radio de la circunferencia: "))
longitud = 2 * math.pi * radio
area = math.pi * radio ** 2

print("La longitud de la circunferencia es:", longitud)
print("El área de la circunferencia es:", area)
