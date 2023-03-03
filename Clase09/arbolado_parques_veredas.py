# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 18:32:38 2022

@author: rebe_
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# 1
directorio = '../Data'
archivo_veredas = 'arbolado-publico-lineal-2017-2018.csv'
archivo_parques = 'arbolado-en-espacios-verdes.csv'
fname1 = os.path.join(directorio,archivo_veredas)
fname2 = os.path.join(directorio,archivo_parques)
df_veredas = pd.read_csv(fname1)
df_parques = pd.read_csv(fname2)

# 2

# veredas

df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'] == 'Tipuana tipu'].copy()
df_tipas_veredas = df_tipas_veredas[['diametro_altura_pecho', 'altura_arbol']]
df_tipas_veredas = df_tipas_veredas.rename(columns={'diametro_altura_pecho': 'diametro', 'altura_arbol':'altura'})

# parques

df_tipas_parques = df_parques[df_parques['nombre_cie'] == 'Tipuana Tipu'].copy()
df_tipas_parques = df_tipas_parques[['diametro', 'altura_tot']]
df_tipas_parques = df_tipas_parques.rename(columns={"altura_tot": "altura"})

# 3

df_tipas_parques['ambiente'] = 'parque'
df_tipas_veredas['ambiente'] = 'veredas'

# 4

df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])

# 5 y 6

def plot():
    df_tipas.boxplot('diametro',by = 'ambiente')
    df_tipas.boxplot('altura',by = 'ambiente')
    
grafico = plot()



