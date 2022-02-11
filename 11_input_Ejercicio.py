playlist = {}
playlist['canciones'] = []


def app():
    agregar_playlist = True
    while agregar_playlist:
        nombre_playlist = input('Como se va a llamar la playlist?\r\n')
        if nombre_playlist:
            playlist['nombre'] = nombre_playlist
            # Ya tenemos nombre, se desactiva el True
            agregar_playlist = False

            # LLamando a la funcion agregar canciones
            agregar_canciones()


def agregar_canciones():
    # Bandera para agregar canciones
    agregar_cancion = True
    while agregar_cancion:
        nombre_playlist = playlist['nombre']
        pregunta = f'Agrega canciones para la playlist {nombre_playlist}: \r\n'
        pregunta += 'Escribe "X" para dejar de agregar canciones \r\n'
        cancion = input(pregunta)
        if cancion == 'X':
            agregar_cancion = False
            # Mostrar resumen de la playlist
            mostrar_resumen()
        else:
            playlist['canciones'].append(cancion)


def mostrar_resumen():
    nombre_playlist = playlist['nombre']
    print(f'Playlist: {nombre_playlist}\r\n')
    print('Canciones: \r\n')
    for cancion in playlist['canciones']:
        print(cancion)


app()

# Nota y consejo, es importante probar el codigo conforme agregas mas codigo o funciones.
