import json
import os
from tabulate import tabulate
def deletBooks():
    while True:
    # Leer los tres archivos
        books = json.load(open(os.path.join('data', 'books.json'), "r", encoding="utf-8"))
        movies = json.load(open(os.path.join('data', 'movies.json'), "r", encoding="utf-8"))
        music = json.load(open(os.path.join('data', 'musics.json'), "r", encoding="utf-8"))

        # Crear una lista combinada de títulos con su fuente (libros, películas, música)
        todos_los_titulos = []
        for item in books:
            todos_los_titulos.append({"titulo": item["titulo"], "origen": "Libros"})
        for item in movies:
            todos_los_titulos.append({"titulo": item["titulo"], "origen": "Películas"})
        for item in music:
            todos_los_titulos.append({"titulo": item["titulo"], "origen": "Música"})

        # Mostrar todos los títulos en formato de tabla usando tabulate
        print("\nTodos los títulos disponibles:")
        headers = ["#", "Título", "Origen"]
        table = [[i+1, item['titulo'], item['origen']] for i, item in enumerate(todos_los_titulos)]
        print(tabulate(table, headers=headers, tablefmt="grid"))

        # Solicitar al usuario que elija el título a eliminar
        try:
            opcion = int(input("\nSelecciona el número del título que deseas eliminar: "))
            if opcion < 1 or opcion > len(todos_los_titulos):
                print("Opción no válida.")
                return
        except ValueError:
            print("Por favor ingresa un número válido.")
            return

        # Obtener el título y su origen
        titulo_a_eliminar = todos_los_titulos[opcion - 1]["titulo"]
        origen = todos_los_titulos[opcion - 1]["origen"]

        # Determinar el archivo basado en el origen
        if origen == "Libros":
            file_name = "books.json"
        elif origen == "Películas":
            file_name = "movies.json"
        else:
            file_name = "musics.json"

        # Leer el archivo correspondiente
        file_path = os.path.join('data', file_name)
        items = json.load(open(file_path, "r", encoding="utf-8"))

        # Filtrar los elementos que no coinciden con el título
        items_filtrados = [item for item in items if item['titulo'] != titulo_a_eliminar]

        # Verificar si el título fue encontrado y eliminado
        if len(items) == len(items_filtrados):
            print(f"No se encontró un {origen} con el título '{titulo_a_eliminar}'.")
        else:
            # Guardar los cambios en el archivo JSON
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(items_filtrados, file, indent=4, ensure_ascii=False)
            print(f"El {origen} con el título '{titulo_a_eliminar}' ha sido eliminado exitosamente.")
            back = input(
            "¿Deseas seguir eliminando? (s/n)"
                )
        if back.lower() == "s":
            continue #se queda en el menu
        else:
          break

# Ruta de la carpeta donde se encuentran los archivos
folder_path = 'data'


# Función única para eliminar un elemento por su ID de los tres archivos
def eliminar_elemento_por_id():
    while True:

        # Preguntar al usuario qué tipo de archivo desea modificar
        print("Seleccione el tipo de archivo que desea modificar:")
        print("1. Libro")
        print("2. Película")
        print("3. Música")
        
        try:
            opcion = int(input("Ingrese el número correspondiente (1, 2, o 3): "))
        except ValueError:
            print("Por favor, ingresa un número válido para la opción.")
            return

        # Definir los archivos según la opción seleccionada
        if opcion == 1:
            archivo = 'books.json'
        elif opcion == 2:
            archivo = 'movies.json'
        elif opcion == 3:
            archivo = 'musics.json'
        else:
            print("Opción no válida. Por favor, elige 1, 2 o 3.")
            return

        archivo_path = os.path.join(folder_path, archivo)  # Ruta completa del archivo
        
        # Verificar si el archivo existe
        if not os.path.exists(archivo_path):
            print(f"El archivo {archivo} no existe.")
            return

        # Cargar los datos del archivo
        with open(archivo_path, 'r', encoding='utf-8') as file:
            datos = json.load(file)
        
        # Mostrar los elementos disponibles en el archivo usando tabulate
        print(f"\nLos elementos disponibles en {archivo}:")
        tabla = []
        for elemento in datos:
            # Extraemos el título y otros detalles según el tipo de archivo
            if 'titulo' in elemento:
                fila = [elemento['id'], elemento['titulo'], elemento.get('artista', ''), elemento.get('genero', ''), elemento.get('valoracion', '')]
                tabla.append(fila)
        
        # Imprimir la tabla
        headers = ["ID", "Título", "Artista", "Género", "Valoración"]
        print(tabulate(tabla, headers=headers, tablefmt="grid"))

        # Pedir la ID del elemento que se desea eliminar
        try:
            id_elemento = int(input("\nIntroduce la ID del elemento que deseas eliminar: "))
        except ValueError:
            print("Por favor, ingresa un número válido para la ID.")
            return

        # Filtrar los datos para eliminar el elemento con la ID especificada
        datos_actualizados = [elemento for elemento in datos if elemento["id"] != id_elemento]
        
        # Si encontramos un cambio, actualizamos la lista y cambiamos el indicador
        if len(datos_actualizados) != len(datos):
            # Guardar los datos actualizados de nuevo en el archivo
            with open(archivo_path, 'w', encoding='utf-8') as file:
                json.dump(datos_actualizados, file, ensure_ascii=False, indent=4)
            print(f"\nElemento con ID {id_elemento} ha sido eliminado de {archivo}.")
        else:
            print(f"\nNo se encontró ningún elemento con la ID '{id_elemento}' en {archivo}.")
            back = input(
            "¿Deseas seguir eliminando? (s/n)"
                )
        if back.lower() == "s":
            continue #se queda en el menu
        else:
          break

