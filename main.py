from design.allMenus import addNewElementMenu, SeeAllItems, SearhElement, EditElement, deletElement, seeByCategory, saveAndLoadCollecton 
from logic.addMultimedia import dateBooks, dateMovies, dateMusic
from design.table import tableBooks,tableMovies, tableMusic
from design.searhItem import searchByTitle, searchByADA, searchBygener
from logic.editAElemet import editTitle, editADA, editValoracion, editgener
from logic.deletAElement import deletBooks, eliminar_elemento_por_id
from logic.seeByCategory import mostrar_libros_por_categoria, mostrar_musica_por_categoria, mostrar_peliculas_por_categoria

while(True):
    try:
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
                    case 4:
                        break
                    case _:
                        print("opcion no valida")
                back = input(
                    "¿Deseas continuar en el menu de añadir un nuevo elemento?(s/n)"
                    )
                if back.lower() == "s":
                    continue #se queda en el menu
                else:
                    break
        elif opc == 2 :
            while(True):
                match SeeAllItems():
                    case 1:
                        tableBooks()
                    case 2:
                        tableMovies()
                    case 3:
                        tableMusic()
                    case 4:
                        break
                    case _:
                        print("opcion no valida")
                back = input(
                    "¿Deseas continuar en el menu de Ver Todos los Elementos?(s/n)"
                    )
                if back.lower() == "s":
                    continue #se queda en el menu
                else:
                    break

        elif opc == 3 :
            while(True):
                match SearhElement():
                    case 1:
                        searchByTitle()
                    case 2:
                        searchByADA()
                    case 3:
                        searchBygener()
                    case 4:
                        break
                    case _:
                        print("opcion no valida")
                back = input(
                    "¿Deseas continuar en el menu de buscar elementos?(s/n)"
                    )
                if back.lower() == "s":
                    continue #se queda en el menu
                else:
                    break
                        
        elif opc == 4 :
            while True:
                match EditElement():
                    case 1:
                        editTitle()
                    case 2:
                        editADA()
                    case 3:
                        editgener()
                    case 4:
                        editValoracion()
                    case 5:
                        break
                    case _:
                        print("opcion no valida")
                back = input(
                    "¿Deseas continuar en el menu de editar elemento?(s/n)"
                    )
                if back.lower() == "s":
                    continue #se queda en el menu
                else:
                    break
        elif opc == 5 :
            while True:
                match deletElement():
                    case 1:
                        deletBooks()
                    case 2:
                        eliminar_elemento_por_id()
                    case 3:
                        break  
                    case _:
                        print("opcion no valida")
                back = input(
                    "¿Deseas continuar en el menu de eliminar elemento?(s/n)"
                    )
                if back.lower() == "s":
                    continue #se queda en el menu
                else:
                    break

        elif opc == 6 :
            while True:
                match seeByCategory():
                    case 1:
                        mostrar_libros_por_categoria()
                    case 2:
                        mostrar_peliculas_por_categoria()
                    case 3:
                        mostrar_musica_por_categoria()
                    case _:
                        break
        elif opc == 7 :
            match saveAndLoadCollecton():
                case 1:
                    addNewElementMenu()
                case 2:
                    SeeAllItems()
                case 3:
                    print("chao")
        elif opc == 8:
            print("chao")
            break
    except:
        print("ingresa un dato valido")
        




