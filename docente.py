from persona import Persona

class Docente(Persona):

    contador_docente=0

    def __init__(self, cedula=None, nombre=None, apellido=None, email=None, telefono=None, direccion=None,
                 numero_libros=None, actividad=None, carrera=None, titulo3ernivel=None, titulo4tonivel=None, nivel=None):
        Persona.__init__(self, cedula=cedula, nombre=nombre, apellido=apellido, email=email, telefono=telefono,
                         direccion=direccion, numero_libros=numero_libros, actividad=actividad, carrera=carrera)

        self._titulo3ernivel = titulo3ernivel
        self._titulo4tonivel = titulo4tonivel
        Docente.contador_docente += 1
        self._id = Docente.contador_docente

        @property
        def id(self):
            return self._id

        @property
        def titulo3ernivel(self):
            return self._titulo3ernivel

        @titulo3ernivel.setter
        def nivel(self, valor):
            self._titulo3ernivel = valor

        @property
        def titulo4tonivel(self):
            return self._titulo4tonivel

        @titulo4tonivel.setter
        def titulo4tonivel(self,valor):
            self._titulo4tonivel = valor

        def __str__(self):
            return f'Docente{self.__dict__}'

if __name__ == '__main__':
            d1=Docente(cedula='0956387282', nombre='Arturo', apellido='Mendoza', email='arturo@gmail.com', telefono='0967543214', direccion='samanes',
                 numero_libros='12', actividad=True, carrera='administracion', titulo3ernivel='ingeniero en sistema', titulo4tonivel='maestria')
            print(d1)