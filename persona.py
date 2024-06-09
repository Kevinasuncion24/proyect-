class Persona:
    def __init__(self, cedula=None, nombre=None, apellido=None, email=None, telefono=None,
                 direccion=None, numero_libros=None, actividad=None, carrera=None):
        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._telefono = telefono
        self._direccion = direccion
        self._numero_libros = numero_libros
        self._actividad = actividad
        self._carrera = carrera

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, telefono):
        self._telefono = telefono

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, direccion):
        self._direccion = direccion

    @property
    def numero_libros(self):
        return self._numero_libros

    @numero_libros.setter
    def numero_libros(self, numero_libros):
        self._numero_libros = numero_libros

    @property
    def actividad(self):
        return self._actividad

    @actividad.setter
    def actividad(self, actividad):
        self._actividad = actividad

    @property
    def carrera(self):
        return self._carrera

    @carrera.setter
    def carrera(self, carrera):
        self._carrera = carrera

    def __str__(self):
        return f'persona{self.__dict__}'

if __name__=='__main__':
    p1=Persona(cedula=2987659503, nombre='kevin', apellido='Asuncion', email='kevin.paul@gmail.com', telefono='593965748392',
               direccion='florida', numero_libros=14, actividad=True, carrera='administracion')
    print(p1)