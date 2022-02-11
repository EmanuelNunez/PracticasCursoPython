lenguajes = ['Python', 'Kotlin', 'Java', 'Javascript']

lenguajes.sort()  # Ordena elementos
print(lenguajes)

aprendiendo = f'Estoy aprendiendo {lenguajes[3]}'
print(aprendiendo)

# Modificar valores de un list (arreglo)
lenguajes[2] = 'PHP'
print(lenguajes)

# Agregar nuevos valores a un list
lenguajes.append('Ruby')
print(lenguajes)

#eliminar de un list (arreglo)
del lenguajes[1]
print(lenguajes)

#eliminar de un list (arreglo) con pop()
lenguajes.pop()
print(lenguajes)

#eliminar de un list (arreglo) con pop() con una posicion en especifico
lenguajes.pop(0)
print(lenguajes)

#eliminar por nombre
lenguajes.remove('PHP')
print(lenguajes)

