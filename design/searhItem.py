import json
from tabulate import tabulate
import os

def searhBook ():
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
