#import json
def addNewBook(book_json, ruta_archivo):
    print("Introduce los datos del nuevo libro: ")
    titulo = input("Introduce el titulo del nuevo libro: ")
    autor = input("Introduce el nombre del autor del libro: ")
    genero = input("Introduce el genero del libro: ")
    valoracion = input("Introduce la valoracion del libro: ")

    #manejar de valoracion (comvertir a float si es neceasiro por numero decimal en la valoracion del libro)
    valoracion = float(valoracion) if valoracion.strip() else None

    #crear un diccionario para la pelicula
    NewBook = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "valoracion": valoracion
    }

    