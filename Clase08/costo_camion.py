#costo_camion.py
import informe_final


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

def f_principal():

if __name__ == '__main__':
    import sys
    f_principal(sys.argv)
            
costo = costo_camion('../Data/camion.csv')     
print('Costo total:', round(costo, 2))