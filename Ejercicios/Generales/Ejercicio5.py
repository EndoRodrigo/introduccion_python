'''
El programa pide por teclado un número y muestra 
si es perfecto o no. mediante un bucle for sumaremos 
los divisores del número. Al final si esta 
suma es igual al número mostraremos el mensaje correspondiente.
'''

numero = int(input("Ingrese un numero entero -> "))
suma = 0
for number in range(1,numero):
    if numero % number == 0:
        suma = suma + number


if numero == suma:
    print(f"El numero {numero} ingresado es perfecto")
else:
    print(f"El numero {numero} no es perfecto")
        