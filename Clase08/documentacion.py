
def valor_absoluto(n):
    '''  
    Devuelve valor absoluto de n
    ----------
    Pre: un valor n real
    Pos: un valor n positivo
    '''
    if n >= 0:
        return n
    else:
        return -n
    
#%%

def suma_pares(l):
    '''
    Devuelve la suma de los numeros pares de una lista
    -----------
    Pre: valores reales en la lista
    Pos: si el elemento es par, hace res += e
         si el elemento es impar suma 0
    '''
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res

#%%

def veces(a, b):
    '''
    Devuelve una multipiclación entre a y b
    -----------
    Pre: a y b deben ser numeros reales
    Pos: producto entre a y b    
    '''
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res

#%%

def collatz(n):
    '''
    Funcion de conjetura de collatz
    -----------
    Pre: n debe ser un numero real positivo 
    Pos: si n es par, se divide entre 2
         si n es impar, hace 3 * n + 1            
    '''    
    res = 1
    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1
    return res