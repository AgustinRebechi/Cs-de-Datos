lista = ['banana', 'manzana', 'mandarina']


def geringoso(lista):
    vocales = ['a', 'e', 'i', 'o', 'u']
    palabra_nueva = ''
    for k in lista:
        palabra_nueva = palabra_nueva + k
        if k in vocales:
            palabra_nueva = palabra_nueva + 'p' + k
    return(palabra_nueva)
        
dic = {}
for d in lista:
    dic[d] = geringoso(d)
print(dic)
    



    