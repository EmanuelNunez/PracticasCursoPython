class Restaurante:
    #self.variable = variable -> Default public
    #self._variable = variable -> Protected
    #self.__variable = variable -> Private
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre 
        self.categoria = categoria
        self.__precio = precio #Private

    def mostrar_informacion(self):
        print(f'Nombre del Restaurante: {self.nombre}, categoria: {self.categoria}, precio: ${self.__precio}')


# Instancia de la clase
restaurante = Restaurante('Pizzeria', 'Comida Rapida', 20)
restaurante.__precio = 80 #No sera posible modificarse con private
restaurante.mostrar_informacion()

restaurante2 = Restaurante('Tuva Vista', 'Platillos variados', 40)
restaurante.__precio = 100 #No sera posible modificarse con private
restaurante2.mostrar_informacion()