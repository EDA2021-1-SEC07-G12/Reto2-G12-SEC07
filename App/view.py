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
        #print(controller.ArtworkSize(catalog))
        
        
    elif int(inputs[0]) == 2:


        print(controller.artistas(catalog))

    elif int(inputs[0]) == 3:
        print(controller.organizar_obras(catalog))

        
    
    elif int(inputs[0]) == 4:
    

        print(controller.requerimiento3(catalog))

    elif int(inputs[0]) == 5:
        

        
        print(controller.requerimiento4(catalog))
    elif int(inputs[0]) == 6:
        

        print(controller.requerimiento5(catalog))
    
    
    else:
        sys.exit(0)
sys.exit(0)
    