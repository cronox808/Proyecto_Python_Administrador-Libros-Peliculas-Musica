import json
from tabulate import tabulate
def tableBooks():
    while(True):
        with open('data/books.json','r') as file:
            data = json. load(file)
        # Usar tabulate para mostrar el contenido como una tabla
        # Si el JSON es una lista de diccionarios, puedes usar directamente tabulate
        print(tabulate(data,headers="keys", tablefmt="grid"))
        back = input(
                "¿Deseas volver? (s/n)"
                )
        if back.lower() == "s":
                break#se regresa
        else:
             continue
                
def tableMovies():
    while(True):
        with open('data/movies.json','r') as file:
            data = json. load(file)

        print(tabulate(data,headers="keys", tablefmt="grid"))
        back = input(
                "¿Deseas vover?(s/n)"
                )
        if back.lower() == "s":
                break #se regresa
        else:
             continue
                
def tableMusic():
    while(True):
        with open('data/musics.json','r') as file:
            data = json. load(file)

        print(tabulate(data,headers="keys", tablefmt="grid"))
        back = input(
                "¿Deseas continuar obserbando la tabla?(s/n)"
                )
        if back.lower() == "s":
                break #se regresa
        else:
             continue
                