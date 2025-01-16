import json
# Ruta al archivo JSON (modifica según la ubicación del archivo)
ruta_archivo = "data/movies.json"
#cargar el json existente
with open(ruta_archivo, "r")as archivo:
    movies_json = json.load(archivo)

#Funcion para añadir un nuevo libro
def addNewMovie(movies_json, ruta_archivo):
    print("Introduce los datos del nuevo libro: ")
    titulo = input("Introduce el titulo de la pelicula: ")
    director = input("Introduce el nombre del director de la pelicula: ")
    genero = input("Introduce el genero del libro: ")
    valoracion = input("Introduce la valoracion del libro: ")

    #manejar de valoracion (comvertir a float si es neceasiro por numero decimal en la valoracion del libro)
    valoracion = float(valoracion) if valoracion.strip() else None

    #crear un diccionario para la pelicula
    NewMovie = {
        "titulo": titulo,
        "director": director,
        "genero": genero,
        "valoracion": valoracion
    }

    # Añadir al JSON
    movies_json["libros"].append(NewBook)
    print("\nPeliculas añadidas con éxito.")

    #Guardar el JSON actulizado en el archivo
    with open(ruta_archivo, "w") as archivo:
        json.dump(movies_json, archivo, indet=4)
    print(f"JSON actualizado guardado en '{ruta_archivo}'.")

#Llamar a la funcion para añadir el libro
addNewMovie(movies_json, ruta_archivo)