'''
Programa que lea dos variables
numéricas A y B e 
1. intercambie sus contenidos.
2. También se puede intercambiar el valor de dos variables
sin utilizar una variable auxiliar.
'''

numero_1 = int(input("Ingrese el valor de A -> "))
numero_2 = int(input("Ingrese el valor de B -> "))


auxiliar = numero_2
numero_2 = numero_1
numero_1 = auxiliar


print("El valor de A es -> ",numero_1)
print("El valor de B es -> ",numero_2)









#También se puede intercambiar el valor de dos variables 
# sin utilizar una variable auxiliar.

'''numero_1 = numero_1 + numero_2
numero_2 = numero_1 - numero_2
numero_1 = numero_1 - numero_2 '''
