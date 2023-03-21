'''
 * Ejemplo de programa con estructura condicional
 * Programa que lea dos números por teclado y muestre el resultado de 
 * la división del primero por el segundo.     
 * Se comprueba que el divisor es distinto de cero.
'''

dividendo = int(input("Ingrese el dividendo -> "))
divisor = int(input("Ingrese el devisor -> "))

if(divisor == 0):
    print("No se puede dividir por 0")
else:
    print(f"{dividendo} / {divisor} = ",dividendo//divisor)