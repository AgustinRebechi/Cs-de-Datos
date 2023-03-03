import csv


def leer_camion(nombre_archivo):
       
    camion = [] 
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for n_fila, rows in enumerate(rows, start=1):
            record = dict(zip(header, rows))            
            try:
                lote 
                
        return camion

camion = leer_camion('../Data/fecha_camion.csv')  




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

precios = leer_precios('../Data/precios.csv')




    
costo_camion = 0
venta = 0    
for lineaA in camion:
    costo_camion += lineaA['cajones'] * lineaA['precio']
    for lineaB in precios:
        try:
            if lineaB['producto'] == lineaA['nombre']:
                venta += int(lineaA['cajones']) * float(lineaB['precio'])
        except KeyError:
            break
    
    
    

print(f'Costos $ {costo_camion}')
print(f'Ventas: $ {venta}')
print('Balance: $', round(venta - costo_camion,3))


 