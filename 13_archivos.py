def app():
    # Crear el archivo
    # w es escritura, si n o existe lo creara
    archivo = open('archivo.txt', 'w')

    # Generar numero en archivo
    for i in range(0, 20):
        archivo.write('Esta es la linea ' +str(i)+"\n")

    archivo.close()

app()
