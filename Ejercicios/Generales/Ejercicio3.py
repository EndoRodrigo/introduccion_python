'''
Programa que lea un número entero N y 
muestre la tabla de multiplicar de ese número.
'''

tabla = int(input("Ingrese un numero entero -> "))
numero = 1

while True:
    
    print(f"{tabla} * {numero} = ",(tabla * numero))
    numero = numero + 1

    if(numero == 11):
        break