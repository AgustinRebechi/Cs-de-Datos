import random
import numpy as np
import matplotlib.pyplot as plt

def plotear_temperaturas():
    temperaturas = np.load('Data/Temperaturas.npy')
    return temperaturas
    

temperaturas = plotear_temperaturas()


plt.hist(temperaturas, bins=50, density=True)