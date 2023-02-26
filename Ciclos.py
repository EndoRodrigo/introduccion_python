# syntax
'''while condition:
    code goes here

count = 3
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)


count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

count = 0
while count < 5:
    if count == 3:
        continue
    print(count)
    count = count + 1'''

numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5


language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])

print('')

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

print()
for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out