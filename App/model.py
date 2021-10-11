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


from App.controller import artistas
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
                "medios" : None,
                "nacionalidad":None}

    catalog["Lista_artistas"] = mp.newMap(1949,
        maptype="CHAINING", loadfactor=1.5)
    
    catalog["Lista_obras"] = mp.newMap(769,
        maptype="CHAINING", loadfactor=1.5)

    catalog["medios"] = mp.newMap(1949, maptype="CHAINING" , loadfactor=1.5, )
    catalog["nacionalidad"] = mp.newMap(1949, maptype="CHAINING" , loadfactor=1.5, )
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

def crearIndiceMedios(catalog):
    mapaMedios=mp.newMap(1949, maptype="CHAINING" , loadfactor=1)

    for i in lt.iterator(mp.valueSet(catalog["Lista_obras"])):
        lista=lt.newList("ARRAY_LIST")
        
        if mp.contains(mapaMedios,i["Medium"])==False:
            lt.addLast(lista,i)
            mp.put(mapaMedios, i["Medium"],lista)
        else:
            dato = mp.get(mapaMedios,i["Medium"])
            value=dato["value"]
            lt.addLast(value,i)
            mp.put(mapaMedios,i["Medium"],value)
    return mp.get(mapaMedios,"Drypoint")

# Funciones de consulta

def ArtworkSize(catalog):
    return mp.size(catalog["Lista_obras"])

def AuthorsSize(catalog):   

    return mp.size(catalog["Lista_artistas"])


def ordenarEdadAutores(catalog,inicio,final):
    autores = catalog["Lista_artistas"]
    lista= lt.newList(datastructure='ARRAY_LIST')
    for i in lt.iterator(mp.valueSet(autores)):
        if inicio<=int(i["BeginDate"])<=final:
            lt.addLast(lista,i)
    ordenados = sa.sort(lista,OrdenarFechas)
    return ordenados



# Funciones utilizadas para comparar elementos dentro de una lista

#Prueba

#Prueba rama prueba

def asignarArtista(catalog):
    obras= catalog["Lista_obras"]
    artistas = catalog["Lista_artistas"]

    keyObras = mp.valueSet(obras)
    valueArt=mp.valueSet(artistas)
    for i in lt.iterator(keyObras):
        const = i["ConstituentID"]
        
        const=const.replace('[',"")
        const=const.replace(']',"")
        const=const.split(",")
        constfinal= const[0]
        artista1 = mp.get(artistas, constfinal)
        
        nacionalidad = artista1["value"]["Nationality"]
        
        
        if mp.contains(catalog["nacionalidad"], nacionalidad)== False:
            lista = lt.newList("ARRAY_LIST")
            lt.addLast(lista,i)
            mp.put(catalog["nacionalidad"], nacionalidad, lista)
        else:
            valor = mp.get(catalog["nacionalidad"], nacionalidad)
            lt.addLast(valor["value"],i)
    print(mp.get(catalog["nacionalidad"], "Colombian"))
       
def requerimiento3(catalog, artista):
    obras = catalog["Lista_obras"]
    artistas= catalog["Lista_artistas"]

    valoresArt= mp.valueSet(artistas)
    for i in lt.iterator(valoresArt):
        if i["DisplayName"]==artista:
            artista_cons=i["ConstituentID"]
    lista_obras=lt.newList("ARRAY_LIST")

    for j in lt.iterator(mp.valueSet(obras)):
        lista=j["ConstituentID"]
        lista=lista.replace('[',"")
        lista=lista.replace(']',"")
        lista=lista.split(",")
        
        if artista_cons in lista:
            lt.addLast(lista_obras,j)

    contar = contarObras(lista_obras)
    for x in lt.iterator(mp.valueSet(contar)):
        print(x)
    for z in lt.iterator(mp.keySet(contar)):
        print(z)
# Funciones de ordenamiento

def agregarAutores(catalog):
    obras= catalog["Lista_obras"]
    artistas = catalog["Lista_artistas"]
    

def contarObras(catalog):
    medios=mp.newMap(1949, maptype="CHAINING" , loadfactor=1.5)
    
    for i in lt.iterator(catalog):
        
        if mp.contains(medios,i["Medium"])==False:
            
         mp.put(medios,i["Medium"],1)
        else:
            dato = mp.get(medios,i["Medium"])
            value=dato["value"]
            value=int(value)+1
            mp.put(medios,i["Medium"],value)
    
    return medios



def OrdenarFechas(artista1,artista2):

    Retorno=True
    if int(artista1["BeginDate"])<=int(artista2["BeginDate"]):
        Retorno=True
    else:
        Retorno=False
    return Retorno



