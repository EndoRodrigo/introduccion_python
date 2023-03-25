#Exportando informacion de una clase externa
from Empleado import *

#Declracion de variables
operacion = 1
opcion = 1
empleado = []
customer = Empleado()


# bucle para simepre me mueste el menu
while operacion != 0:
    print('''
    == BIENVENIDO A LA CAJA ==
    1. Iniciar Sesion
    0. Salir

    ''')

    operacion = int(input("Ingrese el numero de la opcion -> "))
    cedula = int(input("Ingrese su codigo de cajero -> "))

    
    empleado = customer.validarUsuario(cedula)
    
    if empleado != []:
        while opcion != 0:
            print(f'''
            Bienvenido señor(@) {empleado[1]}
            ''')
            opcion = int(input("Ingrese el numero de la opcion -> "))
    