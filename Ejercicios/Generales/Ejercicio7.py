'''
 * Serie de Fibonacci
 * Programa que imprima los N primeros números de la serie de Fibonacci.
 * El primer número de la serie es 1, el segundo número es 1 y cada uno de los                                    
 * siguientes es la suma de los dos anteriores.
 * 1, 1, 2, 3, 5, 8, 13,  ....... , N
'''
fibo_1 = 1
fibo_2 = 1

print(fibo_1)

for number in range(1, 20):
    print(fibo_2)
    fibo_2 = fibo_1 + fibo_2
    fibo_1 = fibo_2 - fibo_1

