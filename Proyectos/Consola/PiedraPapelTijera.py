#Creacion del juego piedra papel y tijera version 2
import random

while True:
    user = int(input('''
    Selecione una opcion:
        1. Piedra
        2. Papel
        3. Tijera
        Oprima cualquier tecla para finalizar el juego
        Respuest -> '''))

    opciones = (1,2,3)

    computer = random.randint(1, 3)

    if not user in opciones: 
        print('== END GAME ==')
        break

    if user == computer:
        print(f"User -> {user} & computadora -> {computer} == EMPATE")

    if user == 1 and computer == 2:
        print(f"User -> {user} & computadora -> {computer} == GANANA LA COMPUTADORA")

    if user == 1 and computer == 3:
        print(f"User -> {user} & computadora -> {computer} == GANA EL USUARIO")

    if user == 2 and computer == 1:
        print(f"User -> {user} & computadora -> {computer} == GANANA LA COMPUTADORA")

    if user == 2 and computer == 3:
        print(f"User -> {user} & computadora -> {computer} == GANA EL USUARIO")

    if user == 3 and computer == 1:
        print(f"User -> {user} & computadora -> {computer} == GANANA LA COMPUTADORA")

    if user == 3 and computer == 2:
        print(f"User -> {user} & computadora -> {computer} == GANA EL USUARIO")


