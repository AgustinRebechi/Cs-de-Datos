import os
import sys

def archivos_png(directorio):
    '''
    recorre directorio y detecta .png

    '''
    pngs = []
    for root, dirs, files in os.walk(directorio):
        for name in files:
            png = os.path.join(root, name)
            if str(png)[-4:] == '.png':
                pngs.append(png)
    print(pngs)
    return pngs

def main(directorio):
    '''
    Funcion principal

    '''
    archivos_png(directorio)
    
if __name__ == '__main__':
    '''  
    sys
    
    si hay un arg lo interpreta como directorio
    '''
    if len(sys.argv) == 2:
        directorio = sys.argv[1]
    else:
        directorio = '../Data/ordenar'
    main(directorio)

        
    
