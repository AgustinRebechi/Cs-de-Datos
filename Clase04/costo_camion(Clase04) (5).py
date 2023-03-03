import csv


def costo_camion(nombre_archivo):
    costo = 0
    f = open(nombre_archivo, 'rt')
    rows = csv.reader(f)
    header = next(rows)    
    for n_fila, line in enumerate(rows, start=1):
        record = dict(zip(header, line))
        try:
            cantidad = int(record['cajones'])
            precio = float(record['precio'])
            costo += cantidad * precio
        except ValueError:
            print(f'Fila {n_fila}: No puede interpretar: {line}')
    return (costo)
    f.close()
            
            
            



        
costo = costo_camion('../Data/missing.csv')     
print('Costo total:', round(costo, 2))