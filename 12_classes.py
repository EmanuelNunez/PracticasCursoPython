#Siempre el nombre de la clase comienza con MAYUSCULAS
class Restaurante:
    def agregar_restaurante(self, nombre):
        self.nombre = nombre  # Atributo
        #self es una forma de referirse al mismo objeto
    def mostrar_informacion(self):
        print(f'Nombre del Restaurante: {self.nombre}')


# Instancia de la clase
restaurante = Restaurante()
restaurante.agregar_restaurante('Pizzeria')
restaurante.mostrar_informacion()

restaurante2 = Restaurante()
restaurante.agregar_restaurante('Calle 14')
restaurante.mostrar_informacion()

print(restaurante)
