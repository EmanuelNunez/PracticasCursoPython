import os

CARPETA = 'contactos/'
EXTENCION = '.txt'


class Contacto:

    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria


def app():
    # Revisa si la carpeta existe o no
    crear_directorio()

    # Muestra menu de opciones
    mostrar_menu()

    # Preguntar al usuario la accion a realizar
    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opcion \r\n')
        opcion = int(opcion)

        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostra_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print('Opcion no valida, intenta otra vez')

def eliminar_contacto():
    nombre = input('Escribe el nombre del contacto a Eliminar \r\n')
    try:
        os.remove(CARPETA + nombre + EXTENCION)
        print('\r\nEliminado correctamnte.')
    except:
        print('No existe el contacto')
    #Reiniciar la app
    app()

def buscar_contacto():
    nombre = input('Escribe el nombre del contacto a Buscar \r\n')

    try:
        with open(CARPETA + nombre + EXTENCION) as contacto:
            print('\r\n Informacion del contacto \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')

    except IOError: 
        print('El archivo no existe. ')  
        print(IOError)
    
    #Reiniciar App
    app()

def mostra_contactos():
    archivos = os.listdir(CARPETA)
    archivos_txt = [i for i in archivos if i.endswith(EXTENCION)]
    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contactos:
            for linea in contactos:
                #Imprime los contenidos.
                print(linea.rstrip())
            #Separador entre contactos.
            print('\r\n')

def editar_contacto():

    print('Escribe el nombre del contacto a Editar:\r\n')
    nombre_anterior = input('Nombre del contacto que desea editar: \r\n')

    existe = existe_contacto(nombre_anterior)
    if existe:
            with open(CARPETA + nombre_anterior + EXTENCION, 'w') as archivo:

                # Resto de campos
                nombre_contacto = input('Agrega el nuevo Nombre :\r\n')
                telefono_contacto = input(
                'Agrega el Nuevo telefono :\r\n')
                categoria_contacto = input(
                'Agrega la Nueva categoria :\r\n')

                contacto = Contacto(
                nombre_contacto, telefono_contacto, categoria_contacto)

                # Escribir en el archivo
                archivo.write('Nombre: '+contacto.nombre + '\r')
                archivo.write('Telefono: '+contacto.telefono + '\r')
                archivo.write('Categoria: '+contacto.categoria + '\r')

            # Renombrar el archivo
            os.rename(CARPETA + nombre_anterior + EXTENCION,
                  CARPETA + nombre_contacto + EXTENCION)
                
            #Mensaje de exito
            print('Contacto editado correctamente.')
    else:
        print('No existe ese contacto')
    
    #Reiniciar aplicacion
    app()

def agregar_contacto():

    print('Escribe los datos para agregar el Nuevo Contacto')
    nombre_contacto = input('Nombre del Contacto:\r\n')

    # Revisar si el archivo ya existe
    existe = os.path.isfile(CARPETA + nombre_contacto + EXTENCION)

    if not existe:
        with open(CARPETA + nombre_contacto + EXTENCION, 'w') as archivo:
            # Resto de los campos de informacion del contacto.
            telefono_contacto = input('Agrega el telefono del contacto:\r\n')
            categoria_contacto = input('Agrega la categoria del contacto:\r\n')

            # Instaciar la clase
            contacto = Contacto(
                nombre_contacto, telefono_contacto, categoria_contacto)

            # Escrbir en el archivo
            archivo.write('Nombre: '+contacto.nombre + '\r')
            archivo.write('Telefono: '+contacto.telefono + '\r')
            archivo.write('Categoria: '+contacto.categoria + '\r')

            # Mostrar mensaje de exito
            print('\r\n Contacto guardado correctamente\r\n')
    else:
        print('Ese contacto ya existe.')
    
    #Reiniciar la App
    app()

def mostrar_menu():
    print('Seleccione del menu lo que desea hacer:')
    print('1) Agregar un Nuevo Contacto')
    print('2) Editar el Contacto')
    print('3) Ver Contactos')
    print('4) Buscar Contacto')
    print('5) Eliminar Contacto')

def crear_directorio():
    # Verificamos si la carpeta no existe y la creamos
    if not os.path.exists(CARPETA):
        os.makedirs(CARPETA)

def existe_contacto(nombre):
    # Revisar si el archivo ya existe
    return os.path.isfile(CARPETA + nombre + EXTENCION)


app()
