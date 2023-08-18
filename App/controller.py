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
import model
import csv
import os


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def newController():
    """
    Crea una instancia del modelo
    """
    control = {
        "model": None
    }
    control["model"] = model.newCatalog()
    return control


# Funciones para la carga de datos

def loadBooks(control, filename):
    """
    Carga los libros del archivo. Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    catalog = control.get("model")
    booksfile = os.path.join(cf.data_dir, filename)
    catalog = model.addBooks(catalog, booksfile)
    if model.emptyBooks(catalog):
        return None
    else:
        return model.bookSize(catalog)


def loadTags(control, filename):
    """
    Carga todos los tags del archivo y los agrega a la lista de tags
    """
    catalog = control.get("model")
    tagsfile = os.path.join(cf.data_dir, filename)
    input_file = csv.DictReader(open(tagsfile, encoding="utf-8"))
    catalog = model.createTagList(catalog)
    for tag in input_file:
        model.addTag(catalog, tag)
    if model.emptyTags(catalog):
        return None
    else:
        return model.tagSize(catalog)


def loadBooksTags(control, filename):
    """
    Carga los tags de los libros del archivo y los agrega a la lista
    de tags. Siga el mismo procedimiento que en la carga de libros.
    """
    # TODO: Mods Lab 1, integrar vista y modelo
    catalog = control.get("model")
    booksfile = os.path.join(cf.data_dir, filename)
    catalog = model.addBookTags(catalog, booksfile)
    if model.emptyBookTags(catalog):
        return None
    else:
        return model.bookTagSize(catalog)
    pass
