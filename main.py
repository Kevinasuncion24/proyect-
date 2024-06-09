from  pedido import Pedido
from estudiante import Estudiante
from libro import Libro
from docente import Docente
from revista import Revista

estudiante1 = Estudiante(cedula='0956478392', nombre='Kevin', apellido='Asuncion', email='kevin@gmail.com', telefono='0967548394', direccion='florida norte', numero_libros='2', actividad='taller')

docente1 = Docente(cedula='0956387282', nombre='Arturo', apellido='Mendoza', email='arturo@gmail.com', telefono='0923543214', direccion='aurora', numero_libros='2', actividad='taller')

libro1 = Libro(codigo= '1001', autor='Carlor',titulo='libro: el viaje 2', editorial= 'viejos' , anio= '2001' ,disponible=True, cantidad_disponible='4')

revista1 = Revista(codigo='1002',autor='Ramos',titulo='revista: viajes nuevos',anio='1999', editorial='nuevos',disponible=True,cantidad_disponible='5')

libro2 = Libro(codigo= '1003', autor='juan',titulo='libro: planeta tierra', editorial= 'antiguos' , anio= '2007' ,disponible=True, cantidad_disponible='6')

revista2 = Revista(codigo='1004',autor='angel',titulo='revista: la luna ',anio='2004', editorial='moderno',disponible=True,cantidad_disponible='7')

lista_materiales = list()
lista_materiales.append(libro1)
lista_materiales.append(revista1)

lista_materiales1 = list()
lista_materiales1.append(libro2)
lista_materiales1.append(revista2)



pedido1 = Pedido()
pedido1.pedir_material(materia ='ciencias', solicitante= docente1, lista_material = lista_materiales )
print(pedido1)
print(pedido1.mostrar_materiales())

pedido2 = Pedido()
pedido2.pedir_material(materia ='ciencias', solicitante= estudiante1, lista_material = lista_materiales1 )
print(pedido2)
print(pedido2.mostrar_materiales())
