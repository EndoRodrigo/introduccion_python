'''
Programa que lea un número entero y muestre si el número es múltiplo de 10  
'''
numero = int(input("Ingrese un numero entero -> "))

if(numero % 10 == 0):
    print(f"{numero} es multiplo de 10")
else:
    print(f"{numero} no es multiplo de 10")
