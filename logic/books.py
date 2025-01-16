import json
# Ruta al archivo JSON (modifica según la ubicación del archivo)
ruta_archivo = "data/books.json"
#cargar el json existente
with open(ruta_archivo, "r")as archivo:
    books_json = json.load(archivo)

#Funcion para añadir un nuevo libro
def addNewBook(books_json, ruta_archivo):
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

    # Añadir al JSON
    books_json["libros"].append(NewBook)
    print("\nPeliculas añadidas con éxito.")

    #Guardar el JSON actulizado en el archivo
    with open(ruta_archivo, "w") as archivo:
        json.dump(books_json, archivo, indet=4)
    print(f"JSON actualizado guardado en '{ruta_archivo}'.")

#Llamar a la funcion para añadir el libro
addNewBook(books_json, ruta_archivo)
