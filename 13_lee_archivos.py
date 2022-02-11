def app():
    #Para leer un archivo
    with open('archivo.txt') as archivo:
        for contenido in archivo:
            print(contenido)

app()