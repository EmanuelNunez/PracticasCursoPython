cancion = {
    'artista': 'Post Malone',
    'cancion': 'Circles',
    'album': 'Hollywoods Bleeding',
    'likes': 120000,
    'Disponible': True
}

# Imprimiendo el objeto cancion.
print(cancion)

# Accediendo a los eleentes del diccionario.
print(cancion['artista'])

# Mezclar con strings
artista = cancion['artista']
print(f'Estoy escuchando a {artista}')

# Agregar nuevos valores
cancion['playlist'] = 'Heavy Metal'
print(cancion)

#Reemplazar valor existente
cancion['cancion'] = 'Feel'
print(cancion)

del cancion['Disponible']
print(cancion)