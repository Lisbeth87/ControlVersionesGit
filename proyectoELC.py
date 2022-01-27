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