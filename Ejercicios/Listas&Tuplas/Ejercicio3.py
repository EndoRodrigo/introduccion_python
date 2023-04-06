# Creacion de una lista
materias = [['Matematicas',0],
           ['Fisica',0],
           ['Quimica',0],
           ['Historias',0],
           ['Lengua',0]]

# Mostrar el resultado por pamtalla
contador = 0

for mate in materias:
    
    mate[0][2] = int(input(f"Ingrese la nota final de la asignatira {mate[contador]} ->")) 
    contador = contador + 1
    print(mate)