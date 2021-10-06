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
    print(mp.get(catalog["nacionalidad"], "Afghan"))
       
    
# Funciones de ordenamiento



def OrdenarFechas(artista1,artista2):
    Retorno=True
    if int(artista1["BeginDate"])<=int(artista2["BeginDate"]):
        Retorno=True
    else:
        Retorno=False
    return Retorno



def requerimiento_4_1(catalogo):
    obras=catalogo['lista_obras']
    artistas=catalogo['lista_artistas']
    lista_codigos_a=lt.newList('ARRAY_LIST')
    for k in range(lt.size(artistas)):
        elemento_a=lt.getElement(artistas,k)
        codigo_a=elemento_a['ConstituentID']
        lt.addLast(lista_codigos_a,codigo_a)
    lista_nacionalidad=lt.newList('ARRAY_LIST')  
    for i in range(lt.size(obras)):
        elemento_o=lt.getElement(obras,i)
        codigo_o=elemento_o['ConstituentID']
        codigo_o=codigo_o.replace('[',"")
        codigo_o=codigo_o.replace(']',"")
        posi=lt.isPresent(lista_codigos_a,codigo_o)
        elemento_final=lt.getElement(artistas,posi)
        nacionalidad=elemento_final['Nationality']
        lt.addLast(lista_nacionalidad,nacionalidad)
    nacionalidades_filtradas= eliminarRepetidos(lista_nacionalidad)
    n_contadas=contar(lista_nacionalidad,nacionalidades_filtradas)
    ordenada=ms.sort(n_contadas,OrdenarNacionalidad)
    top_10=lt.subList(ordenada,1,10)
    dict_top_10={}
    lista_paises=lt.newList('ARRAY_LIST')
    for c in top_10['elements']:
        lt.addLast(lista_paises,c['elements'][1])
        if c['elements'][1]=="":
            dict_top_10['Unkown']=c['size']
        else:
            dict_top_10[c['elements'][1]]=c['size']
    respuesta=(dict_top_10,lista_paises)
    return respuesta
def requerimiento_4_2(catalogo,lista_paises):
    pais=lt.getElement(lista_paises,1)
    obras=catalogo['lista_obras']
    artistas=catalogo['lista_artistas']
    lista_codigos_a=lt.newList('ARRAY_LIST')
    for k in range(lt.size(artistas)):
        elemento_a=lt.getElement(artistas,k)
        codigo_a=elemento_a['ConstituentID']
        lt.addLast(lista_codigos_a,codigo_a)
    lista_obras_pais=lt.newList('ARRAY_LIST')
    for i in range(lt.size(obras)):
        elemento_o=lt.getElement(obras,i)
        codigo_o=elemento_o['ConstituentID']
        codigo_o=codigo_o.replace('[',"")
        codigo_o=codigo_o.replace(']',"")
        posi=lt.isPresent(lista_codigos_a,codigo_o)
        elemento_final=lt.getElement(artistas,posi)
        nacionalidad=elemento_final['Nationality']
        resp_obra=lt.newList('ARRAY_LIST')
        lt.addLast(resp_obra,elemento_o['Title'])
        lt.addLast(resp_obra,elemento_final['DisplayName'])
        lt.addLast(resp_obra,elemento_o['Date'])
        lt.addLast(resp_obra,elemento_o['Medium'])
        lt.addLast(resp_obra,elemento_o['Dimensions'])
        if nacionalidad==pais:
            lt.addLast(lista_obras_pais,resp_obra)
    lista_final=lt.newList('ARRAY_LIST')
    lt.addLast(lista_final,lt.getElement(lista_obras_pais,1))
    lt.addLast(lista_final,lt.getElement(lista_obras_pais,2))
    lt.addLast(lista_final,lt.getElement(lista_obras_pais,3))
    lt.addLast(lista_final,lt.getElement(lista_obras_pais,-1))
    lt.addLast(lista_final,lt.getElement(lista_obras_pais,-2))
    lt.addLast(lista_final,lt.getElement(lista_obras_pais,-3))
    print (lista_final)