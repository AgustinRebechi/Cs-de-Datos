import random
import matplotlib.pyplot as plt
import numpy as np


n = 999
temp = 37.5
error = 0.2
media = 0

m = []

 

def medir_temp(n, mu, sigma, medreal):
    lista = []
    for i in range(n):
        temp = round(random.normalvariate(mu, sigma) + medreal,5)
        lista.append(temp)
    return lista



lista = medir_temp(n, media, error, temp)


lista = np.array(medir_temp(n, media, error, temp))
np.save('Data/Temperaturas.npy', lista)



maximo = max(lista)
minimo = min(lista)
promedio = sum(lista)/n

m = np.sort(lista)
mediana = m[n//2]


print(f'maximo:' , maximo)
print(f'minimo:' , minimo)
print(f'promedio:' , promedio)
print(f'mediana:' , mediana)





plt.hist(lista, bins = 100, density=True) 



