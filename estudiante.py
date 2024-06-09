from persona import Persona

class Estudiante(Persona):

    contador_estudiante=0

    def __init__(self, cedula=None, nombre=None, apellido=None, email=None, telefono=None, direccion=None,
                 numero_libros=None, actividad=None, carrera=None, nivel=None):
        Persona.__init__(self, cedula=cedula, nombre=nombre, apellido=apellido, email=email, telefono=telefono,
                         direccion=direccion, numero_libros=numero_libros, actividad=actividad, carrera=carrera)
        self._nivel=nivel
        Estudiante.contador_estudiante +=1
        self._id = Estudiante.contador_estudiante

    @property
    def id(self):
        return self._id

    @property
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, valor):
        self._nivel = valor

    def __str__(self):
        return f'estudiante{self.__dict__}'

if __name__ == '__main__':
    e1=Estudiante(cedula='0956478392', nombre='Kevin', apellido='Asuncion', email='kevin@gmail.com', telefono='0945845983',
                  direccion='machala 123', numero_libros='20', actividad=True, carrera='administracion', nivel='medio')
    print(e1)