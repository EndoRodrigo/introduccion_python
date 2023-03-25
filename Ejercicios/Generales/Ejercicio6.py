'''
 * Programa que determina si dos números son amigos.
 * Dos números son amigos si la suma de los divisores propios del primero
 * es igual al segundo y viceversa.
'''

numero_a = int(input("Ingrese el valor de A -> "))
numero_b = int(input("Ingrese el valor de B -> "))

suma_a = 0
suma_b = 0

for a in range(1,numero_a):
    if numero_a % a == 0:
        suma_a = suma_a + a

for b in range(1,numero_b):
    if numero_b % b == 0:
        suma_b = suma_b + b
        
if suma_a == numero_b and suma_b == numero_a:
    print(numero_a)
    print(numero_b)
    print(f"Los numero {numero_a} & {numero_b} son primos ")
else:
    print(numero_b)
    print(numero_a)
    print(f"Los numero {numero_a} & {numero_b} no son primos ")