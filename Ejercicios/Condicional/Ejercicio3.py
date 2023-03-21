'''
Programa que lea un carácter por teclado y compruebe si es una letra mayúscula
'''

letra = input("Ingrese una letras -> ")

'''if(letra.isupper()):
    print(f"La lesta {letra} es mayuscula")
else:
    print(f"La letra {letra} es minuscula")'''

if(letra>='A' and letra <='Z'):
    print(f"La lesta {letra} es mayuscula")
else:
    print(f"La letra {letra} es minuscula")

print(letra>='A')
print(letra <='Z')