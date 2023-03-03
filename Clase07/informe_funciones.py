# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 21:22:46 2022

@author: rebe_
"""
#informe_funciones.py
import csv
from fileparse import parse_csv

# Funciones

def leer_camion(nombre_archivo):       
    camion = parse_csv(nombre_archivo, types=[str,int,float])
    return (camion)
    
def leer_precios(nombre_archivo):
    precios = []
    venta = parse_csv(nombre_archivo, types=[str,float], has_headers=False)
    cabeza = ['producto', 'precio']
    for unidad in venta:
        venta = dict(zip(cabeza, unidad))
        precios.append(venta)
    return (precios)

def hacer_informe(camion, precios):
    informe = []
    for itemA in camion:
        for itemB in precios:
            try:
                if itemA['nombre'] == itemB['producto']:
                    producto = itemA['nombre']
                    cantidad = int(itemA['cajones'])
                    precio = round(float(itemA['precio']),2)
                    cambio = round(float(itemB['precio']) - precio,2)
                    cabezera = (producto, cantidad, precio, cambio)
                    informe.append(cabezera)
            except KeyError:
                continue
    return informe

def imprimir_informe(informe):
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print(f'{headers[0]:>10s} {headers[1]:>10} {headers[2]:>10s} {headers[3]:>10s}')
    print(f'---------- ---------- ---------- ----------')
    for nombre, cajones, precio, cambio in informe:
        precio =  '$' + str(precio)
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')
    return 

def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    camion = leer_camion('../Data/camion.csv')
    precios = leer_precios('../Data/precios.csv')
    informe = hacer_informe(camion, precios)
    imprimir_informe(informe)

# llamada de funciones

informe_camion('../Data/camion.csv', '../Data/precios.csv')


