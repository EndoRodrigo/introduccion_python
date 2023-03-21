'''
 * Programa que lee tres números distintos
 * y nos dice cuál de ellos es el mayor
'''

numero_1 = int(input("Ingrese le primer numero ->"))
numero_2 = int(input("Ingrese le segundo numero ->"))
numero_3 = int(input("Ingrese le tercer numero ->"))

if(numero_1 > numero_2 and numero_2 > numero_3):
    print(f"{numero_1} es le mayor")

if(numero_2 > numero_1 and numero_2 > numero_3):
    print(f"{numero_2} es numero mayor")

if(numero_3 > numero_2 and numero_3 > numero_1):
    print(f"{numero_3} es el numero mayor")

if(numero_1 == numero_2 == numero_3):
    print("Los numeros ingresados son iguales0")