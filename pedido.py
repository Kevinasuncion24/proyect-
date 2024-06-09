from datetime import datetime, timedelta
from estudiante import Estudiante
from libro import Libro
from revista import Revista
from docente import Docente

class Pedido:
    contador_pedido = 0

    def __init__(self, materia=None, solicitante=None):
        Pedido.contador_pedido += 1
        self._id = Pedido.contador_pedido
        self._solicitante = solicitante
        self._lista_material = list()
        self._materia = materia
        self._fecha_prestamo = datetime.now()
        td = timedelta(days= 5)
        self._fecha_devolucion = self._fecha_prestamo + td

    @property
    def id(self):
        return self._id

    @property
    def materia(self):
        return self._materia
    @materia.setter
    def materia(self, valor):
        self._materia = valor

    @property
    def fecha_prestamo(self):
        return self._fecha_prestamo

    @property
    def fecha_devolucion(self):
        return self._fecha_devolucion

    @property
    def solicitante(self):
        return self._solicitante



    def pedir_material(self, materia, solicitante, lista_material):
        self._materia = materia
        self._solicitante = solicitante
        self._lista_material = lista_material


    def mostrar_materiales(self):
        for material in self._lista_material:
            print(f'\nTitulo: {material.titulo},     autor: {material.autor},     año: {material.anio},     \ncodigo: {material.codigo}, '
                  f'     editorial: {material.editorial},    disponible: {material.disponible},    \ncantidad disponible: {material.cantidad_disponible}')



    def __str__(self):
        return (f'pedido\n\n'
                f'\tid: {self.id}\n'
                f'\tmateria:{self.materia}\n'
                f'fecha pedido:{self._fecha_prestamo}\n'
                f'fecha de devolucion: {self._fecha_devolucion}\n\n'
                f'datos del solicitante:\n\n'
                f'cedula:\t{self._solicitante.cedula}\t'
                f'nombre:\t{self._solicitante.nombre}\t'
                f'apellido:\t{self._solicitante.apellido}\t'
                f'email:\t{self._solicitante.email}\t\n'
                f'telefono:\t{self.solicitante.telefono}\t'
                f'direccion:\t{self.solicitante.direccion}\t'
                f'numero de libros:\t{self._solicitante.numero_libros}\t'
                f'actividad:\t{self._solicitante.actividad}')


# En la carpeta main es donde vamos imprimir los resultados.
if __name__ == '__main__':
    pass
