"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Ordenar autores por fecha de nacimiento")
    print("3- Ordenar obras por fecha de adquisición")
    print("4- Ordenar medios de un artistas")
    print("5- Ordenar obras por nacionalidad")
    print("6- Calcular costo de transporte de las obras de un departamento")
   
catalog= controller.initCatalog()
print("3- Ordenar obras por nacionalidad")
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        controller.loadData(catalog)
       # 
        print( "Cantidad de artistas cargados: " + str(controller.ArtistSize(catalog)))
        print("Cantidad de obras cargadas: " + str(controller.ArtworkSize(catalog)))
        print(controller.ArtworkSize(catalog))
        
        
    elif int(inputs[0]) == 2:


        lista= controller.artistas(catalog)
        print("El numero de artistas en el intervalo es de " + str(lt.getElement(lista,1)))
        print("Los 3 primeros y ultimos artistas encontrados en el intervalo de tiempo son: ")

        for i in lt.iterator(lt.getElement(lista,2)):
            print(i)

    elif int(inputs[0]) == 3:
        lista= controller.organizar_obras(catalog)
        print("El numero de obras compradas por el museo es de " + str(lt.getElement(lista,1)))
        print("El numero de obras total en el intervalo es de " + str(lt.getElement(lista,2)))
        print("Las 3 primeras y ultimas obras en el intervalo de tiempo insertado son ")
        for i in lt.iterator(lt.getElement(lista,3)):
            print(i) 
        
    
    elif int(inputs[0]) == 4:
    

        lista=controller.requerimiento3(catalog)
        print(lista)
        print("Los cinco medios mas utilizados fueron ")
        for j in lt.iterator(lt.getElement(lista,4)):
            print(j["key"]+ " "  + str(j["value"])) 
        print("El medio mas utilizado fue " + str(lt.getElement(lista,1)) + " Con " + str(lt.getElement(lista,2)) + " usos")
        print("Las obras con el medio mas utilizado fueron: ")
        for i in lt.iterator(lt.getElement(lista,3)):
            print(i) 


    elif int(inputs[0]) == 5:
        

        
        resp=controller.requerimiento4(catalog)
        paises=lt.getElement(resp,2)
        obras=lt.getElement(resp,1)
        for i in lt.iterator(paises):
            print (i[0]+'   '+str(i[1]))
        print (obras)
    elif int(inputs[0]) == 6:
        

       lista = controller.requerimiento5(catalog)
       
       print("La cantidad de obras a transportar es de " + str(lt.getElement(lista,5)))
       print("El peso de las obras obras a transportar es de " + str(lt.getElement(lista,4)))
       print("El costo total del transporte es de " + str(lt.getElement(lista,3)))
       print("Las obras mas costosas a transportar son ")
       for i in lt.iterator(lt.getElement(lista,1)):
            print(i) 
       print("Las obras mas antiguas a transportar son ")
       for j in lt.iterator(lt.getElement(lista,2)):
            print(j) 
    
    else:
        sys.exit(0)
sys.exit(0)
    