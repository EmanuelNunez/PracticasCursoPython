# Iniciando un diccionario vacio
jugador = {}
print(jugador)

# Se une un jugador
jugador['nombre'] = 'Emanuel'
jugador['puntaje'] = 0
print(jugador)

#Incrementado el puntaje
jugador['puntaje'] = 100
print(jugador)

jugador['puntaje'] = 400
print(jugador)

#Acceder a un valor
print(jugador.get('consola', 'No existe ese valor.'))

#Iterar en el diccionario
for llave, valor in jugador.items():
    print(valor)

#Eliminar el jugador
del jugador['nombre']
del jugador['puntaje']
print(jugador)