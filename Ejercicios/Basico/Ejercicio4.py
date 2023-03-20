# Ejercicio 4: Programa que lea una cantidad de grados centígrados y la pase a grados Fahrenheit.
#La fórmula correspondiente para pasar de grados centígrados a fahrenheit es:
# F = 32 + ( 9 * C / 5)

centogrados = int(input('Ingresos ev valor en centogrados -> '))
grados_f = 32 + (9 * centogrados /5)
print(f'{centogrados} °C es igual a {grados_f} °F')

#32solucion de chatgpt

celsius = float(input("Introduce la temperatura en grados Celsius: "))
fahrenheit = (celsius * 1.8) + 32
print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")
