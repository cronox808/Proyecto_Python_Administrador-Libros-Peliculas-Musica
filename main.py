from design.allMenus import addNewElementMenu, SeeAllItems, SearhElement, EditElement, deletElement, seeByCategory, saveAndLoadCollecton 
from logic.addMultimedia import dateBooks, dateMovies, dateMusic
from design.table import tableBooks
while(True):
    print("""
    ===========================================
            Administrador de Colección
    ===========================================
    1. Añadir un Nuevo Elemento
    2. Ver Todos los Elementos
    3. Buscar un Elemento
    4. Editar un Elemento
    5. Eliminar un Elemento
    6. Ver Elementos por Categoría
    7. Guardar y Cargar Colección
    8. Salir
    ===========================================
    Selecciona una opción (1-8): """)

    opc = int(input())

    if opc == 1:
        while(True):
            match addNewElementMenu():
                case 1:
                    dateBooks()
                case 2:
                    dateMovies()
                case 3:
                    dateMusic()
            back = input(
                "¿Deseas continuar en el menu de añadir un nuevo elemento?(s/n)"
                )
            if back.lower() == "s":
                continue #se queda en el menu
            else:
                break
    elif opc == 2 :
        match SeeAllItems():
            case 1:
               tableBooks()
    elif opc == 3 :
        match SearhElement():
            case 1:
                print("busacr")
    elif opc == 4 :
        match EditElement():
            case 1:
                print("editar titulo")

    elif opc == 5 :
        match deletElement():
            case 1:
                print("eliminar pedido")
    elif opc == 6 :
        match seeByCategory():
            case 1:
                print("ver libros")
    elif opc == 7 :
        match saveAndLoadCollecton():
            case 1:
                print("guardar colecion")
    elif opc == 8:
        print("chao")
        break
    else:
        print("¿eres tonto?") 




