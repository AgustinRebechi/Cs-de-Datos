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

def busqueda_lineal_lordenada(lista, e):
    posicion = -1 # Por ahora no existe
    contador = 0
    for i in lista:
        if busqueda > float(e):
            break
        else:
            posicion = i
        i+=1
    return posicion

def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos
    
            

#namber = 5
#l = [1,2,3,4,5,6,7,8,9,11]



