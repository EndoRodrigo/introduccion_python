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
print(person['first_name']) # Asabeneh
print(person['country'])    # Finland
print(person['skills'])     # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street']) # Space street
#print(person['city'])       # Error

print(person.get('first_name')) # Asabeneh
print(person.get('country'))    # Finland
print(person.get('skills')) #['HTML','CSS','JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))   # None

person['job_title'] = 'Instructor'
person['skills'].append('HTML')

person['first_name'] = 'Eyob'
person['age'] = 252

#person.pop('first_name')        # Removes the firstname item
#person.popitem()                # Removes the address item
#del person['is_married']        # Removes the is_married item

keys = person.keys()
values = person.values()
print(keys)
print(values)

#print(person)