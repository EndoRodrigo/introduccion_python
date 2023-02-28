'''
# Syntax
open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update
'''

f = open('.//reading_file_example.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()

print()

f = open('.//reading_file_example.txt')
txt = f.read(10)
print(type(txt))
print(txt)
f.close()

print()

f = open('.//reading_file_example.txt')
line = f.readline()
print(type(line))
print(line)
f.close()

print()
f = open('.//reading_file_example.txt')
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()

print()
with open('.//reading_file_example.txt','a') as f:
    f.write('This text has to be appended at the end')


'''
import os
if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('The file does not exist')
'''

print()

import json
# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# let's change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])


print()
import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# let's convert it to  json
person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
print(type(person_json))
print(person_json)

print()
import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
with open('.//json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)


print()

import csv
with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')

print()

import xlrd
excel_book = xlrd.open_workbook('sample.xls)
print(excel_book.nsheets)
print(excel_book.sheet_names)


print()

import xml.etree.ElementTree as ET
tree = ET.parse('./files/xml_example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)