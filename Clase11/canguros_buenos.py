# canguros_buenos.py
class Canguro(object):
    def __init__(self, nombre, contenido=[]):
        self.nombre = nombre
        self.contenido_marsupio = contenido.copy() # acá añadí .copy()

    def __str__(self):
        cosas = []
        for i in self.contenido_marsupio:
            if i == str(i):
                cosas.append(i)
            else:
                cosas.append(i.nombre)
                
        return f'{self.nombre} tiene en el marsupio: {cosas}'
    def meter_en_marsupio(self, item):
        self.contenido_marsupio.append(item)


madre = Canguro('Madre')
hijo = Canguro('cangurito')

madre.meter_en_marsupio('choripan')
madre.meter_en_marsupio('messi')
madre.meter_en_marsupio(hijo)

print(madre)

#%%
# canguros_malo.py
"""Este código continene un 
bug importante y dificil de ver
"""

class Canguro:
    """Un Canguro es un marsupial."""
    
    def __init__(self, nombre, contenido=[]):
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.nombre = nombre
        self.contenido_marsupio = contenido

    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)

#%%
madre_canguro = Canguro('Madre')
cangurito = Canguro('gurito')
madre_canguro.meter_en_marsupio('billetera')
madre_canguro.meter_en_marsupio('llaves del auto')
madre_canguro.meter_en_marsupio(cangurito)

print(madre_canguro)

# Al ejecutar este código todo parece funcionar correctamente.
# Para ver el problema, imprimí el contenido de cangurito.

#%%

'''
# Error:
    la funcion meter_en_marsupio() añade items tanto al
    self como al item
    
# Solución
    Lo solucioné haciendo un ".copy()" en el contenido_marsupio
    inicial
'''
