# random_walk.py

# Imports
import numpy as np
import matplotlib.pyplot as plt

# Variables

N = 100000

lista = []


# Funciones 

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()

def mas_lejos(lista):
    comparador = 0
    mas_lejos = []    
    for i in lista:        
        if np.absolute(np.amin(i)) > np.absolute(comparador) or np.absolute(np.amax(i)) > np.absolute(comparador):
            mas_lejos = i
            comparador = i[-1]            
    return mas_lejos 

def mas_cerca(lista):
    comparador = np.amax(np.absolute(lista[0]))
    mas_cerca = []
    for i in lista:
        if np.amax(np.absolute(i)) < np.absolute(comparador):
            mas_cerca = i
            comparador = np.amax(i)    
    return mas_cerca


# Plots

def doce_lineas():
    for i in range(12):
        linea = randomwalk(N)
        lista.append(linea)
        plt.subplot(2,1,1)
        plt.plot(lista[i])
        plt.ylim(-750,750)
        plt.xticks([])
        plt.yticks([-500,0,500])
        plt.title('12 Caminatas al azar')

def caminata_mas_lejana():
    plt.subplot(2,2,3)
    plt.plot(mas_lejos(lista))
    plt.ylim(-750,750)
    plt.xticks([])
    plt.yticks([-500,0,500])
    plt.title('La caminata que más se aleja')

def caminata_que_menos_se_aleja():
    plt.subplot(2,2,4)
    plt.plot(mas_cerca(lista))
    plt.ylim(-750,750)
    plt.title('La caminata que menos se aleja')
    plt.xticks([])
    plt.yticks([])

        
doce = doce_lineas()
lejana = caminata_mas_lejana()
menos_lejana = caminata_que_menos_se_aleja()
    



