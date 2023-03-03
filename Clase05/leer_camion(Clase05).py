import csv
f = open('../Data/fecha_camion.csv')
rows = csv.reader(f)
headers = next(rows)

select = ['nombre', 'cajones', 'precio']

row = next(rows)
indices = [headers.index(ncolumna) for ncolumna in select]
record = {ncolumna: row[index] for ncolumna, index in zip(select, indices)}
camion = [{ ncolumna: row[index] for ncolumna, index in zip(select, indices)} for row in rows] 