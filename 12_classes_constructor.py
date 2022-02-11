#La abstraccion de datos son los datos mas necesarios e importantes.
class Restaurante:
    #constructor
    #el constructor se ejecuta automaticamente
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def mostrar_informacion(self):
        print(f'Nombre del Restaurante: {self.nombre}, categoria: {self.categoria}, precio: ${self.precio}')


# Instancia de la clase
restaurante = Restaurante('Pizzeria', 'Comida Rapida', 20)
restaurante.mostrar_informacion()

restaurante2 = Restaurante('Tuva Vista', 'Platillos variados', 40)
restaurante2.mostrar_informacion()
