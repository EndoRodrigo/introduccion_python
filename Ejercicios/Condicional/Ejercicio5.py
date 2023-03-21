'''
Programa que lea dos caracteres y compruebe si los dos son letras minúsculas
'''
caracter_1 = input("Ingrese un caractres -> ")
caracter_2 = input("Ingrese un segundo caracter ->")

if(caracter_1.islower()):
    if(caracter_2.islower()):
        print("Los dos cacarcteres ingresados son minusculas")
    else:
        print("La primera letra es miniscula la segunda no")
elif(caracter_2.islower()):
    print("La segunda letra es miniscula la primera no no")
else:
    print("Ninguno es una letra minúscula")
