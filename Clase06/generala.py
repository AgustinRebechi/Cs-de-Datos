import random

N = 100000

def tirar(n):
    tirada = [random.randint(1,6) for i in range(5)]
    return tirada

def es_generala(tirada):
    return max(tirada) == min(tirada)

def prob_generala():
    tiradas = 0
    num = 0
    dados = 5      
    while dados != 0 and tiradas < 3:
        guardado = [0]*6
        tirada = tirar(N)
        for i in range(1,7):
            for valor in tirada:
                if valor == i:
                    guardado[i-1] += 1
        if tiradas == 0:
            maximo = max(guardado)
            num = guardado.index(maximo) + 1
            dados -= maximo
        else:
            dados -= guardado[num-1]
        tiradas += 1    
    if tiradas == 2 and dados == 0:
        return True
    return False


G = sum([prob_generala() for i in range(N)])
prob = G/N

print(prob)
print(f'Tiré {N} veces, de las cuales {G} saqué generala en maximo tres tiros.')
print(f'Entonces podemos estimar la probabiliudad de sacar generala {prob:.6f}')

