frase = 'Todos somos programadores'
palabras = frase.split()

a = 0

for palabra in palabras:
    if palabra[-1] == 'o':
        palabras[a] = palabra[:-1] + 'e'
    elif (len(palabra) >= 2) and (palabra[-2] == 'o'):
        palabras[a] = palabra[:-2] + 'e' + palabra[-1:]
    
    a = a + 1
        
frase_t = ' '.join(palabras)
print(frase_t)