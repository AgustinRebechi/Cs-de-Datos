import csv
import sys


def costo_camion(nombre_archivo):
    costo = 0
    f = open(nombre_archivo, 'rt')
    rows = csv.reader(f)
    header = next(rows)    
    for line in rows:
        try:
            cantidad = float(line[1])
            precio = float(line[2])
            costo += cantidad * precio
        except ValueError:
            print(f'no se puede interpretar: {rows}')
    return (costo)
    f.close()
            
if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'            
            



        
costo = costo_camion(nombre_archivo)     
print('Costo total:', round(costo, 2))