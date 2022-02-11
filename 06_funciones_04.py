def mensajeBienvenida():
    print('Hola bienvenido a este curso.'.upper())


def bienvenidaUsuario(nombre):
    print(f'Hola {nombre}, esperamos disfrutes este curso.')


def actividades(actividad):
    return f'My ultima actividad fue {actividad}'
#Se usa la f para poder concatenar la palabra pasado por parametro. En este caso {actividad}


mensajeBienvenida()
bienvenidaUsuario('Emanuel')
print(actividades('Salir a caminar'))
