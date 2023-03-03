import csv
from collections import Counter

file = '../Data/arbolado-en-espacios-verdes.csv' 
algunos_parques = ['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']

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

#def especie_promedio_mas_inclinada(lista_arboles):
 #   promedio = []
  #  ejemplares = []

    #ejemplares = especies(lista_arboles)
    #del set                        
   # for especie in lista_arboles:        
    #    inclinacion = obtener_inclinaciones(lista_arboles, especie)
     #   promedio.append(round(sum(inclinacion)/float(len(inclinacion)),2))
    #promedios = dict(zip(ejemplares, promedio))
    #return promedios
        
    
#error =
       
   #ejemplares = especies(lista_arboles)

#TypeError: 'set' object is not callable           
       

    
            
            
        
#Input#        
parque = input(f'ingrese el parque(Ejemplo: GENERAL PAZ): ')
especie = input(f'ingrese la especie(Ejemplo: "Jacarandá"): ')

#llaamada a funciones
lista_arboles = leer_parque(file, parque)
especies = especies(lista_arboles)
contar_ejemplares = contar_ejemplares(lista_arboles,2)
alturas = obtener_alturas(lista_arboles, especie)
inclinaciones = obtener_inclinaciones(lista_arboles, especie)
mas_inclinado = especimen_mas_inclinado(lista_arboles)
#promedios = especie_promedio_mas_inclinada(lista_arboles)

#Prints
print(contar_ejemplares.most_common(5))
print('max:',max(alturas), 'promedio:', sum(alturas)/len(alturas))
print('especimen mas inclinado:', mas_inclinado)
#print('Mayor promedio:' , promedios)
