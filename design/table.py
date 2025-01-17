import json
from tabulate import tabulate
def tableBooks():
    with open('data/books.json','r') as file:
        data = json. load(file)

    print(tabulate(data,headers="keys", tablefmt="grid"))