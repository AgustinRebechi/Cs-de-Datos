# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 20:46:18 2022

@author: rebe_
"""

#bbin.py


def ordena_listas(lista):
    lista = sorted(lista)
    return lista

def insertar(lista, x):
    if x in lista:
        print(lista.index(x))
    else:
        lista.append(x)
        lista = sorted(lista)
    return lista

def donde_insertar(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    
    
    if pos != -1:
        return pos
    else:
        if lista[medio] > x:            
            return medio
        else:
            return medio+1
    

e = [0,2,4,6]
ordenada = ordena_listas(e)
position = donde_insertar(e, 3)
