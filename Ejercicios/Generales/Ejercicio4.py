'''
Programa que lea una serie de números por teclado hasta que
se lea un número negativo. El programa indicará cuántos números
acabados en 2 se han leído.
'''
contador = 0
numero = 0

numero = int(input("Ingrese un numero entero -> "))

while numero >= 0:
    if numero % 10 == 2:
        contador = contador + 1

    numero = int(input("Ingrese un numero entero -> "))

print(f"Se han ingresado {contador} de numeros que terminan en dos")
