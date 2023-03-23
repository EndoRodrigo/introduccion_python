'''
Programa Java que muestre los números del 1 al 100 utilizando la instrucción while.
'''

numero = int(input("Ingrese la cantidad de numero ->"))
contador = 1
while(contador <= numero):
    print(contador)
    contador = contador + 1
    if(contador == 101):
        break;