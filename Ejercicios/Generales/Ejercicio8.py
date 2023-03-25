'''
 Programa que pasa un número
 de decimal a binario
'''
# Pedir al usuario un número decimal
decimal = int(input("Introduce un número decimal: "))

# Inicializar la cadena binaria
binario = ""

# Convertir decimal a binario
while decimal >= 1:
    # Si el decimal es divisible por 2, añadir un 0 al principio de la cadena binaria
    if decimal % 2 == 0:
        binario = "0" + binario
    # Si no es divisible por 2, añadir un 1 al principio de la cadena binaria
    else:
        binario = "1" + binario
    # Dividir decimal entre 2
    decimal = decimal // 2

# Imprimir el número binario resultante
print("El número binario correspondiente es:", binario)