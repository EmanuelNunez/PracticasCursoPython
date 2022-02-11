class Restaurante:

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio  # Private

    def mostrar_informacion(self):
        print(
            f'Nombre del Restaurante: {self.nombre}, categoria: {self.categoria}, precio: ${self.precio}')

    def get_precio(self):
        print(self.precio)

    def set_precio(self, precio):
        self.precio = precio


class Hotel(Restaurante):
    def __init__(self, nombre, categoria, precio, alberca):
        super().__init__(nombre, categoria, precio)
        self.alberca = alberca

    # Agregar un metodo solo para Hotel
    def get_alberca(self):
        return self.alberca

    # Reescribir un metodo (debe llamarse igual) es otra forma de polimorfismo
    def mostrar_informacion(self):
        print(
            f'Nombre del Restaurante: {self.nombre}, categoria: {self.categoria}, precio: ${self.precio}, alberca: {self.alberca}')


hotel = Hotel('POO H', '5 Estrellas', 200, 'Tiene alberca')
hotel.mostrar_informacion()
alberca = hotel.get_alberca()
print(alberca)
