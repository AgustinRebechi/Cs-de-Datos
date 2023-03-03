def buscar_elemento(lista, numero):
    no = 0
    for i, busqueda in enumerate(lista, start=1):
        if busqueda == float(numero):
            no = no + 1
            break
    if no == 0:
        no = -1
    return no

def maximo(lista):
    m = 0
    for e in lista:
        if e > m:
            m = e 
    return m

def minimo(lista):
    f = max(lista)
    for e in lista:
        if e <= f:
            f = e
    return f

namber = input(f'que numero desea encontrar monstruo: ')
l = [1,2,3,4,5,6,7,8,9,11]

no = buscar_elemento(l,namber)
m = maximo(l)
f = minimo(l)

print(f'su numero se encuentra: {no} veces')
print(f'el maximo de la lista es {m}')
print(f'el minimimo del la lista es {f}')



