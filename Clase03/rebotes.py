import sys


try:
    altura = int(sys.argv[1])
except IndexError:
    altura = 100
rebotes = 1

while rebotes <= 10:
    altura = altura / 5 * 3
    print('Rebote numero:', rebotes, round(altura,4))
    rebotes = rebotes + 1