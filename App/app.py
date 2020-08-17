"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
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
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para
   cargar datos, contar elementos, y hacer búsquedas sobre una lista.
"""

import config as cf
import sys
import csv
from time import process_time


def loadCSVFile(file_d, file_c, lst_d, lst_c, sep=';'):
    """
    Carga un archivo csv a una lista
    Args:
        file_d
            Archivo de texto del cual se cargaran los detalles de las películas.
        file_c
            Archivo de texto del cual se cargaran los castings de las películas.
        lst_d :: []
            Lista a la cual quedaran cargados los detalles despues de la lectura del archivo.
        lst_c :: []
            Lista a la cual quedaran cargados los castings despues de la lectura del archivo.
        sep :: str
            Separadores código para diferenciar a los distintos elementos dentro del archivo.
    Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None   
    """
    del lst_d[:]
    del lst_c[:]
    print('Cargando archivos...')
    t1_start = process_time()  # tiempo inicial
    dialect = csv.excel()
    dialect.delimiter = sep
    try:
        with open(file_d, encoding='utf-8-sig') as csvfile_d, open(file_c, encoding='utf-8-sig') as csvfile_c:
            spamreader_d = csv.DictReader(csvfile_d, dialect=dialect)
            spamreader_c = csv.DictReader(csvfile_c, dialect=dialect)
            for row in spamreader_d:
                lst_d.append(row)
            for row in spamreader_c:
                lst_c.append(row)
    except:
        del lst_d[:]
        del lst_c[:]
        print('Se presento un error en la carga de los archivos')
    t1_stop = process_time()  # tiempo final
    print('Tiempo de ejecución ', t1_stop - t1_start, ' segundos')


def printMenu():
    """
    Imprime el menu de opciones
    """
    print('\nBienvenido')
    print('1- Cargar Datos')
    print('2- Contar los elementos de la Lista')
    print('3- Contar películas filtradas por palabra clave')
    print('4- Consultar buenas películas de un director')
    print('0- Salir')


def countElementsFilteredByColumn(criteria, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    Args:
        criteria:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        lst
            Lista en la cual se realizará el conteo, debe estar inicializada
    Return:
        counter :: int
            la cantidad de veces que aparece un elemento con el criterio definido
    """
    if len(lst) == 0:
        print('La lista esta vacía')
        return 0
    else:
        t1_start = process_time()  # tiempo inicial
        counter = 0  # Cantidad de repeticiones
        for element in lst:
            if criteria.lower() in element[column].lower():  # filtrar por palabra clave
                counter += 1
        t1_stop = process_time()  # tiempo final
        print('Tiempo de ejecución ', t1_stop - t1_start, ' segundos')
    return counter


def encontrarBP(lst):
    loadCSVFile("Data/MoviesCastingRaw-large.csv", lst)
    contador = 0
    lst1 = []
    for i in range(0,len(lst)):
        if lst1[i]["vote_average"]>=6:
            lst1.append(lst1[i]["vote_average"])
            contador +=1
    return contador

 # Alternativa 1
def ID(criteria,lst):
    loadCSVFile("Data/MoviesCastingRaw-large.csv", lst)
    numofmovies = []
    for element in lst:
            if criteria.lower() in element['director_name'].lower():  # filtrar por nombre
                numofmovies.append(element["id"]) 
    return numofmovies
    

# Alternativa 2
def countElementsByCriteria(criteria, column,lst):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """
    find = encontrarBP(lst)
    find2 = ID(criteria,lst)
    findprom = []
    count = 0
    if len(lst) == 0:
        print("La lista esta vacía")

    else:
        t2_start = process_time()  # tiempo inicial
        for i in range(0,len(lst)):
            if find2 in lst:
                if lst[i]["vote_average"]>=6:
                    findprom.append(lst[i]["vote_average"])
                    count +=1
                    prom = sum(findprom)/ count

        t2_stop = process_time()  # tiempo final
        print("Tiempo de ejecución ", t2_stop - t2_start, " segundos")
    return (find,prom)

def encontrar_ID(nombre,lst):
    lista = []
    listas = []
    loadCSVFile("Data/MoviesCastingRaw-large.csv", lista) 
    for i in range(0,len(lista)):        
        if lista[i]["director_name"].lower() == nombre.lower():
            listas.append(lista[i]["id"])
    return lista

# Alternativa 1
def countElementsByCriteria_alt1(criteria,lst):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """
    lista = encontrar_ID(criteria,lst)
    pr =[]
    for i in range(0,len(lista)):
        if lst[i]["\ufeffid"] in lista: #Comparación director
            if lst[i]["vote_average"]>= 6:
                pr.append(lst[i]["vote_average"])
                contador += 1   #Número de películas buenas o con votación positiva
                promedio = sum(pr)/contador   
    return (contador,promedio)

def countElementsByCriteria(criteria, vote_average, lst_d, lst_c):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """
    if len(lst_d) == 0:
        print('Las listas están vacías')
        return 0, 0
    else:
        t1_start = process_time()  # tiempo inicial
        director_movies = []
        # Search all director movies and add them to a list.
        for element in lst_c:
            if criteria.lower() in element['director_name'].lower():  # filtrar por nombre
                director_movies.append(element)
        # Search good movies and add vote points to list.
        good_movies_votes = []
        for movie in director_movies:
            for element in lst_d:
                if movie['id'] == element['id']:
                    actual_vote = float(element['vote_average'])
                    if actual_vote >= vote_average:
                        good_movies_votes.append(actual_vote)
        # Calculate number of good movies and total vote average of director.
        counter_good_movies = len(good_movies_votes)
        total_vote_average = sum(good_movies_votes) / counter_good_movies
        t1_stop = process_time()  # tiempo final
        print('Tiempo de ejecución ', t1_stop - t1_start, ' segundos')
    return counter_good_movies, round(total_vote_average, 1)


def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    details_list = []  # instanciar una lista vacia
    casting_list = []  # instanciar una lista vacia
    while True:
        printMenu()  # imprimir el menu de opciones en consola
        inputs = input('Seleccione una opción para continuar:\n')  # leer opción ingresada
        if len(inputs) > 0:
            if int(inputs[0]) == 1:  # opcion 1

                """Alternativa 1
                loadCSVFile("Data/MoviesDetailsCleaned-large.csv", lista)  # llamar funcion cargar datos
                print("Datos cargados, " + str(len(lista)) + " elementos cargados")
            elif int(inputs[0]) == 2:  # opcion 2   
                if len(lista) == 0:  # obtener la longitud de la lista
                    print("La lista esta vacía")
                  """

                """ Alternativa 2
                loadCSVFile("Data/MoviesDetailsCleaned-large.csv", lista)  # llamar funcion cargar datos
                print("Datos cargados, " + str(len(lista)) + " elementos cargados")
                """
                loadCSVFile('../Data/MoviesDetailsCleaned-large.csv', '../Data/MoviesCastingRaw-large.csv',
                            details_list, casting_list)  # llamar funcion cargar datos
                if len(details_list) == len(casting_list):
                    print('Datos cargados, ' + str(len(details_list)) + ' elementos cargados en listas')
                else:
                    print('Datos cargados, aunque inconsistentes')
            elif int(inputs[0]) == 2:  # opcion 2
                if len(details_list) == 0:  # obtener la longitud de la lista
                    print('La lista esta vacía')

                else:
                    print('La lista tiene ' + str(len(details_list)) + ' elementos')
            elif int(inputs[0]) == 3:  # opcion 3
            """ Alternativa 1
                criteria = input('Ingrese el criterio de búsqueda\n')
                counter = countElementsFilteredByColumn(criteria,"name",lista)  # filtrar una columna por criterio
                print("Coinciden ", counter, " elementos con el crtierio: ", criteria)
            elif int(inputs[0]) == 4:  # opcion 4
                criteria = input('Ingrese el criterio de búsqueda\n')
                counter = countElementsByCriteria(criteria, lista)
                print("Coinciden ", counter, " elementos con el crtierio: '", criteria, "' (en construcción ...)")
            """
                criteria = input('Ingrese un director para consultar su cantidad de películas:\n')  # filtrar columna
                counter_movies = countElementsFilteredByColumn(criteria, 'director_name', casting_list)
                print('Coinciden', counter_movies, 'elementos con el director', criteria)
            elif int(inputs[0]) == 4:  # opcion 4
                criteria = input('Ingrese el nombre del director para conocer la votación en sus películas:\n')
                counter, average = countElementsByCriteria(criteria, 6, details_list, casting_list)
                print('Existen', counter, 'buenas películas del director', criteria, 'en el catálogo')
                print('Las buenas películas de este director tienen un promedio de votación de', average, 'puntos.')
            elif int(inputs[0]) == 0:  # opcion 0, salir
                sys.exit(0)


if __name__ == '__main__':
    main()
