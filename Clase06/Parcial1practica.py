#1
oso = 'oso'

def una_funcion():
    if 'a' in 'trolo':
        print('si')
        return True
    else:
        print('no')
        return False

si = una_funcion()

#2
mi_var = {'cero': 0}
print(mi_var[0])


#%%
#3

for i in range(9):
    print(i)

#%%

def funct(a,b):
    c = a + b
    return c
    
# le falta el return moster por eso da none    
    
c = 3
c = funct(2,3)
print(c)

#%%


a = [1]
b = [2,3]
c = [4,5,6]
k = [a,b,c]
k[1].append(7)
print(k)

#%%

n = 5
lista = [1]*n
for i in range(1,n):
    lista [i] = lista[i-1] + lista[i] + lista[i+1] 

#%%

n = 5
lista = [1]*n
for i in range(n):
    if i + 1 < n and lista[i+1]==1:
        lista[i] += lista[i+1]
lista[4] = 2
        
#%%

lista = [1,2,3]
n = 2
for k in range(10):
    try:
        if k<n and lista[k]==3:
            print('Caso 1')
    except Exception:
        print('Caso 2')
        
#no imprime nada por que no llega al except

#%%

r = [x*y for x in range(-10,10) if x>0 and x%2==1 for y in [1,0,-1] if y!=0]

#????

#%%

a = ['n','e','p']
b = ['R', 43, 78]
d = dict(zip(a,b))
if (d['e'])%2==0:
    print('par')
else:
    print('impar')
    
#%%

for i,c in enumerate('pavada'):
    if i != (i//2)*2:
        print(c,end='')
        
#%%

i = 0
suma = 0
#while i <= 10:
 #   suma += i
    
#print(suma)

#%%

d = {}
#%%

def func(a):
    a += 1
    
a = 1
a = func(a)
a = a + 1

# muy importante, al no tener return, nada mas uno no existe

#%%

lista = [2,4,6,8,10]
{x: x**2 for x in range(10) if x in lista}

#%%

def suma(a,b):
    c = a + b 

print(suma(1,2))

