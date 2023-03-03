# 
import csv
f = open('../Data/dowstocks.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
headers
['name', 'price', 'date', 'time', 'change', 'open', 'high', 'low', 'volume']
row
['AA', '39.48', '6/11/2007', '9:36am', '-0.18', '39.67', '39.69', '39.45', '181800']


# convertido

types = [str, float, str, str, float, float, float, float, int]
converted = [func(val) for func, val in zip(types, row)]
record = dict(zip(headers, converted))


fecha = [s for s in record['date'].split('/')]