from design.allMenus import design, addNewElementMenu
from logic.books import addNewBook
from logic.movie import addNewMovie
match addNewElementMenu():
        case 1:
           addNewBook()
        case 2:
            addNewMovie()
        case 3:
            print("hola")
        case 4:
            print("vale")
            design()
