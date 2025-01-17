import json
#funcion para guardar u7n nuevo libro
def dateBooks():
        #leer el archivo jso existente(contiene productos)
        with open('data/books.json', "r")as file:
            book = json.load(file)
        #pedir al usuario detalles
        print("Introduce los datos del nuevo libro: ")
        titulo = input("Introduce el titulo de la pelicula: ")
        autor = input("Introduce el nombre del director de la pelicula: ")
        genero = input("Introduce el genero del libro: ")
        valoracion = input("Introduce la valoracion del libro: ")
        valoracion = float(valoracion) if valoracion.strip() else None
     #crear un diccionario para la pelicula
        NewBook = {
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
              


        


# Función para agregar los datos nuevos a los datos existentes







