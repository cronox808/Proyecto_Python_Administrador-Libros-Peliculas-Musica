

def addNewElementMenu():
    print("""
===========================================
        Añadir un Nuevo Elemento
===========================================
¿Qué tipo de elemento deseas añadir?
1. Libro
2. Película
3. Música
4. Regresar al Menú Principal
===========================================
Selecciona una opción (1-4): """)
    return int(input())

def SeeAllItems():
    print("""
===========================================
        Ver Todos los Elementos
===========================================
¿Qué categoría deseas ver?
1. Ver Todos los Libros
2. Ver Todas las Películas
3. Ver Toda la Música
4. Regresar al Menú Principal
===========================================
Selecciona una opción (1-4): """)
    return int(input())

def SearhElement():
    print("""
===========================================
        Buscar un Elemento
===========================================
¿Cómo deseas buscar?
1. Buscar por Título
2. Buscar por Autor/Director/Artista
3. Buscar por Género
4. Regresar al Menú Principal
===========================================
Selecciona una opción (1-4): """)
    return int(input())

def EditElement():
    print("""
===========================================
        Editar un Elemento
===========================================
¿Qué tipo de cambio deseas realizar?
1. Editar Título
2. Editar Autor/Director/Artista
3. Editar Género
4. Editar Valoración
5. Regresar al Menú Principal
===========================================
Selecciona una opción (1-5): """)
    return int(input())
    
def deletElement():
    print("""
===========================================
        Eliminar un Elemento
===========================================
¿Cómo deseas eliminar?
1. Eliminar por Título
2. Eliminar por Identificador Único
3. Regresar al Menú Principal
===========================================
Selecciona una opción (1-3): """)
    return int(input())

def seeByCategory():
    print("""
===========================================
        Ver Elementos por Categoría
===========================================
¿Qué categoría deseas ver?
1. Ver Libros
2. Ver Películas
3. Ver Música
4. Regresar al Menú Principal
===========================================
Selecciona una opción (1-4): """)
    return int(input())

def saveAndLoadCollecton():
    print("""
===========================================
        Guardar y Cargar Colección
===========================================
¿Qué deseas hacer?
1. Guardar la Colección Actual
2. Cargar una Colección Guardada
3. Regresar al Menú Principal
===========================================
Selecciona una opción (1-3): """)
    return int(input())