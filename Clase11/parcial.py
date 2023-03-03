class Lote:
    def __init__(self, f, c, p):
        self.nombre = f
        self.cajones = c
        self.precio = p
        
    def __repr__(self):
        return f'Lote({self.nombre}, {self.cajones}, {self.precio})'
    
    def __str__(self):
        return f'Lote: {repr(self.nombre)} / {self.cajones} / ${self.precio}'
    
    def costo(self):
        return self.cajones * self.precio
    
    def vender(self, n):
        self.cajones -= n
        
class Lote_inf(Lote):
    def costo(self):
        return 1.25*self.cajones*self.precio


#milote = Lote('Naranja', 100, 32.2)
milote = Lote_inf('Pera', 100, 10)
