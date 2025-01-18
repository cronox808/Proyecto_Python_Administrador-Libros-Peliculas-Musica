import json
from tabulate import tabulate
import os

def searchByTitle ():
    while(True):
        # Ruta de la carpeta donde se encuentran los archivos JSON
        carpeta = 'data'
        # Lista de archivos JSON a procesar
        archivos_json = ['books.json', 'movies.json', 'musics.json']

        titleSearh = input("Introduce el título que deseas buscar: ")
        # Lista para almacenar los resultados encontrados
        resultados = []
        # Iterar sobre cada archivo en la carpeta
        for archivo in archivos_json:
            # Construir la ruta completa del archivo
            ruta_archivo = os.path.join(carpeta, archivo)
        # Verificar si el archivo existe
            if os.path.exists(ruta_archivo, ):
                with open(ruta_archivo, 'r') as file:
                    data = json.load(file)
                resultados.extend([item for item in data if item['titulo'].lower() == titleSearh.lower()])
            else:
                print(f"El archivo {archivo} no se encontró en la carpeta {carpeta}.")
            
        #verificar si hay resultados
        if resultados:
            #Mostrar los resultados con tabulate
            print(tabulate(resultados, headers="keys", tablefmt="grid"))   
        else:
            print("No se encontraron resultados para este titulo")
        back = input(
                "¿Deseas volver? (s/n)"
                )
        if back.lower() == "s":
                break#se regresa
        else:
             continue

def searchByADA():
    while(True):
        # Ruta de la carpeta donde se encuentran los archivos JSON
        carpeta = 'data'
        # Lista de archivos JSON a procesar
        archivos_json = ['books.json', 'movies.json', 'musics.json']

        search = input("Introduce el Autor/Director/Artista que deseas buscar: ")
        # Lista para almacenar los resultados encontrados
        resultados = []
        # Iterar sobre cada archivo en la carpeta
        for archivo in archivos_json:
            # Construir la ruta completa del archivo
            ruta_archivo = os.path.join(carpeta, archivo)
        # Verificar si el archivo existe
            if os.path.exists(ruta_archivo):
                with open(ruta_archivo, 'r') as file:
                    data = json.load(file)
                        # Buscar en las claves autor, director, o artista
                for item in data:
                    for clave in ['autor', 'director', 'artista']:
                        if clave in item and search.lower() in item[clave].lower():
                            resultados.append(item)
                            break 
            else:
                print(f"El archivo {archivo} no se encontró en la carpeta {carpeta}.")
            
        #verificar si hay resultados
        if resultados:
            #Mostrar los resultados con tabulate
            print(tabulate(resultados, headers="keys", tablefmt="grid"))   
        else:
            print("No se encontraron resultados para este titulo")
        back = input(
                "¿Deseas volver? (s/n)"
                )
        if back.lower() == "s":
                break#se regresa
        else:
             continue
def searchBygener ():
        while(True):
            # Ruta de la carpeta donde se encuentran los archivos JSON
            carpeta = 'data'
            # Lista de archivos JSON a procesar
            archivos_json = ['books.json', 'movies.json', 'musics.json']

            titleSearh = input("Introduce el genero que deseas buscar: ")
            # Lista para almacenar los resultados encontrados
            resultados = []
            # Iterar sobre cada archivo en la carpeta
            for archivo in archivos_json:
                # Construir la ruta completa del archivo
                ruta_archivo = os.path.join(carpeta, archivo)
            # Verificar si el archivo existe
                if os.path.exists(ruta_archivo, ):
                    with open(ruta_archivo, 'r') as file:
                        data = json.load(file)

                    for item in data:
                         if 'genero' in item and titleSearh.lower()in item['genero'].lower():
                            resultado = {
                                 'titulo': item.get('titulo', 'No disponible'),
                                 'genero': item.get('genero', 'No disponible'),
                                 'autor': item.get('autor', 'No disponible'),
                                 'director': item.get('director', 'No disponible'),
                                 'artista': item.get('artista', 'No disponible'),
                                 'valoracion': item.get('valoracion', 'No disponible'),
                            }
                            resultados.append(resultado)
                else:
                    print(f"El archivo {archivo} no se encontró en la carpeta {carpeta}.")
                
            #verificar si hay resultados
            if resultados:
                #Mostrar los resultados con tabulate
                print(tabulate(resultados, headers="keys", tablefmt="grid"))   
            else:
                print("No se encontraron resultados para este titulo")
            back = input(
                    "¿Deseas volver? (s/n)"
                    )
            if back.lower() == "s":
                    break#se regresa
            else:
                continue