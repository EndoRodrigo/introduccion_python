'''
Programa que pida que se introduzcan dos números 
enteros por teclado y muestre los números desde el menor 
hasta el mayor de los números introducidos
'''

contador = 0
lista = []
while True:
    numero_a = int(input("Ingrese el numero a -> "))
    numero_b = int(input("Ingrese el numero b -> "))

    if numero_a > numero_b:
        print("El numero a debe ser menor a numero b")
    else:
        for numero in range(numero_a,numero_b):
            if numero % 2 == 0:
                lista.append(numero)

    print(f"Los numero pares son {lista}")
                    
    break

