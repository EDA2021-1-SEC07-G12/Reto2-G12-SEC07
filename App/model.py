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

from DISClib.Algorithms.Sorting import mergesort as ms
from App.controller import artistas
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT import orderedmap as om
import time
assert cf
from datetime import date
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

    
    catalog["nacionalidad"] =  mp.newMap(30000, maptype="PROBING" , loadfactor=0.8 )
    return catalog
# Funciones para agregar informacion al catalogo
def addArtist(catalog, artist):
    
    lista=catalog["Lista_artistas"]
    mp.put(lista, artist["ConstituentID"], artist)


def addArtwork(catalog, artwork):
    lista=catalog["Lista_obras"]
    mp.put(lista, artwork["ObjectID"], artwork)




# Funciones para creacion de datos

def crearIndiceMedios(catalog):
    
    start_time = time.process_time()
    mapaMedios=mp.newMap(30000, maptype="CHAINING" , loadfactor=0.8)

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

    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000   
    
    
    print(elapsed_time_mseg)
   # return mapaMedios


# Funciones de consulta

def ArtworkSize(catalog):
    return mp.size(catalog["Lista_obras"])

def AuthorsSize(catalog):    
    return mp.size(catalog["Lista_artistas"])


def ordenarEdadAutores(catalog,inicio,final):
    start_time = time.process_time()
    autores = catalog["Lista_artistas"]
    lista= lt.newList(datastructure='ARRAY_LIST')
    for i in lt.iterator(mp.valueSet(autores)):
        if inicio<=int(i["BeginDate"])<=final:
            lt.addLast(lista,i)
    ordenados = sa.sort(lista,OrdenarFechas)
    retorno=lt.newList(datastructure='ARRAY_LIST')
    lt.addLast(retorno, lt.size(ordenados))
    primeros3=lt.subList(ordenados,1,3)
    ultimos3=lt.subList(ordenados,int(lt.size(ordenados))-3,3)
    for a in lt.iterator(ultimos3):
        lt.addLast(primeros3,a)
    lt.addLast(retorno,primeros3)

    
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    print(elapsed_time_mseg)

    #return retorno



# Funciones utilizadas para comparar elementos dentro de una lista

#Prueba

#Prueba rama prueba

def ordenarObras(dia1,mes1,anio1, dia2, mes2,anio2,catalogo):
    start_time = time.process_time()
    lista=lt.newList("ARRAY_LIST")
    inicial=date(anio1,mes1,dia1).isoformat()
    final=date(anio2,mes2,dia2).isoformat()

    for i in lt.iterator(mp.valueSet(catalogo["Lista_obras"])):
        

        if inicial<=i["DateAcquired"]<=final:
            lt.addLast(lista,i)
    
    autores=lt.newList("ARRAY_LIST")
    for j in lt.iterator(lista):
        lista1=j["ConstituentID"]
        lista1=lista1.replace('[',"")
        lista1=lista1.replace(']',"")
        lista1=lista1.replace(' ',"")
        lista1=lista1.split(",")
        for k in lista1:
            
           # if lt.isPresent(autores,k)==0:

            lt.addLast(autores,k)
    compradas=lt.newList("ARRAY_LIST")
    for x in lt.iterator(lista):
        if x["CreditLine"]=="Purchase":
                lt.addLast(compradas,x)
    retorno=lt.newList("ARRAY_LIST")

    lt.addLast(retorno,lt.size(compradas))
    lt.addLast(retorno,lt.size(autores))

    primeros3=lt.subList(lista,1,3)
    ultimos3=lt.subList(lista,int(lt.size(lista))-3,3)
    for a in lt.iterator(ultimos3):
        lt.addLast(primeros3,a)
    lt.addLast(retorno,primeros3)

    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    print(elapsed_time_mseg)


    #return retorno

def indiceNacionalidad(catalog):
    
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
    desconociada=mp.get(catalog['nacionalidad'],"Nationality unknown")
    vacia=mp.get(catalog['nacionalidad'],"")
    paises_unknown=lt.newList('ARRAY_LIST')
    if lt.size(desconociada['value'])>lt.size(vacia['value']):
        paises_unknown=desconociada['value']
        for z in vacia['value']:
            lt.addLast(paises_unknown,z)
    else:
        paises_unknown=vacia['value']
        for z in desconociada['value']:
            lt.addLast(paises_unknown,z)
    mp.put(catalog['nacionalidad'],'Nationality unknown',paises_unknown)
    mp.remove(catalog['nacionalidad'],'')
    stop_time = time.process_time()
    

    return(catalog['nacionalidad'])

def requerimiento_4(catalog):
    start_time = time.process_time()


    mapa=indiceNacionalidad(catalog)
    llaves=mp.keySet(mapa)
    obras_x_pais=lt.newList('ARRAY_LIST')

    for i in lt.iterator(llaves):
        elemento=mp.get(mapa,i)
        tamano=lt.size(elemento['value'])
        tupla=(i,tamano)
        lt.addLast(obras_x_pais,tupla)
    ordenada=ms.sort(obras_x_pais,OrdenarNacionalidad)
    top10=lt.subList(ordenada,1,10)
    primero=lt.getElement(top10,1)
    final=primero[0]
    obras=mp.get(mapa,final)
    lista_obras=obras['value']
    lista_3_3=lt.newList('ARRAY_LIST')
    lt.addLast(lista_3_3,lt.getElement(lista_obras,1))
    lt.addLast(lista_3_3,lt.getElement(lista_obras,2))
    lt.addLast(lista_3_3,lt.getElement(lista_obras,3))
    lt.addLast(lista_3_3,lt.getElement(lista_obras,-1))
    lt.addLast(lista_3_3,lt.getElement(lista_obras,-2))
    lt.addLast(lista_3_3,lt.getElement(lista_obras,-3))
    lista_final=lt.newList('ARRAY_LIST')
    lt.addLast(lista_final,lista_3_3)
    lt.addLast(lista_final,top10)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    print(elapsed_time_mseg)


    return lista_final


def requerimiento3(catalog, artista):
    start_time = time.process_time()
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

    contadas1 = contarObras(lista_obras)
    retorno=0
    valor=0
    for z in lt.iterator(mp.keySet(contadas1)):
        variable= mp.get(contadas1,z)
        if variable["value"]>valor:
            retorno=z
            valor=variable["value"]

    retorno1=lt.newList("ARRAY_LIST")
    medio_mas_usado=lt.newList("ARRAY_LIST")
    lt.addLast(retorno1,retorno )
    lt.addLast(retorno1,valor)    
    
    for x in lt.iterator(lista_obras):
        if x["Medium"]==retorno:
            lt.addLast(medio_mas_usado,x)
    lt.addLast(retorno1,medio_mas_usado)

    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    print(elapsed_time_mseg)

    #return retorno1

def requerimiento5(catalog, departamento):
    start_time = time.process_time()
    mapa=crearMapaReq5(catalog)
    departament= mp.get(mapa,departamento)
    obras=departament["value"]
    costos=calcularCostos(obras)
    retorno=lt.newList("ARRAY_LIST")

    lt.addLast(retorno,costos)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    print(elapsed_time_mseg)


   # return retorno


def crearMapaReq5(catalog):
    mapa=mp.newMap(30000, maptype="PROBING" , loadfactor=0.8 )
    for i in lt.iterator(mp.valueSet(catalog["Lista_obras"])):
        lista=lt.newList("ARRAY_LIST")
        
        if mp.contains(mapa,i["Department"])==False:
            lt.addLast(lista,i)
            mp.put(mapa, i["Department"],lista)
        else:
            dato = mp.get(mapa,i["Department"])
            value=dato["value"]
            lt.addLast(value,i)
            mp.put(mapa,i["Department"],value)
    return mapa

def calcularCostos(catalogo):
    for i in lt.iterator(catalogo):
       
        if i["Height (cm)"]!= "":

            altura= float(i["Height (cm)"])/100
        elif i["Length (cm)"]!="":
            altura=float(i["Length (cm)"])/100
        else:
            altura=0
        if i["Width (cm)"]!="":

            ancho = float(i["Width (cm)"])/100
        else:
            ancho=0
        
        if i["Depth (cm)"]!="":

            profundidad= float(i["Depth (cm)"])/100
        else:
            profundidad=0
            
        if i["Weight (kg)"]!= "":

            peso=float(i["Weight (kg)"])
        else:
            peso=0
        
        if i["Diameter (cm)"]!="":

            radio = ((float(i["Diameter (cm)"])/2)/100)
        else:
            radio=0

        
        area=altura*ancho*72
        volumen=altura*ancho*profundidad*72
        peso = peso*72
        area_cir=(radio*radio*radio)*4*3.1416/3*72
        lista=[area,volumen,peso,area_cir]
        if max(lista)==0:
            i["Costo"]=48
        else:
            i["Costo"] = max(lista)
    return catalogo
# Funciones de ordenamiento

def agregarAutores(catalog):
    obras= catalog["Lista_obras"]
    artistas = catalog["Lista_artistas"]
    

def contarObras(catalog):
    medios=mp.newMap(20, maptype="PROBING" , loadfactor=0.8 )
    
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

def OrdenarNacionalidad(e1,e2):
    
    Retorno=True

    if int(e1[1])>=int(e2[1]):
        Retorno=True
    else:
        Retorno=False
    return Retorno

