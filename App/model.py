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
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""



# Construccion de modelos

def newCatalog():
    
    catalog = {"Lista_artistas" : None,
                "Lista_obras":None,
                "medios" : None}

    catalog["Lista_artistas"] = mp.newMap(1949,
        maptype="CHAINING", loadfactor=1.5)
    
    catalog["Lista_obras"] = mp.newMap(769,
        maptype="CHAINING", loadfactor=1.5)

    catalog["medios"] = mp.newMap(1949, maptype="CHAINGING" , loadfactor=1.5, )

    return catalog
# Funciones para agregar informacion al catalogo
def addArtist(catalog, artist):
    
    lista=catalog["Lista_artistas"]
    mp.put(lista, artist["ConstituentID"], artist)


def addArtwork(catalog, artwork):
    lista=catalog["Lista_obras"]
    mp.put(lista, artwork["ObjectID"], artwork)


def addMedium(catalog, artwork):

    lista=catalog["medios"]
    array=lt.newList(datastructure='ARRAY_LIST')
    
    if mp.contains(lista,artwork["Medium"] )== False:
        lt.addLast(array,artwork)
        mp.put(lista, artwork["Medium"], array)

    else:
        lt.addLast(array, artwork)
        mp.put(lista, artwork["Medium"], array)

    
# Funciones para creacion de datos





# Funciones de consulta

def ArtworkSize(catalog):
    return mp.size(catalog["Lista_obras"])

def AuthorsSize(catalog):   

    return mp.size(catalog["Lista_artistas"])

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
