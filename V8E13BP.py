class Alumno:
    def __init__(self,num_control, nombre, semestre, grupo):
     self.num_control = num_control
     self.nombre = nombre
     self.semestre = semestre
     self.grupo = grupo
    

alumno1 = Alumno (123455, "Tomas",3,"B")

print(alumno1.nombre)