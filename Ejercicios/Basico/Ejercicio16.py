'''
Programa que lee una temperatura en grados centígrados y nos calcula y escribe 
su valor equivalente en grados Reamur y Kelvin.
'''

centigrados = float(input("Ingrese los grados centogrados -> "))

gradosR = 80 * centigrados / 100
gradosK = centigrados + 273

print(f"{centigrados}f °C equoivale a {gradosR} °R & a {gradosK} °K")
