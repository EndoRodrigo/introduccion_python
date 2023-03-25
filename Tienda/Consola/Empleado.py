class Empleado:


    def __init__(self):
        pass

    

    def validarUsuario(self,cedula):
        empleados = [1011,'Andrea','Empleada','andrea@gm.com']
        lista = []
        if cedula in empleados:
            return empleados
        else:
            return lista