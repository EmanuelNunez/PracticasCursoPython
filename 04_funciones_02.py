# definiremos una funcion con parametros
# Esta es una funcion con parametros

def informacion(nombre, puesto='Desconocino'):
    # Si es usuario no agrega un puesto el valor por defecto sera "Desconocido".
    # Importante poner la f en el print cuando pasamos parametros...
    # y los usamos de esta forma.
    print(f'Hola soy {nombre}, y mi puesto actual es: {puesto}')


informacion('Emanuel', 'Programador fullstack')
informacion('Lucero', 'Abogada')
informacion('Aldo', 'Negocios')
informacion('Alan')
