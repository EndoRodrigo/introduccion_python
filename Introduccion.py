#Numeros

numero1 = 17
numero2 = 3
print(numero1 + numero2)
print(numero1 - numero2)
print(numero1 * numero2)
print(numero1 / numero2) #Siempre devuleve un numero flotante
print(numero1 // numero2) #Alternativa para el resultado sea entero
print(numero1 % numero2) # devuelve el residuo de la operacion

# Cadenas

texto1 = "Hola mundo como estas"
texto2 = 'Endo Rodrigo Rodrigureez'

print(f'Verificacion de los textos {texto1} - {texto2}')

indece = 'Python'
print(indece[0])
print(indece[-1])

#List

squares = [1,4,9,16,25]

#Forma de obtener valores de las listas
print(squares[0])
print(squares[-1])
print(squares[-3:])

squares.append(99)
print(squares)

#Incio de una serie fibinachi

a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b



