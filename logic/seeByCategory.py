import json
import os
from tabulate import tabulate

# Ruta de la carpeta donde se encuentran los archivos
folder_path = 'data'

# Función para mostrar los libros por una categoría específica
def mostrar_libros_por_categoria():
    # Preguntar al usuario qué categoría desea filtrar
    print("Seleccione la categoría por la cual desea filtrar los libros:")
    print("1. Género")
    print("2. Autor")
    
    try:
        opcion = int(input("Ingrese el número correspondiente (1 o 2): "))
    except ValueError:
        print("Por favor, ingresa un número válido para la opción.")
        return

    # Definir el campo según la opción seleccionada
    if opcion == 1:
        categoria = "genero"
        categoria_nombre = "Género"
    elif opcion == 2:
        categoria = "autor"
        categoria_nombre = "Autor"
    else:
        print("Opción no válida. Por favor, elige 1 o 2.")
        return

    # Pedir al usuario el valor de la categoría
    valor_categoria = input(f"Introduce el {categoria_nombre} por el cual deseas filtrar: ").strip()

    # Cargar los datos de los libros
    archivo_path = os.path.join(folder_path, 'books.json')
    
    # Verificar si el archivo existe
    if not os.path.exists(archivo_path):
        print(f"El archivo books.json no existe.")
        return

    # Cargar los datos del archivo
    with open(archivo_path, 'r', encoding='utf-8') as file:
        datos = json.load(file)
    
    # Filtrar los libros por la categoría especificada
    libros_filtrados = [libro for libro in datos if libro.get(categoria, '').lower() == valor_categoria.lower()]
    
    # Si no se encontraron libros, mostrar mensaje
    if not libros_filtrados:
        print(f"No se encontraron libros con el {categoria_nombre} '{valor_categoria}'.")
        return
    
    # Mostrar los libros filtrados usando tabulate
    print(f"\nLibros con {categoria_nombre} '{valor_categoria}':")
    tabla = []
    for libro in libros_filtrados:
        fila = [libro['id'], libro['titulo'], libro['autor'], libro['genero'], libro['valoracion']]
        tabla.append(fila)

    # Encabezados de la tabla
    headers = ["ID", "Título", "Autor", "Género", "Valoración"]
    print(tabulate(tabla, headers=headers, tablefmt="grid"))

# Función para mostrar las películas por una categoría específica
def mostrar_peliculas_por_categoria():
    # Preguntar al usuario qué categoría desea filtrar
    print("Seleccione la categoría por la cual desea filtrar las películas:")
    print("1. Género")
    print("2. Director")
    
    try:
        opcion = int(input("Ingrese el número correspondiente (1 o 2): "))
    except ValueError:
        print("Por favor, ingresa un número válido para la opción.")
        return

    # Definir el campo según la opción seleccionada
    if opcion == 1:
        categoria = "genero"
        categoria_nombre = "Género"
    elif opcion == 2:
        categoria = "director"
        categoria_nombre = "Director"
    else:
        print("Opción no válida. Por favor, elige 1 o 2.")
        return

    # Pedir al usuario el valor de la categoría
    valor_categoria = input(f"Introduce el {categoria_nombre} por el cual deseas filtrar: ").strip()

    # Cargar los datos de las películas
    archivo_path = os.path.join(folder_path, 'movies.json')
    
    # Verificar si el archivo existe
    if not os.path.exists(archivo_path):
        print(f"El archivo movies.json no existe.")
        return

    # Cargar los datos del archivo
    with open(archivo_path, 'r', encoding='utf-8') as file:
        datos = json.load(file)
    
    # Filtrar las películas por la categoría especificada
    peliculas_filtradas = [pelicula for pelicula in datos if pelicula.get(categoria, '').lower() == valor_categoria.lower()]
    
    # Si no se encontraron películas, mostrar mensaje
    if not peliculas_filtradas:
        print(f"No se encontraron películas con el {categoria_nombre} '{valor_categoria}'.")
        return
    
    # Mostrar las películas filtradas usando tabulate
    print(f"\nPelículas con {categoria_nombre} '{valor_categoria}':")
    tabla = []
    for pelicula in peliculas_filtradas:
        fila = [pelicula['id'], pelicula['titulo'], pelicula['director'], pelicula['genero'], pelicula['valoracion']]
        tabla.append(fila)

    # Encabezados de la tabla
    headers = ["ID", "Título", "Director", "Género", "Valoración"]
    print(tabulate(tabla, headers=headers, tablefmt="grid"))

def mostrar_musica_por_categoria():
    # Preguntar al usuario qué categoría desea filtrar
    print("Seleccione la categoría por la cual desea filtrar la música:")
    print("1. Género")
    print("2. Artista")
    
    try:
        opcion = int(input("Ingrese el número correspondiente (1 o 2): "))
    except ValueError:
        print("Por favor, ingresa un número válido para la opción.")
        return

    # Definir el campo según la opción seleccionada
    if opcion == 1:
        categoria = "genero"
        categoria_nombre = "Género"
    elif opcion == 2:
        categoria = "artista"
        categoria_nombre = "Artista"
    else:
        print("Opción no válida. Por favor, elige 1 o 2.")
        return

    # Pedir al usuario el valor de la categoría
    valor_categoria = input(f"Introduce el {categoria_nombre} por el cual deseas filtrar: ").strip()

    # Cargar los datos de la música
    archivo_path = os.path.join(folder_path, 'musics.json')
    
    # Verificar si el archivo existe
    if not os.path.exists(archivo_path):
        print(f"El archivo musics.json no existe.")
        return

    # Cargar los datos del archivo
    with open(archivo_path, 'r', encoding='utf-8') as file:
        datos = json.load(file)
    
    # Filtrar la música por la categoría especificada
    musica_filtrada = [musica for musica in datos if musica.get(categoria, '').lower() == valor_categoria.lower()]
    
    # Si no se encontraron música, mostrar mensaje
    if not musica_filtrada:
        print(f"No se encontraron música con el {categoria_nombre} '{valor_categoria}'.")
        return
    
    # Mostrar la música filtrada usando tabulate
    print(f"\nMúsica con {categoria_nombre} '{valor_categoria}':")
    tabla = []
    for musica in musica_filtrada:
        fila = [musica['id'], musica['titulo'], musica['artista'], musica['genero'], musica['valoracion']]
        tabla.append(fila)

    # Encabezados de la tabla
    headers = ["ID", "Título", "Artista", "Género", "Valoración"]
    print(tabulate(tabla, headers=headers, tablefmt="grid"))