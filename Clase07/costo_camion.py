#costo_camion.py
import informe_funciones


def costo_camion(nombre_archivo):
    costo = 0
    fila = informe_funciones.leer_camion(nombre_archivo)   
    for n_fila, linea in enumerate(fila, start=1):
        try:
            cantidad = int(linea['cajones'])
            precio = float(linea['precio'])
            costo += cantidad * precio
        except ValueError:
            print(f'Fila {n_fila}: No puede interpretar: {linea}')
    return (costo)
            
costo = costo_camion('../Data/camion.csv')     
print('Costo total:', round(costo, 2))