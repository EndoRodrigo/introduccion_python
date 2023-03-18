'''
Programa que lea un número de 3 cifras y 
muestre por pantalla las cifras del número                                 

'''

numero = input("Ingrese un numero de mas de una cifra -> ")
print(f"El numero de cifras del {numero} es -> {len(numero)}")


#Solucion de chatgpt
numero = int(input("Introduce un número de 3 cifras: "))

# Obtenemos las cifras del número dividiéndolo y tomando el resto de la división
cifra_centenas = numero // 100
cifra_decenas = (numero // 10) % 10
cifra_unidades = numero % 10

# Mostramos las cifras en pantalla
print("La cifra de las centenas es:", cifra_centenas)
print("La cifra de las decenas es:", cifra_decenas)
print("La cifra de las unidades es:", cifra_unidades)
