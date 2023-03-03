import csv

types = [str, int, float]

f = open ('../Data/camion.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)

r = list(zip(types, row))

converted = list()
for func, val in zip(types, row):
    converted.append(func(val))


# mas resumido

converted = [func(val) for func, val in zip(types, row)]

# diccionarios

dict(zip(headers, converted))

{name: func(val) for name, func, val in zip(headers, types, row)}


