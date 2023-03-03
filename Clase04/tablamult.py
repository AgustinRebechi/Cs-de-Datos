h = (0,1,2,3,4,5,6,7,8,9)

print(f'{h[0]:7d} {h[1]:3d} {h[2]:3d} {h[3]:3d} {h[4]:3d} {h[5]:3d} {h[6]:3d} {h[7]:3d} {h[8]:3d} {h[9]:3d}')
print(f'---------------------------------------------')

for r in range(10):
    uno = r
    dos = uno + r
    tres = dos + r
    cuatro = tres + r
    cinco = cuatro + r
    seis = cinco + r
    siete = seis + r
    ocho = siete + r
    nueve = ocho + r    
    print(f'{r}: {h[0]:>4d} {uno:>3d} {dos:>3d} {tres:>3d} {cuatro:>3d} {cinco:>3d} {seis:>3d} {siete:>3d} {ocho:>3d} {nueve:>3d}')