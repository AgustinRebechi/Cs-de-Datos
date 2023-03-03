# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 19:24:15 2022

@author: rebe_
"""

from fileparse import parse_csv
camion = parse_csv('../Data/camion.csv', select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
lista_precios = parse_csv('../Data/precios.csv', types = [str, float], has_headers = False)
precios = dict(lista_precios)

