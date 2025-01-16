from design.allMenus import design, adNewElementMenu, seeByCategory, saveAndLoadCollecton, SearhElement,EditElement, deletElement, SeeAllItems, saveAndLoadCollecton
from design.books import addNewBook

match design():
        case 1:
           adNewElementMenu()
        case 2:
            SeeAllItems()
        case 3:
            seeByCategory()
        case 4:
            EditElement()
        case 5:
            deletElement()
        case 6:
            seeByCategory()
        case 7:
            saveAndLoadCollecton()
        case  8:
            print("Adios")
        case _:
            print("No enender tu elexion, por favor marque una opcion valida, no sea pendejo")

match adNewElementMenu():
        case 1:
           addNewBook()
        case 2:
            SeeAllItems()
        case 3:
            seeByCategory()
        case 4:
            EditElement()
        case 5:
            deletElement()
        case 6:
            seeByCategory()
        case 7:
            saveAndLoadCollecton()
        case  8:
            print("Adios")
        case _:
            print("No enender tu elexion, por favor marque una opcion valida, no sea pendejo")