usuario_logueado = True
usuario_admin = True

if usuario_logueado and usuario_admin:
    print('Administrador')
elif usuario_logueado:
    print('Acceso al sistema')
else:
    print('Debes Iniciar sesion')

print('------------')

usuario_logueado_1 = True
usuario_admin_1 = False

# El programa evaluara la primera condicion verdadera que encuentre.

if usuario_logueado_1 and usuario_admin_1:
    print('Administrador')
elif usuario_logueado_1:#imprime esta condicion
    print('Acceso al sistema')
else:
    print('Debes Iniciar sesion')
