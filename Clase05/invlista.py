l1 = [1, 2, 3, 4, 5]
l2= ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']

def invertir_lista(lista):
    invertida = []
    for i, e in enumerate(lista, start=1):
        e = lista[-i]
        invertida.append(e)
    return invertida

invertida = invertir_lista(l2)

print(invertida)