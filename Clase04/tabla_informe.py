import csv


def leer_camion(nombre_archivo):       
    camion = [] 
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                lote = dict(zip(headers, row))
                camion.append(lote)
            except IndexError:
                continue
        return camion

def leer_precios(nombre_archivo):
    precios = []
    cabeza = ['producto', 'precio']
    with open(nombre_archivo, 'rt') as file:
        rows = csv.reader(file)        
        for linea in rows:
            try:
                producto_precio = dict(zip(cabeza, linea))                         
                precios.append(producto_precio)
            except IndexError:
                break
        return precios

def hacer_informe(camion, precios):
    informe = []
    for itemA in camion:
        for itemB in precios:
            try:
                if itemA['nombre'] == itemB['producto']:
                    producto = itemA['nombre']
                    cantidad = int(itemA['cajones'])
                    precio = round(float(itemA['precio']),2)
                    cambio = round(float(itemB['precio']) - precio,2)
                    cabezera = (producto, cantidad, precio, cambio)
                    informe.append(cabezera)
            except KeyError:
                continue
    return informe

camion = leer_camion('../Data/camion.csv')
precios = leer_precios('../Data/precios.csv')
informe = hacer_informe(camion, precios)

headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
print(f'{headers[0]:>10s} {headers[1]:>10} {headers[2]:>10s} {headers[3]:>10s}')
print(f'---------- ---------- ---------- ----------')
for nombre, cajones, precio, cambio in informe:
    precio =  '$' + str(precio)
    print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')


    







  


 