'''
Programa Java que pide un número entero por teclado y calcula y
muestra el número de cifras que tiene.
'''

'''while True:
    numero = input("Ingrese un numero por teclado -> ")
    print(f"El numero {numero} tiene {len(numero)} cifras")
    respuesta = input("Continuar? (S/N) ->")
    if respuesta.upper() == 'N' or respuesta.upper() == 'n':
        print(respuesta)
        break'''



def calcularCifra(numero):
    cifras = 0
    while numero != 0:
       numero = numero // 10
       cifras = cifras + 1
    
    return cifras

while True:
   numero = int(input("Ingrese un numero por teclado -> "))
   cifra = calcularCifra(numero)
   print(f"El numero {numero} tiene {cifra} cifras")
   
        
        
        
