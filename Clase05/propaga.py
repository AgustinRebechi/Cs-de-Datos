l1 = [ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]
l2 = [ 0, 0, 0, 1, 0, 0]


def propagar(l):
    chispa = 0
    propagacion = []
    for i, e in enumerate(l):
        if e == 0:
            if chispa != 1:
                propagacion.append(e)
            else:
                propagacion.append(chispa)            
        elif e == -1:
            propagacion.append(e)            
        else:
            chispa = 1
            propagacion.append(chispa)
    for e in reversed(l):
        if e == 0:
            if chispa != 1:
                propagacion.append(e)
            else:
                propagacion.append(chispa)            
        elif e == -1:
            propagacion.append(e)            
        else:
            chispa = 1
            propagacion.append(chispa)
    return propagacion
            
    
    
    
    

propagacion = propagar(l2)