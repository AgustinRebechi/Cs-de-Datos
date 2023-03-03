#infomr_final.py

# Imports

from fileparse import parse_csv
import lote
import formato_tabla
import sys


# Funciones

def leer_camion(nombre_archivo):
    with open(nombre_archivo) as f:
        camion_dicts = parse_csv(f, types = [str, int, float])
        camion = [lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]        
        return camion

def leer_precios(nombre_archivo):
    with open(nombre_archivo) as f:
        precios =  parse_csv(f, types = [str, float], has_headers = False) 
        header = ['producto', 'precio']
        precios = [dict(zip(header,tupa)) for tupa in precios]        
        return precios

def hacer_informe(camion, precios):
    lista = []
    for a in camion:
        for b in precios:
            try:
                if a.nombre == b['producto']:
                    producto = a.nombre
                    cantidad = int(a.cajones)
                    precio = a.precio
                    cambio = b['precio'] - precio
                    info = (producto, cantidad, precio, cambio)
                    lista.append(info)
            except KeyError:
                continue
    return lista

def imprimir_informe(data_informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas con (nombre, cajones, precio, cambio) 
    '''
    formateador.encabezado(['Nombre','Cajones','Precio','Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)

def informe_camion(archivo_camion, archivo_precios, fmt = 'csv'):
    '''
    Crea un informe con la carga de un camión
    a partir de archivos camion y precio.
    El formato predeterminado de la salida es .txt
    Alternativas: .csv o .html
    '''
    # Lee archivos de datos
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)

    # Crea la data del informe
    data_informe = hacer_informe(camion, precios)

    # Imprime el informe
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(data_informe, formateador)


# Funcion principal    

def f_principal(argumentos):
    if len(sys.argv) != 4:
        camion = '../Data/camion.csv'
        precios = '../Data/precios.csv'
        fmt = 'txt'        
    else:
        camion = sys.argv[1]
        precios = sys.argv[2]
        fmt = sys.argv[3]
        
    informe_camion(camion, precios, fmt)

if __name__ == '__main__':    
    f_principal(sys.argv)
    


    






