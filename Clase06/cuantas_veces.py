from collections import Counter

text = 'Creo que a veces es la gente de la que nadie espera nada, la que nadie hace nada'

def minuscula(text):
    minuscula = text.lower()
    return minuscula

def limpiaso(minuscula):
    limpiaso = minuscula.replace(',','').replace('.','')
    limpiaso = limpiaso.split(' ')
    return limpiaso



def contador(limpiaso, palabra):
    contar = Counter()    
    for palabras in limpiaso:
        if palabras == palabra:
            contar[palabras] +=1
    contar = contar[palabra]
    print(f'{palabra} aparece {contar} veces')
    return contar

def contador_palabras(texto):
    palabras = {}
    for palabra in texto:
        if palabra in palabras:
            palabras[palabra] += 1
        else:
            palabras[palabra] = 1
            
    print(palabras)
    return palabras
        


minuscula = minuscula(text)
limpiaso = limpiaso(minuscula)
contar = contador(limpiaso, 'nadie')
palabras = contador_palabras(limpiaso)
    
            
        
        
        
    