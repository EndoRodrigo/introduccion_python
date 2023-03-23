'''
Programa que lea dos números enteros positivos N y M 
y muestre los múltiplos de N que hay desde 1 hasta M. 
Por ejemplo si N = 4 y M = 500 el programa mostrará los 
múltiplos de 4 desde 1 hasta 500. El valor de N deberá ser 
menor que el valor de M. Si no se introducen valores 
válidos para N o M se mostrará el mensaje correspondiente 
y se vuelven a pedir.
'''

n = int(input("Ingresar el valor de n -> "))
m = int(input("Ingrese el valor de m -> "))
lisa = []

if n > m:
    print("El valor de n debe ser menos que m")
else:
    for numero in range(1,m):
        print(numero)
        if(numero % n == 0):
            lisa.append(numero)
    print(f"los multiplos de n {n} son -> {lisa}")
