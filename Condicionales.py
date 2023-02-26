# syntax
'''if condition:
    this part of code runs for truthy conditions'''

a = -0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')


a = -3
print('A is positive') if a > 0 else print('A is negative') # first condition met, 'A is positive' will be printed

a = 4
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')