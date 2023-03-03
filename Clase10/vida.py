#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 11:41:54 2022

@author: datascience
"""

from datetime import datetime, date, timedelta

def vida_en_segundos(fecha_nac):
    f = fecha_nac.split('/')    
    AAAA = int(f[0])
    mm = int(f[1])
    dd = int(f[2])    
    fecha_actual = datetime.now()
    fecha_eu = datetime(AAAA,dd,mm)
    fecha = fecha_actual - fecha_eu
    fecha = fecha.total_seconds()
    return fecha

fecha = vida_en_segundos('2002/10/03')
print(float(fecha))