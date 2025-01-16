El **Administrador de Colección de Libros/Películas/Música** es una aplicación de consola que permite al usuario gestionar una colección personal de elementos culturales, como libros, películas o música. El objetivo principal es ofrecer una herramienta sencilla para organizar títulos, con detalles como el autor, género, y una valoración. Esto es útil para quienes desean mantener un registro estructurado de su colección, consultar rápidamente algún elemento o encontrar recomendaciones basadas en ciertos criterios.


# Problemática

Para muchas personas, organizar su colección de libros, películas o música puede ser un desafío, especialmente cuando el número de elementos crece y es difícil recordar detalles específicos. Sin un sistema, es complicado:

- Mantener un registro ordenado de cada elemento con sus características.
- Consultar detalles de cada título, como autor, género o valoraciones, sin revisar manualmente cada uno.
- Realizar búsquedas rápidas por título, género o autor.

Este administrador de colección ayuda a resolver estas problemáticas al ofrecer una interfaz de consola donde los datos quedan organizados y accesibles. Además, la aplicación permite guardar y cargar los datos en un archivo JSON, asegurando que el registro de la colección se mantenga entre sesiones.



# **Tecnologías y Herramientas**

- **Front-end**: 
  - **Recursos**: 
    - **Diseño de los menús:** https://gist.github.com/programmersland/0d76751149e083e073e7aac03e6fbae0
    - **Librería para mostrar la información en formato de tablas:**  https://pypi.org/project/tabulate/
- **GitHub**: Para la gestión de versiones del código en el desarrollo, usando **conventional commits.**



# Funciones Principales

1. **Añadir Elemento a la Colección**
   - Permite al usuario registrar un nuevo elemento en la colección, especificando:
     - Título
     - Autor/Director/Artista (según el tipo de colección)
     - Género
     - Valoración o puntuación (opcional)
   - Los datos se guardan en un archivo JSON para su persistencia.
2. **Listar Elementos de la Colección**
   - Muestra todos los elementos registrados en la colección.
   - Puede incluir opciones de visualización adicionales, como listar por categoría (libros, películas o música) o por género.
3. **Buscar Elemento**
   - Función para buscar un elemento en la colección filtrando por:
     - Título
     - Autor o género
   - Facilita el acceso rápido a detalles específicos sin necesidad de revisar toda la lista.
4. **Editar Elemento**
   - Permite modificar la información de un elemento específico en la colección.
   - Los usuarios pueden actualizar detalles como el título, el autor o la valoración del elemento, y los cambios se guardan automáticamente en el archivo JSON.
5. **Eliminar Elemento**
   - Elimina un elemento de la colección según el título o un identificador específico.
   - Asegura que la colección esté actualizada y sin elementos duplicados o innecesarios.
6. **Cargar y Guardar Colección en JSON**
   - Al iniciar el programa, la aplicación carga la colección desde un archivo JSON para continuar donde el usuario la dejó.
   - Al finalizar, guarda automáticamente cualquier cambio realizado en el archivo JSON, manteniendo la persistencia de los datos.





# **Estructura del Menú Principal**

https://gist.github.com/programmersland/0d76751149e083e073e7aac03e6fbae0

```bash
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
Selecciona una opción (1-8):
```

1. **Añadir un Nuevo Elemento**
   - Opción para registrar un nuevo libro, película o música en la colección.
2. **Ver Todos los Elementos**
   - Muestra una lista de todos los elementos registrados en la colección.
3. **Buscar un Elemento**
   - Permite buscar un título específico por nombre, autor/director/artista o género.
4. **Editar un Elemento**
   - Opción para editar la información de un elemento existente en la colección (título, autor, género, valoración).
5. **Eliminar un Elemento**
   - Permite eliminar un elemento de la colección por su título o identificador único.
6. **Ver Elementos por Categoría**
   - Filtrar y mostrar solo libros, películas o música, según lo que el usuario elija.
7. **Guardar y Cargar Colección**
   - Permite guardar la colección actual en un archivo JSON o cargar la colección guardada previamente.
8. **Salir**
   - Cierra la aplicación.

## **Menú de Opciones - Añadir un Nuevo Elemento**

```bash
===========================================
        Añadir un Nuevo Elemento
===========================================
¿Qué tipo de elemento deseas añadir?
1. Libro
2. Película
3. Música
4. Regresar al Menú Principal
===========================================
Selecciona una opción (1-4):
```

------

## **Menú de Opciones - Ver Todos los Elementos**

```bash
===========================================
        Ver Todos los Elementos
===========================================
¿Qué categoría deseas ver?
1. Ver Todos los Libros
2. Ver Todas las Películas
3. Ver Toda la Música
4. Regresar al Menú Principal
===========================================
Selecciona una opción (1-4):
```

------

## **Menú de Opciones - Buscar un Elemento**

```bash
===========================================
        Buscar un Elemento
===========================================
¿Cómo deseas buscar?
1. Buscar por Título
2. Buscar por Autor/Director/Artista
3. Buscar por Género
4. Regresar al Menú Principal
===========================================
Selecciona una opción (1-4):
```

------

## **Menú de Opciones - Editar un Elemento**

```bash
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
Selecciona una opción (1-5):
```

------

## **Menú de Opciones - Eliminar un Elemento**

```bash
===========================================
        Eliminar un Elemento
===========================================
¿Cómo deseas eliminar?
1. Eliminar por Título
2. Eliminar por Identificador Único
3. Regresar al Menú Principal
===========================================
Selecciona una opción (1-3):
```

------

## **Menú de Opciones - Ver Elementos por Categoría**

```bash
===========================================
        Ver Elementos por Categoría
===========================================
¿Qué categoría deseas ver?
1. Ver Libros
2. Ver Películas
3. Ver Música
4. Regresar al Menú Principal
===========================================
Selecciona una opción (1-4):
```

------

## **Menú de Opciones - Guardar y Cargar Colección**

===========================================
        Guardar y Cargar Colección
===========================================
¿Qué deseas hacer?
1. Guardar la Colección Actual
2. Cargar una Colección Guardada
3. Regresar al Menú Principal
===========================================
Selecciona una opción (1-3):