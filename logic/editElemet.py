import json
import os
from tabulate import tabulate
def editTitle():
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
                json.dump(data, file, indent=4)

            print(f"El título ha sido actualizado en el archivo {archivo}.")
    except ValueError:
        print("Por favor, ingresa un número válido.")