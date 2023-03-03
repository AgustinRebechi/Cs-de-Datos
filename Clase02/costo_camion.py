import csv


def costo_camion(nombre_archivo):
    costo = 0
    f = open('../Data/camion.csv', 'rt')
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
            
            
            



        
costo = costo_camion('../Data/camion.csv')     
print('Costo total:', round(costo, 2))