import csv
from collections import Counter
import os
import matplotlib.pyplot as plt
import numpy as np

file = '../Data/arbolado-en-espacios-verdes.csv' 
algunos_parques = ['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']

os.path.join('..', 'Data', 'arolado-en-espacios-verdes.csv')

#funciones
def leer_parque(nombre_archivo, parque=False):
    parques = []
    otros = []
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        linea = csv.reader(f)       
        header = next(linea)
        for n_arbol, arbol in enumerate(linea, start=1):
            record = dict(zip(header, arbol))           
            otros.append(record)
            if record['espacio_ve'] == parque:
                parques.append(record)
    return parques
            
def especies(lista_arboles):
    especies_totales = []
    especies_unicos = []
    for arbol in lista_arboles:
        especies_totales.append(arbol['nombre_com'])
    especies_unicos = set(especies_totales)
    especies_unicos_2 = especies_unicos
    return especies_unicos_2

def contar_ejemplares(lista_arboles, most_common_ingrese_nEntero=None):
    contador = Counter()
    for especie in lista_arboles:
        contador[especie['nombre_com']] += 1
    return contador

def obtener_alturas(lista_arboles, especie):
    alt_arboles = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            alt_arboles.append(float(arbol['altura_tot']))
    return alt_arboles

def obtener_inclinaciones(lista_arboles, especie):
    inclinaciones = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            inclinaciones.append(float(arbol['inclinacio']))
    return inclinaciones

def especimen_mas_inclinado(lista_arboles):
    mas_inclinado = []
    valor = 0
    for arbol in lista_arboles:
        if valor <= float(arbol['inclinacio']):
            valor = float(arbol['inclinacio'])
            especie = arbol['nombre_com']
            mas_inclinado = [especie, valor]
        else:
            continue
    return mas_inclinado

def especie_promedio_mas_inclinada(lista_arboles):
    mas_inclinado = []
    especie = []
    especie = especies(lista_arboles)
    for tipo in especie:
        inclinado = obtener_inclinaciones(lista_arboles, tipo)
        mas_inclinado.append(round(sum(inclinado)/float(len(inclinado)),2))
    inclinaciones_dict = dict(zip(especie, mas_inclinado))
    return inclinaciones_dict


          
       
#-----------------CLASE 5 -----------------
    
def leer_arboles(nombre_de_archivo):
    f = open(nombre_de_archivo, 'rt', encoding = "utf8")
    rows = csv.reader(f)
    header = next(rows)
    indices = [header.index(ncolumna) for ncolumna in header]
    arboleda = [{ncolumna: row[index] for ncolumna, index in zip(header, indices)} for row in rows]
    return arboleda

def medidas_de_especies(especies, arboleda):
    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    datos_AyD = {}
    for especie in especies:
        Alto = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == especie] 
        Diametro = [float(arbol['diametro']) for arbol in arboleda if arbol['nombre_com'] == especie]
        datos_AyD[especie] = (Alto, Diametro)
    return datos_AyD




#Input#        
parque = algunos_parques[0]
especie = 'Jacarandá'

#llaamada a funciones
lista_arboles = leer_parque(file, parque)
especies_unicos_2 = especies(lista_arboles)
contar_ejemplares = contar_ejemplares(lista_arboles,2)
alturas = obtener_alturas(lista_arboles, especie)
inclinaciones = obtener_inclinaciones(lista_arboles, especie)
mas_inclinado = especimen_mas_inclinado(lista_arboles)
#promedios = especie_promedio_mas_inclinada(lista_arboles)
arboleda = leer_arboles(file)
datos_AyD = medidas_de_especies(especies, arboleda)
#datoss_AyD2 = medidas_de_especies2(especies, arboleda)





Alto = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == especie] 
Alto_Diametro = [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie ] 

#Prints
print(contar_ejemplares.most_common(5))
print('max:',max(alturas), 'promedio:', sum(alturas)/len(alturas))
print('especimen mas inclinado:', mas_inclinado)
#print('Mayor promedio:' , promedios)



#-----------------CLASE 6--------------------

def scatter_hd(lista_de_pares):
    pares = np.array(lista_de_pares)
    h = pares[:,0]
    d = pares[:,1]
    return d,h



d,h = scatter_hd(Alto_Diametro)

plt.scatter(d,h, c='purple',alpha=0.1)
plt.xlabel('diametro (cm)')
plt.ylabel('alto (m)')
plt.title('Relación diámetro-alto para Jaracandás')
plt.xlim(0,100)
plt.ylim(0,30)


especiardas = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']  
for i, especie in enumerate(especiardas):
    plt.subplot(131+i)
    plt.scatter(tuple(datos_AyD[especiardas[i]][1]), tuple(datos_AyD[especiardas[i]][0]), c='purple', alpha=0.1)
    plt.xlim(0, max(datos_AyD[especiardas[0]][1]))
    plt.ylim(0, max(datos_AyD[especiardas[0]][0]))
    plt.xlabel('Diametro (cm)', fontsize=8)
    if i == 0:
        plt.ylabel('Alto (m)', fontsize=8)
    plt.title(f'{especie}', fontsize = 8)
    plt.suptitle('Relación diámetro-alto', fontsize = 14)
    
  

