class Restaurante:

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.__precio = precio  # Private

    def mostrar_informacion(self):
        print(
            f'Nombre del Restaurante: {self.nombre}, categoria: {self.categoria}, precio: ${self.__precio}')

    def get_precio(self):
        print(self.__precio)

    def set_precio(self, precio):
        self.__precio = precio

#Heredando de la clase restaurante
#Con la herencia heredamos todos los metodos del padre al hijo
class Hotel(Restaurante):
    def __init__(self, nombre, categoria, precio):
        #Super hace referencia al constructor de la clase padre.
        super().__init__(nombre, categoria, precio)

hotel = Hotel('POO H', '5 Estrellas', 200)
hotel.mostrar_informacion()