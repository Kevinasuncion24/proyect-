from material import Material

class Libro(Material):
    contador_libro = 0

    def __init__(self,codigo=None, autor=None, titulo=None, anio=1000,
                 editorial= None, disponible= True, cantidad_disponible = 0, tipo_pasta=None):
        Material.__init__(self, codigo = codigo, autor = autor, titulo = titulo, anio = anio,
                          editorial = editorial, disponible= disponible, cantidad_disponible=cantidad_disponible)

        Libro.contador_libro += 1
        self._id = Libro.contador_libro

        self._tipo_pasta = tipo_pasta


    @property
    def id(self):
        return self._id


    @property
    def tipo_pasta(self):
        return self._tipo_pasta

    @tipo_pasta.setter
    def tipo_pasta(self, tipo_pasta):
        self._tipo_pasta = tipo_pasta

    def __str__(self):
        return f'Libro: {self.__dict__}'

    def actualizar_disponible(self, disponible):
        self.disponible = disponible

if __name__=='__main__':
    L1= Libro(codigo= 432, autor='MN',titulo='primer', editorial= 'paco' , anio= 2014 ,disponible=True, cantidad_disponible=4,tipo_pasta='gruesa')
    print(L1)