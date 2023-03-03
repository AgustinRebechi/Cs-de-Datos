class Lote:
    '''
    Clase lote, elabora informe de camión
    '''
    def __init__(self, nombre, cajones, precio):
        '''
        Definición de atributos: nombre, cajones y precio
        
        '''
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
        
    def costo(self):
        '''
        Returns
        -------
        costo = cajones * precio 

        '''
        return self.cajones * self.precio
        
    def vender(self, venta):
        '''
        Vendo cajones y resto del total
        
        '''
        self.cajones -= venta
    
    def __repr__(self):
        '''
        Muestra contendio de Lote
        '''
        return f'Lote({self.nombre},{self.cajones},{self.precio})'
 



c = Lote('Peras', 100, 490.1)
columnas = ['nombre', 'cajones']
for colname in columnas:
        print(colname, '=', getattr(c, colname))

   
 
