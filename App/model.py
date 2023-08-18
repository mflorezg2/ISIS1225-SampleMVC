"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 * Santiago Arteaga - Otras versiones
 """


import config as cf
from DISClib.ADT import list as lt
assert cf

"""
En el modelo, se crean las estructuras de datos, es decir,
las variables donde se van a guardar los datos leidos de los
archivos CSV.

El modelo debe ser el unico sitio donde se modifican y manipulan
los datos.
"""


def newCatalog():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {
        "books": None,
        "tags": None,
        "book_tags": None,
    }

    # definicion de arreglos
    catalog["books"] = lt.newList(datastructure="ARRAY_LIST")
    catalog["tags"] = lt.newList(datastructure="ARRAY_LIST")
    catalog["book_tags"] = lt.newList(datastructure="ARRAY_LIST")
    return catalog


# Funciones para agregar informacion al catalogo

def addBooks(catalog, booksfile):
    """
    Para guardar los libros provenientes del archivo CSV
    vamos a crear una lista, en donde quedarán todos los datos.

    No es importante entender como funciona esta lista por ahora.

    La funcion newList crea una lista de muchas formas. Una de ellas
    es leyendo todo lo que encuentre en el archivo indicado por filename.
    Cada linea del archivo quedará en una posicion de la lista.
    """
    books = catalog.get("books")
    books = lt.newList(datastructure="SINGLE_LINKED",
                       filename=booksfile)
    catalog.update({"books": books})
    return catalog


def addTag(catalog, tag):
    """
    Para procesar el archivo de tags vamos a usar de otra forma la lista.
    En este caso, agregaremos cada linea del archivo a la lista, en lugar
    de usar la opcion de crearla con el nombre del archivo.
    """
    tags = catalog.get("tags")
    lt.addLast(tags, tag)
    return catalog


def createTagList(catalog):
    """
    Esta funcion crea una lista vacia. Esta lista se utilizara
    para ir guardando la informacion en el archivo de tags.
    """
    tags = lt.newList(datastructure="SINGLE_LINKED")
    catalog.update({"tags": tags})
    return catalog


def addBookTags(catalog, booktagsfile):
    """
    Esta funcion crea una lista basado en el archivo de booktags. siga
    el mismo procedimiento que la funcion addBooks.
    """
    # TODO: Mods Lab 1, completar funcion.
    book_tags = catalog.get("Book_tags")
    book_tags = lt.newList(datastructure="SINGLE_LINKED",
                           filename=booktagsfile)
    catalog.update({"Book_tags": book_tags})
    return catalog
    pass


# Funciones de consulta

def bookSize(catalog):
    return lt.size(catalog["books"])


def tagSize(catalog):
    return lt.size(catalog["tags"])


def bookTagSize(catalog):
    return lt.size(catalog["book_tags"])


def emptyBooks(catalog):
    books = catalog.get("books")
    return lt.isEmpty(books)


def emptyTags(catalog):
    tags = catalog.get("tags")
    return lt.isEmpty(tags)


def emptyBookTags(catalog):
    book_tags = catalog.get("book_tags")
    return lt.isEmpty(book_tags)
