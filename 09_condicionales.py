balance = 800
monto = 700

if balance > 0:
    print('Puedes pagar...')
else:
    print('No tienes el saldo suficiente...')

if balance >= monto:
    print('Pago realizado exitosamente...')
else:
    print('No tienes el saldo suficiente...')

# Un if anidado
usuario_autenticado = True
usuario_admin = True

if usuario_autenticado:
    if usuario_admin:
        print('Acceso total al sistema')
    else:
        print('Acceso solo al sistema')

color_favorito = 'Azul'

if color_favorito == 'Rojo':
    print('Rojo es mi color favorito...')
elif color_favorito == 'Negro':
    print('Negro es mi color favorito...')
elif color_favorito == 'Azul':
    print('Azul es mi color favorito...')
else:
    print('No esta en mi lista de colores favoritos...')
