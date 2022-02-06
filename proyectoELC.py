# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 11:58:46 2022

@author: EstherLanchaCañas
"""

#============================================= IMPORTACIÓN DE LAS LIBRERÍAS =============================================#

import pandas as pd
import numpy as np

#============================================= CARGA DE LOS DATOS =============================================#

#En esta parte del programa realizamos la carga de todos los datos para posteriormente poder trabajar con ellos.

#Usuarios:
    
#En esta lista guardamos los nombres de las columnas para utilizarla como cabecera en el dataframe posterior:
userHeader = ['user_id', 'gender', 'age', 'ocupation', 'zip']

#Carga de los datos de usuarios. Los metemos en el dataframe USERS:
users = pd.read_table('d:/usuarios/Users/EstherLanchaCañas/OneDrive - IES Luis Braille/Entornos de Desarrollo\Entregable 4 - Control de versiones con Git/Proyecto/miProyecto/datos/users.dat', #Comentado para utilizarlo en clase.
                      engine='python', 
                      sep='::',
                      header=None, 
                      names=userHeader)

#Películas:
#En esta lista guardamos los nombres de las columnas para utilizarla como cabecera en el dataframe posterior:
movieHeader = ['movie_id', 'title', 'genders']

#Carga de los datos de las películas. Los metemos en el dataframe MOVIES:
movies = pd.read_table('d:/usuarios/Users/EstherLanchaCañas/OneDrive - IES Luis Braille/Entornos de Desarrollo\Entregable 4 - Control de versiones con Git/Proyecto/miProyecto/datos/movies.dat',
                      engine='python', 
                      sep='::',
                      header=None, 
                      names=movieHeader,
                      encoding='latin-1')


#Valoraciones:
#En esta lista guardamos los nombres de las columnas para utilizarla como cabecera en el dataframe posterior:
ratingHeader = ['user_id', 'movie_id', 'rating', 'timestamp']

#Carga de los datos de las valoraciones. Los metemos en el dataframe RATINGS:
ratings = pd.read_table('d:/usuarios/Users/EstherLanchaCañas/OneDrive - IES Luis Braille/Entornos de Desarrollo\Entregable 4 - Control de versiones con Git/Proyecto/miProyecto/datos/ratings.dat',
                      engine='python', 
                      sep='::',
                      header=None, 
                      names=ratingHeader)

#============================================= EXPORTACIÓN Y UNIÓN DE LOS DATOS =============================================#


#Mergeo de las tablas. Primero creo un dataframe temporal en el que uno users y ratings y después uno ese dataframe con movies.

mergeUsersRatings=pd.merge(users, ratings)
userRatingsMoviesDF=pd.merge(movies, mergeUsersRatings)


#============================================= PROGRAMA =============================================#


#MENÚ DE OPCIONES:


print("\n\n================================")
print("============= MENU =============")
print("================================\n\n")
print("Opción 1: Rating Medio STAR WARS por género")
print("Opción 2: Películas Mejor Valoradas")
print("Opción 3: Media de los usuarios del Género Terror")
print("Opción 4: Actualización de datos")
print("Opción 5: Salir del programa")
opc = int(input("Escoge una opción: "))

if opc == 1:
    #Opción 1: Rating Medio STAR WARS por género

    #Copio el dataframe general a la variable ratingStarWars para poder trabajar con él posteriormente.
    ratingStarWars = userRatingsMoviesDF.copy()

    #Aquí asigno a la variable starwars todas las películas que en el título contengan las palabras "Star Wars", generándose un nuevo dataframe.
    starwars = ratingStarWars[ratingStarWars['title'].str.contains('Star Wars')]

    #Después las agrupo por género y realizo la media del rating.
    mediaGenero = starwars.groupby(['gender'])['rating'].mean()

    #Exportamos el DataFrame a un CSV con separador de ,.
    mediaGenero.to_csv("d:/usuarios/Users/EstherLanchaCañas/OneDrive - IES Luis Braille/Entornos de Desarrollo\Entregable 4 - Control de versiones con Git/Proyecto/miProyecto/datos/Ejercicio1_EstherLanchaCanas.csv", sep=",")

elif opc == 2:
    #Copio el dataframe general a la variable dg para poder trabajar con él posteriormente.
    mejorValoradas = userRatingsMoviesDF.copy()

    #Creo una pivot table con título y ratings, y hago un conteo del número de votos y de la media de esos votos. Almaceno la tabla en la variable df.
    #Con aggfunc agregas las funciones sobre el valor rating (en este caso el numero de votos y la media)
    mejorValoradas = mejorValoradas.pivot_table(index=['title'], values=['rating'], aggfunc={'rating': [np.size, np.mean]}, fill_value=0)

    #Esta línea sirve para establecer dos únicas columnas llamadas 'rating_medium' (la media del rating) y 'num_votes' (número de votos).
    #mejorValoradas.columns = ['rating_medium', 'num_votes']

    #Aquí indicamos que solo muestre las películas con más de 1000 votos y que las ordene de mayor a menor según el rating.
    valoradasFinal = mejorValoradas[mejorValoradas[('rating','size')] > 1000].sort_values(('rating','mean'), ascending=False)
    
    #Exportamos el DataFrame a un CSV con separador de ,.
    valoradasFinal.to_csv("d:/usuarios/Users/EstherLanchaCañas/OneDrive - IES Luis Braille/Entornos de Desarrollo\Entregable 4 - Control de versiones con Git/Proyecto/miProyecto/datos/Ejercicio2_EstherLanchaCanas.csv", sep=",")

elif opc == 3:
    #Opción 3: Media de los usuarios del Género Terror

    #Copio el dataframe general a la variable mediaTerror para poder trabajar con él posteriormente.
    mediaTerror = userRatingsMoviesDF.copy()

    #Asigno a la variable horror todas las películas que contengan la palabra "Horror"
    horror = mediaTerror[mediaTerror['genders'].str.contains('Horror')]

    #Aquí realizamos la media de la edad y lo redondeamos a 2 decimales.
    media = horror['age'].mean().round(2)

    #Pintamos el resultado.
    print(f"La edad media de los usuarios TERRORÍFICOS es {media} años")

elif opc == 4:
    #Opción 4: Actualización de datos

    #Asigno a la columna ratings del dataframe general el mismo valor multipliclado por 2.
    userRatingsMoviesDF['rating'] = 2*userRatingsMoviesDF['rating']
    
    #Exportamos el DataFrame a un CSV con separador de ,.
    userRatingsMoviesDF.to_csv("d:/usuarios/Users/EstherLanchaCañas/OneDrive - IES Luis Braille/Entornos de Desarrollo\Entregable 4 - Control de versiones con Git/Proyecto/miProyecto/datos/Ejercicio4_EstherLanchaCanas.csv", sep=",")
