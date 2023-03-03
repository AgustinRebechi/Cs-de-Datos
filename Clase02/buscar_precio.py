import csv

def  buscar_precio(fruta):
    f = open('../Data/precios.csv', 'rt')
    rows = csv.reader(f)
    precio = None
    for line in (rows):
        try:
            if line[0] == fruta:
                precio = float(line[1])
                print(f'El precio de un cajón de {fruta} es:, {precio}')
                return precio
        except IndexError:
            print(f'{fruta} no figura en el listado de precios')
    f.close()


buscar_precio('Frambuesa')

#D:\Desktop\Programacion 1\ejercicios_python\Data/precios.csv#