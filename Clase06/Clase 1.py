import random

dado = random.randint(1,6)

print(dado)

#%%
#Generala

import random

tirada=[]

for i in range(5):
    tirada.append(random.randint(1,6))

print(tirada)

#%%
# Con compresion de listas
import random

[random.randint(1,6) for i in range(5)]

#%%
# Con strings+

import random

caras = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis']
tiro = random.choice(caras)
print(tiro)

#%%
#Con funciones

def tirar():
    tirada=[]
    for i in range(5):
        tirada.append(random.randint(1,6))
    return tirada

def es_generala(tirada):
    return max(tirada)==min(tirada)

#%%

N=1000000
salio_generala_servida = [es_generala(tirar()) for i in range(N)]
G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
                    
#%%
#compresion de listas

N = 100000
prob=sum([es_generala(tirar()) for i in range(N)])/N

#%%
#suma de 5 dados con gráficos re lindos

N = 10000000
sumas = [sum(tirar()) for i in range(N)]

import matplotlib.pyplot as plt

plt.hist(sumas,bins=100)#density=True)

#%%
#Sin reposicion
#doble valores
import random 

palos = ['oro', 'copa', 'espada', 'basto']
valores = [1,2,3,4,5,6,7,8,9,10,11,12]

          #tuplas                    #doble iteracion
naipes = [(valor, palo) for valor in valores for palo in palos]

#reparte 3 cartas random
random.sample(naipes, k=3)

#Mezcla las cartas (naipes)
random.shuffle(naipes)

#%%

#random.random() genera un punto aleatorio entre 0 y 1
# Encontrar pi usando puntos aleatorios

def generar_punto():
    x = random.random()
    y = random.random()
    return x,y 

N = 20000000
M = 0

for i in range(N):
    x, y = generar_punto()
    if x**2 + y**2 < 1:
        M += 1
print(f' pi {4*M/N:.5f}')

#%%
# Otros tipos de graficos

plt.clf()
plt.scatter(Xi,Yi, s=1)
plt.scatter(Xo, Yo, s=1)

#%%
#REPASO

#random.randint()        returnea un numero rando entre los valores dados

#random.shuffle()        Toma una secuencia y returnea una mezcla aleatoria

#random.choice()         un elemento  
#random.choices()        varios elementos

#random.sample()         k sin repeticion 
#random.random()         returnea un numero random entre 0 y 1
#random.gauss(mu,sigma)
#seed()                  inicia un generador de numereos aleatorios    



#%%
import random
caras = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis']
print(random.choices(caras,k=2))

print(random.choice(caras))
#%%

import random

valores = [1,2,3,4,5,6,7,8,9,10,11,12]
palos = ['oro','copa', 'espada', 'basto']
naipes = [(valor, palo) for valor in valores for palo in palos]

print(random.sample(naipes, k=3))

#%%
import random

valores = [1,2,3,4,5,6,7,8,9,10,11,12]
palos = ['oro','copa', 'espada', 'basto']
naipes = [(valor, palo) for valor in valores for palo in palos]
random.shuffle(naipes)

print(naipes)

n1 = naipes.pop()
n2 = naipes.pop()
n3 = naipes.pop()
print(f'Repartí el {n1[0]} de {n1[1]}, el {n2[0]} de {n2[1]} y el {n3[0]} de {n3[1]}. Quedan {len(naipes)} naipes en el mazo.')












