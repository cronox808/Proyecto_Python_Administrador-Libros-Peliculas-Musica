
import json
#funcion para guardar u7n nuevo libro
def dateBooks():
        #leer el archivo jso existente(contiene productos)
        with open('data/books.json', "r")as file:
           book = json.load(file)
        #pedir al usuario detalles
        print("Introduce los datos del nuevo libro: ")
        titulo = input("Introduce el titulo del libro: ")
        autor = input("Introduce el nombre del autor: ")
        genero = input("Introduce el genero del libro: ")
        valoracion = input("Introduce la valoracion del libro: ")
        valoracion = float(valoracion) if valoracion.strip() else None

# Determinar el próximo ID (si la lista de libros no está vacía, obtenemos el último ID)ç
        next_id = book[-1]['id'] + 1 if book else 1 

     #crear un diccionario para la pelicula
        NewBook = {
        "id": next_id,
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "valoracion": valoracion
        }
        #agregar el nuevo item(libro) a la lista de book
        book.append(NewBook)
        #guardar los cambieo en el archivo JSON
        with open('data/books.json', 'w') as file:
              str(book).encode('utf-8')
              comvertjson = json.dumps(book, indent=4, ensure_ascii = False)
              file.write(comvertjson)
        print("libro agregado exitosamente")
              


#funcion para guardar u7n nuevo libro
def dateMovies():
        #leer el archivo jso existente(contiene productos)
        with open('data/movies.json', "r")as file:
            movie = json.load(file)
        #pedir al usuario detalles
        print("Introduce los datos de la nueva pelicula: ")
        titulo = input("Introduce el titulo de la pelicula: ")
        director = input("Introduce el nombre del director de la pelicula: ")
        genero = input("Introduce el genero de la pelicula: ")
        valoracion = input("Introduce la valoracion de la pelicula: ")
        valoracion = float(valoracion) if valoracion.strip() else None
        next_id = movie[-1]['id'] + 1 if movie else 1 
     #crear un diccionario para la pelicula
        NewMovie = {
        "id": next_id,
        "titulo": titulo,
        "director": director,
        "genero": genero,
        "valoracion": valoracion
        }
        #agregar el nuevo item(libro) a la lista de book
        movie.append(NewMovie)
        #guardar los cambieo en el archivo JSON
        with open('data/movies.json', 'w') as file:
              str(movie).encode('utf-8')
              comvertjson = json.dumps(movie, indent=4, ensure_ascii = False)
              file.write(comvertjson)
        print("libro agregado exitosamente")
        


def dateMusic():
        #leer el archivo jso existente(contiene productos)
        with open('data/musics.json', "r")as file:
            music = json.load(file)
        #pedir al usuario detalles
        print("Introduce los datos de la nueva cancion: ")
        titulo = input("Introduce el titulo de la cancion: ")
        artista = input("Introduce el nombre del artista: ")
        genero = input("Introduce el genero de la cancion: ")
        valoracion = input("Introduce la valoracion de la cancion: ")
        valoracion = float(valoracion) if valoracion.strip() else None
        next_id = music[-1]['id'] + 1 if music else 1 
     #crear un diccionario para la pelicula
        NewMusic = {
        "id": next_id,
        "titulo": titulo,
        "artista": artista,
        "genero": genero,
        "valoracion": valoracion
        }
        #agregar el nuevo item(libro) a la lista de book
        music.append(NewMusic)
        #guardar los cambieo en el archivo JSON
        with open('data/musics.json', 'w') as file:
              str(music).encode('utf-8')
              comvertjson = json.dumps(music, indent=4, ensure_ascii = False)
              file.write(comvertjson)
        print("libro agregado exitosamente")
        






