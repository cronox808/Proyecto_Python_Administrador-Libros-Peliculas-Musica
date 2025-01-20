import json
import os
from tabulate import tabulate
def editTitle():
    while True:
    # Carpeta donde están los archivos JSON
        carpeta = 'data'
        archivos_json = ['books.json', 'movies.json', 'musics.json']

        # Cargar todos los títulos
        titulos = []
        for archivo in archivos_json:
            ruta_archivo = os.path.join(carpeta, archivo)
            if os.path.exists(ruta_archivo):
                with open(ruta_archivo, 'r') as file:
                    data = json.load(file)
                    for item in data:
                        titulos.append({'archivo': archivo, 'titulo': item['titulo']})

        # Mostrar la tabla con títulos y su índice (empezando desde 1)
        print("Títulos disponibles:")
        tabla = []
        for i, t in enumerate(titulos, start=1):
            tabla.append([i, t['archivo'], t['titulo']])

        # Usamos tabulate para mostrar los títulos en formato tabla con números de índice
        print(tabulate(tabla, headers=["Número", "Archivo", "Título"], tablefmt="grid"))

        # Solicitar al usuario que ingrese el número del título que desea modificar
        try:
            indice_usuario = int(input("\nIngresa el número del título que deseas modificar: ")) - 1
            if indice_usuario < 0 or indice_usuario >= len(titulos):
                print("Número fuera de rango. Intenta de nuevo.")
            else:
                nuevo_titulo = input(f"Ingresa el nuevo título para '{titulos[indice_usuario]['titulo']}': ")

                # Actualizar el archivo correspondiente
                archivo = titulos[indice_usuario]['archivo']
                ruta_archivo = os.path.join(carpeta, archivo)
                
                with open(ruta_archivo, 'r') as file:
                    data = json.load(file)

                # Modificar el título en los datos
                for item in data:
                    if item['titulo'] == titulos[indice_usuario]['titulo']:
                        item['titulo'] = nuevo_titulo
                        break

                # Guardar los cambios en el archivo JSON
                with open(ruta_archivo, 'w') as file:
                    json.dump(data, file, indent=4, ensure_ascii=False)

                print(f"El título ha sido actualizado en el archivo {archivo}.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
            cn = input(
            "¿Volver a intentar? (s/n)"
                )
            if cn.lower() == "s":
                continue #se queda en el menu
            else:
                break
        back = input(
            "¿Deseas seguir editando? (s/n)"
                )
        if back.lower() == "s":
            continue #se queda en el menu
        else:
            break

def editADA():
    while True:
        # Carpeta donde están los archivos JSON
        carpeta = 'data'
        archivos_json = ['books.json', 'movies.json', 'musics.json']

        # Cargar todos los títulos y sus autores/artistas/directores
        items = []
        for archivo in archivos_json:
            ruta_archivo = os.path.join(carpeta, archivo)
            if os.path.exists(ruta_archivo):
                with open(ruta_archivo, 'r') as file:
                    data = json.load(file)
                    for item in data:
                        if archivo == 'books.json' and 'autor' in item:
                            person = item['autor']
                        elif archivo == 'movies.json' and 'director' in item:
                            person = item['director']
                        elif archivo == 'musics.json' and 'artista' in item:
                            person = item['artista']
                        else:
                            continue  # Si no tiene el campo correspondiente, se omite el ítem
                        items.append({'archivo': archivo, 'titulo': item['titulo'], 'persona': person})

        # Mostrar la tabla con los títulos y las personas asociadas
        print("Elementos disponibles:")
        tabla = []
        for i, t in enumerate(items, start=1):
            tabla.append([i, t['archivo'], t['titulo'], t['persona']])

        # Usamos tabulate para mostrar los elementos en formato tabla con números de índice
        print(tabulate(tabla, headers=["Número", "Archivo", "Título", "Persona (Autor/Artista/Director)"], tablefmt="grid"))

        # Solicitar al usuario que ingrese el número del título que desea modificar
        try:
            indice_usuario = int(input("\nIngresa el número del título cuyo autor/artista/director deseas modificar: ")) - 1
            if indice_usuario < 0 or indice_usuario >= len(items):
                print("Número fuera de rango. Intenta de nuevo.")
            else:
                nuevo_persona = input(f"Ingresa el nuevo autor/artista/director para '{items[indice_usuario]['titulo']}': ")

                # Actualizar el archivo correspondiente
                archivo = items[indice_usuario]['archivo']
                ruta_archivo = os.path.join(carpeta, archivo)
                
                with open(ruta_archivo, 'r') as file:
                    data = json.load(file)

                # Modificar la persona en los datos
                for item in data:
                    if item['titulo'] == items[indice_usuario]['titulo']:
                        if archivo == 'books.json':
                            item['autor'] = nuevo_persona
                        elif archivo == 'movies.json':
                            item['director'] = nuevo_persona
                        elif archivo == 'musics.json':
                            item['artista'] = nuevo_persona
                        break

                # Guardar los cambios en el archivo JSON
                with open(ruta_archivo, 'w') as file:
                    json.dump(data, file, indent=4, ensure_ascii= False)

                print(f"El autor/artista/director ha sido actualizado en el archivo {archivo}.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue
        back = input(
                "¿Deseas seguir editando? (s/n)"
                    )
        if back.lower() == "s":
            continue #se queda en el menu
        else:
            break

def editValoracion():
     while True:
    # Carpeta donde están los archivos JSON
        carpeta = 'data'
        archivos_json = ['books.json', 'movies.json', 'musics.json']

        # Cargar todos los títulos
        titulos = []
        for archivo in archivos_json:
            ruta_archivo = os.path.join(carpeta, archivo)
            if os.path.exists(ruta_archivo):
                with open(ruta_archivo, 'r') as file:
                    data = json.load(file)
                    for item in data:
                        titulos.append({'archivo': archivo, 'titulo':item['titulo'], 'valoracion': item['valoracion']})

        # Mostrar la tabla con títulos y su índice (empezando desde 1)
        print("Valoraciones disponibles:")
        tabla = []
        for i, t in enumerate(titulos, start=1):
            tabla.append([i, t['archivo'],t['titulo'], t['valoracion']])

        # Usamos tabulate para mostrar los títulos en formato tabla con números de índice
        print(tabulate(tabla, headers=["Número", "Archivo",'titulo', "valoracion"], tablefmt="grid"))

        # Solicitar al usuario que ingrese el número del título que desea modificar
        try:
            indice_usuario = int(input("\nIngresa el número de la valoracion que deseasmodificar: ")) - 1
            if indice_usuario < 0 or indice_usuario >= len(titulos):
                print("Número fuera de rango. Intenta de nuevo.")
            else:
                nuevo_titulo = input(f"Ingresa la nueva valoracion para '{titulos[indice_usuario]['titulo']}': ")

                # Actualizar el archivo correspondiente
                archivo = titulos[indice_usuario]['archivo']
                ruta_archivo = os.path.join(carpeta, archivo)
                
                with open(ruta_archivo, 'r') as file:
                    data = json.load(file)

                # Modificar el título en los datos
                for item in data:
                    if item['titulo'] == titulos[indice_usuario]['titulo']:
                        item['valoracion'] = nuevo_titulo
                        break

                # Guardar los cambios en el archivo JSON
                with open(ruta_archivo, 'w') as file:
                    json.dump(data, file, indent=4, ensure_ascii=False)

                print(f"la valoracion ha sido actualizado en el archivo {archivo}.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
            cn = input(
            "¿Volver a intentar? (s/n)"
                )
            if cn.lower() == "s":
                continue #se queda en el menu
            else:
                break
        back = input(
            "¿Deseas seguir editando? (s/n)"
                )
        if back.lower() == "s":
            continue #se queda en el menu
        else:
            break

def editgener():
     while True:
    # Carpeta donde están los archivos JSON
        carpeta = 'data'
        archivos_json = ['books.json', 'movies.json', 'musics.json']

        # Cargar todos los títulos
        titulos = []
        for archivo in archivos_json:
            ruta_archivo = os.path.join(carpeta, archivo)
            if os.path.exists(ruta_archivo):
                with open(ruta_archivo, 'r') as file:
                    data = json.load(file)
                    for item in data:
                        titulos.append({'archivo': archivo, 'titulo':item['titulo'], 'genero': item['genero']})

        # Mostrar la tabla con títulos y su índice (empezando desde 1)
        print("Generos disponibles:")
        tabla = []
        for i, t in enumerate(titulos, start=1):
            tabla.append([i, t['archivo'],t['titulo'], t['genero']])

        # Usamos tabulate para mostrar los títulos en formato tabla con números de índice
        print(tabulate(tabla, headers=["Número", "Archivo",'titulo', "genero"], tablefmt="grid"))

        # Solicitar al usuario que ingrese el número del título que desea modificar
        try:
            indice_usuario = int(input("\nIngresa el número del genero que deseas modificar: ")) - 1
            if indice_usuario < 0 or indice_usuario >= len(titulos):
                print("Número fuera de rango. Intenta de nuevo.")
            else:
                nuevo_titulo = input(f"Ingresa el nuevo genero para '{titulos[indice_usuario]['titulo']}': ")

                # Actualizar el archivo correspondiente
                archivo = titulos[indice_usuario]['archivo']
                ruta_archivo = os.path.join(carpeta, archivo)
                
                with open(ruta_archivo, 'r') as file:
                    data = json.load(file)

                # Modificar el título en los datos
                for item in data:
                    if item['titulo'] == titulos[indice_usuario]['titulo']:
                        item['genero'] = nuevo_titulo
                        break

                # Guardar los cambios en el archivo JSON
                with open(ruta_archivo, 'w') as file:
                    json.dump(data, file, indent=4, ensure_ascii=False)

                print(f"la valoracion ha sido actualizado en el archivo {archivo}.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
            cn = input(
            "¿Volver a intentar? (s/n)"
                )
            if cn.lower() == "s":
                continue #se queda en el menu
            else:
                break
            
        back = input(
            "¿Deseas seguir editando? (s/n)"
                )
        if back.lower() == "s":
            continue #se queda en el menu
        else:
            break