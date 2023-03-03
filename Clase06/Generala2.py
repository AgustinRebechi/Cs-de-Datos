import random
import numpy as np
import matplotlib as plot
from collections import Counter
import os


def tirada():
    tirada = [random.randint(1,6) for i in range(5)]
    return tirada

def es_generala(tirada):
    return max(tirada) == min(tirada)

def mas_repetido(tirada):
    dados = Counter()
    for dado in tirada:
        dados[dado] += 1
    mejor = dados.most_common(1)[0]
    dado = mejor[0]
    freq = mejor[1]
    return [dado]*freq

def generala_c():
    lista = []
    contador = 0
    while es_generala(tirada) == False:
        while len(lista) < 4:
            t = tirada()
            m = mas_repetido(t)
            lista.append()
            contador += 1
    return lista, contador
        


    
    

tirada = tirada()
generala = es_generala(tirada)
mas_repetido = mas_repetido(tirada)
sex = generala_c()


        
    