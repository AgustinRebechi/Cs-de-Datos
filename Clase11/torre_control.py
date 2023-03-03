class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0



class TorreDeControl:
    '''
    Simulación de Torre de control
    '''
    def __init__(self):
        self.arribos = Cola()
        self.partidas = Cola()
        
    def nuevo_arribo(self, avion):
        '''
        asigna a la cola un avion en espera de aterrizar
        '''
        self.arribos.encolar(avion)
        
    def nueva_partida(self, avion):
        '''
        asigna a la cola un avion en espera de despegue
        '''
        self.partidas.encolar(avion)
    
    def ver_estado(self):
        '''
        Muestra los vuelos vuelos en espera
        '''
        if not self.arribos.esta_vacia():
            print('Vuelos esperando para aterrizar:')
            for arribo in self.arribos.items:
                print(f'|{arribo}|', end=' ')
            print()
        else:
            print('No hay vuelos esperando a despegar!')
        
        if not self.partidas.esta_vacia():
            print('Vuelos esperando para despegar:')
            for partida in self.partidas.items:
                print(f'|{partida}|', end=' ')
            print()
        else:
            print('No hay vuelos esperando a aterrizar!')
        
    
    def asignar_pista(self):
        '''
        asigna una pista con prioridad a vuelos esperando a aterrizar
        '''
        
        if self.arribos.esta_vacia() == False:
            print(f'El vuelo {self.arribos.items[0]} aterrizó con éxito')
            self.arribos.desencolar()
            
        elif self.partidas.esta_vacia() == False:
            print(f'El vuelo {self.partidas.items[0]} despegó con éxito')
            self.partidas.desencolar() 
                
        else:  
            print('No hay vuelos en espera!')
        
        



torre = TorreDeControl()
torre.nuevo_arribo('AR156')
torre.nueva_partida('KLM1267')
torre.nuevo_arribo('AR32')
torre.ver_estado()
        


