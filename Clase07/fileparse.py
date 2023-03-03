# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 17:24:15 2022

@author: rebe_
"""

# fileparse.py
import csv

def parse_csv(nombre_archivo, select = None, types=None, has_headers=True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        # Si tiene Headers
        if has_headers:
            # Lee los encabezados del archivo
            encabezados = next(filas)
    
            # Si se indicó un selector de columnas,
            #    buscar los índices de las columnas especificadas.
            # Y en ese caso achicar el conjunto de encabezados para diccionarios
    
            if select:
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                encabezados = select
            else:
                indices = []
    
            registros = []
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                # Filtrar la fila si se especificaron columnas
                if indices:
                    fila = [fila[index] for index in indices]
                # Tipos            
                if types:
                    fila = [func(val) for func, val in zip(types, fila)]
                    
                # Armar el diccionario
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
                
        # Si no tiene Headers
        else:
            registros= []
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                # Tipos en forma de tuplas            
                if types:
                    fila = tuple([func(val) for func, val in zip(types, fila)])
                # Lista de tuplas
                registros.append(tuple(fila))
            

    return registros

precios = parse_csv('../Data/precios.csv', select=['nombre','cajones'], types=[str, float], has_headers=False)