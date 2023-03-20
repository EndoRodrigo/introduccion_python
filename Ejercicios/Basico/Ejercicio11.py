'''
Programa que lea un número entero N de 5 cifras y muestre sus 
cifras igual que en el ejemplo.
Por ejemplo para un número N = 12345   La salida debe ser:
1
12
123
1234
12345

'''

numero = int(input("Ingrese un numero de 5 cifras -> "))
print(numero//10000)
print(numero//1000)
print(numero//100)
print(numero//10)
print(numero)