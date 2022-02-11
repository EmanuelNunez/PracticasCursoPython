# Getters y Setters
class Restaurante:
    # self.variable = variable -> Default public
    # self._variable = variable -> Protected
    # self.__variable = variable -> Private
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.__precio = precio  # Private

    def mostrar_informacion(self):
        print(
            f'Nombre del Restaurante: {self.nombre}, categoria: {self.categoria}, precio: ${self.__precio}')

    def get_nombre(self):
        return self.nombre

    def get_precio(self):
        print(self.__precio)

    def set_precio(self, precio):
        self.__precio = precio


# Instancia de la clase
restaurante = Restaurante('Pizzeria', 'Comida Rapida', 20)
nombre = restaurante.get_nombre()
print(f'nombre con return {nombre}')

# Aqui aun no imprime con el valor ya modificado
restaurante.mostrar_informacion()

restaurante.set_precio(90)
restaurante.get_precio()

restaurante2 = Restaurante('Tuva Vista', 'Platillos variados', 40)

restaurante2.set_precio(100)
restaurante2.get_precio()

# Aqui se imprime con el valor ya modificado osea 100
restaurante2.mostrar_informacion()
# Prestar atencion en la orden de lineas de codigo
