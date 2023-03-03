import csv
def leer_precios(nombre_archivo):
    precios = {}
    with open(nombre_archivo, 'rt') as file:        
        for linea in file:
            try:
                row = linea.split(',')                         
                precios[row[0]] = float(row[1])
            except IndexError:
                break
        return precios
            
                
                
            
                
            
                
                
            
            
            
precios = leer_precios('../Data/precios.csv')
print(precios)
