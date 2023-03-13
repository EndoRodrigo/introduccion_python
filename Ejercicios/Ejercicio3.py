#3. Escribe un programa Java que lee un número entero por teclado 
#y obtiene y muestra por pantalla el doble y el triple 
# de ese número.

number = int(input('Enter a number-> '))

print(f'El doble del numero {number} es ',number*2)
print(f'El doble del numero {number} es ',number*3)

# Solucion de chatgpt

numero = float(input("Ingrese un número: "))
doble = numero * 2
triple = numero * 3
print("El doble de ", numero, " es ", doble)
print("El triple de ", numero, " es ", triple)
