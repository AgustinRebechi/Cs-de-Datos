import csv
f = open('../Data/precios.csv', 'r')
rows = csv.reader(f)
for row in rows: 
    print(row)
