def leerArchivo(nombreArchivo):
    try:
        with open(nombreArchivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            return contenido
    except FileNotFoundError:
        return None

def compararArchivos(archivo1, archivo2):
    contenido1 = leerArchivo(archivo1)
    contenido2 = leerArchivo(archivo2)

    if contenido1 is None or contenido2 is None:
        return "Error: Al menos uno de los archivos no existe."

    if contenido1 == contenido2:
        return "Los archivos son idénticos."
    else:
        return "Los archivos no son idénticos."

prueba1 = "Ejercicio2.1.txt"
prueba2 = "Ejercicio2.2.txt"

resultado = compararArchivos(prueba1, prueba2)
print(resultado)
 