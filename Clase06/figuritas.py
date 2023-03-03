import random
import numpy as np
import matplotlib.pyplot as plt

figus_total = 670
figus_paquete = 5
n_repeticiones = 1000

def crear_album(figus_total):
    album = np.zeros(figus_total, dtype=np.int64)
    return album
    
def album_incompleto(A):
    copia = A.copy()
    copia = np.sort(copia)
    if copia[0] == 0:
        return True
    return False

def comprar_figu(figus_total):
    comprada = []
    comprada.append(random.randint(0,figus_total-1))
    return comprada        

def cuantas_figus(figus_total):    
    compras = 0
    album = crear_album(figus_total)
    while album_incompleto(album) == True:
        compra = comprar_figu(figus_total)
        album[compra] += 1
        compras += 1 
    return compras

def experimento_figus(n_repeticiones, figus_total):
    lista = []
    for i in range(n_repeticiones):
        a = cuantas_figus(figus_total)
        lista.append(a)
    promedio = sum(lista)/len(lista)
    return promedio
        
#--------

def comprar_paquete(figus_total, figus_paquete):
    pack = np.array([0]*figus_paquete)
    for i in range(figus_paquete):
        pack[i] = random.randint(1,figus_total)
    return pack

def cuantos_paquetes(figus_total, figus_paquete):
    cant_compras = 0
    album = crear_album(figus_total)
    while album_incompleto(album) == True:
        paquete = comprar_paquete(figus_total, figus_paquete)
        cant_compras += 1
        for i in range(figus_paquete):
            album[paquete[i]-1] += 1
    return cant_compras






    
    
    

pack = comprar_paquete(figus_total, figus_paquete)
cuanto = cuantos_paquetes(figus_total, figus_paquete)
exp_packs = [cuantos_paquetes(figus_total, figus_paquete) for i in range(n_repeticiones)]
pack850 = np.sum([1 for i in range(n_repeticiones) if cuantos_paquetes(figus_total, figus_paquete) <= 850])
#compras = cuantas_figus(figus_total)
#promedio = experimento_figus(n_repeticiones, figus_total)

plt.hist(exp_packs, bins=150)
plt.ylabel('Probabilidad')
plt.xlabel('Paquetes')
plt.show()
