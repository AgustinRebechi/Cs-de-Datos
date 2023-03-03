# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 19:49:07 2022

@author: rebe_
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns
import os

directorio = '../Data'
archivo = 'arbolado-publico-lineal-2017-2018.csv'
fname = os.path.join(directorio, archivo)
df = pd.read_csv(fname)



# 9.6
 
cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
df_lineal = df[cols_sel]

cant_ejemplares = df_lineal['nombre_cientifico'].value_counts()
cant_ejemplares.head(10)

especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']
df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]

# 9.7 

#df_lineal_seleccion.boxplot('diametro_altura_pecho', by = 'nombre_cientifico')
df_lineal_seleccion.boxplot('altura_arbol', by = 'nombre_cientifico')
