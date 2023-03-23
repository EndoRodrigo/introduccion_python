'''
Programa que pida que se introduzcan dos números enteros por 
teclado y muestre los números desde el menor hasta el mayor de 
los números introducidos
'''

while True:
    numero_1 = int(input("Ingrese el primer numero -> "))
    numero_2 = int(input("Ingrese el segundo numero -> "))

    if numero_1 == numero_2:
        print("Debe ingresar dos numeros difentes")
    elif numero_1 > numero_2:
        print(f"El {numero_1} es mayor mayor que {numero_2}")
        break
    else:
        print(f"El numero {numero_2} es mayor que {numero_1}")
        break


