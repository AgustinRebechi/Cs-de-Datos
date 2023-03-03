#solucion_de_errores.py
#Ejercicios de errores en el codigo
#%%
#Ejercicio 3.1 Función tiene_a()
#Comentario: El error era de tipo semántico y estaba ubicado en el "return False"
# El error ocurre por que va iterando letra por letra y al ser "false" la primera corta el "while"

# Corrección:
# 1) Lo corregí comentando el "if" con "print(f'detecto {expresion[i]}')
# 2) Comenté el "return False" que cortaba el while
# 3) Agregué un "if" en el "else" para que cuando haya detectado la ultima letra de la iteracion y
#todavía no haya encontrado un "a" de un print avisando que no hay un "a". Ahora no habría problemas
# con el "return False" por que no necesito que itere mas y puede cortar el while sin problemas. 

# A continuación el código corregido:
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            print(f'Detecto una "{expresion[i]}" en esta expresion') 
            return True
        else:            
            #return False# |Este return cortaba el while| 
            if i == n-1:
                print(f'No encuentro una "a" en esta expresión')
                return False            
        i += 1
        

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')

#%%
#Ejercicio 3.2 Función tiene_a()

#Comentario: El error era de tipo sintáctico

#Correrción:
#1) Falta " : " en la linea de definicion de función
#2) Falta " : " en la linea de while
#3) Falta " : " en la linea de if
#4) Mal escrrito "False"


# A continuación el código corregido:
def tiene_a(expresion): # |Acá faltaba " : "|
    n = len(expresion)
    i = 0
    while i<n: # |Acá faltaba " : "|
        if expresion[i] == 'a': # |Acá faltaba " : "|
            return True
        i += 1
    return False # |Acá estaba mal escrito| 

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')
#%%
#Ejercicio 3.3 Función tiene_uno()

#Comentario: El error es de tipo sintáctico y estaba en el dato "1984"
#Al poner en la función un dato tipo "int" daba error porque solo admite
#de tipo "string"

#Corrección:
#1) Añadir comillas a "1984"


# A continuación el código corregido:
def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno('1984') # |Acá le faltaban las comillas a 1984|
#%%
#Ejercicio 3.4 Función suma()
#Comentario: El error es de tipo semántico y estaba en no colocar
#un return a la función, al hacer la suma el resultado no existía
#y por eso daba "None"
#Corrección:
#1) Darle un return a la función y que este devuelva "c"

# A continuación el código corregido:
def suma(a,b):
    c = a + b
    return c # |Acá faltaba el return|

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")
#%%
#Ejercicio 3.5 Función leer_camion()
#Comentario: El error es de tipo semántico, el problema es que los
#valores se remplazan cada vez que se iteran, es por eso que mostraba
#solamente la ultima fila del dataset

#Corrección:
#1) Utilizar dict(zip())

# A continuación el código corregido:
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = dict(zip(encabezado, (fila[0], int(fila[1]), float(fila[2])))) # | Remplacé por dict(zip()) |
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)























