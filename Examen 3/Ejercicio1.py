def palabraLarga(archivo):
    try:
        with open(archivo, 'r') as f:
            palabras = f.read().split()

        if not palabras:
            print("El archivo está vacío.")
            return

        palabrasLongitud = {}
        maxLargo = 0

        for palabra in palabras:
            longitud = len(palabra)
            maxLargo = max(maxLargo, longitud)

            if longitud in palabrasLongitud:
                palabrasLongitud[longitud].append(palabra)
            else:
                palabrasLongitud[longitud] = [palabra]

        palabrasLargas = palabrasLongitud[maxLargo]

        if len(palabrasLargas) == 1:
            print(f"Palabra más larga: {palabrasLargas[0]}")
        else:
            print(f"Palabras más largas ({maxLargo} caracteres) y su frecuencia:")
            for palabra in set(palabrasLargas):
                frecuencia = palabrasLargas.count(palabra)
                print(f"{palabra}: {frecuencia} veces")

    except FileNotFoundError:
        print("El archivo no fue encontrado.")

palabraLarga('Ejercicio1.txt')
