#Creacion del juego piedra papel y tijera version 1

user = int(input('''
Selecione una opcion:
    1. Piedra
    2. Papel
    3. Tijera
    Respuest -> '''))

for computer in range(1,3):
    continue


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


