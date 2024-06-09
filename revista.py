from material import Material

class Revista(Material):

    contador_revista=0

    def __init__(self,codigo=None, autor=None, titulo=None, anio=1000,
                 editorial= None, disponible= True, cantidad_disponible = 0,contenido=None):
       Material.__init__(self,codigo = codigo, autor = autor, titulo = titulo, anio = anio,
                          editorial = editorial, disponible= disponible,cantidad_disponible=cantidad_disponible)


       Revista.contador_revista += 1
       self._id = Revista.contador_revista

       self._contenido = contenido

    @property
    def id(self):
        return self._id



    @property
    def contenido(self):
        return self._contenido

    @contenido.setter
    def contenido(self, contenido):
        self._contenido = contenido




    def __str__(self):
        return f'Libro:{self.__dict__}'
    
if __name__=='__main__':
    R1= Revista(codigo='123',autor='QW',titulo='TIO',anio=4567,editorial='BABEL',disponible=True,cantidad_disponible=5, contenido='informativa')
    print(R1)
