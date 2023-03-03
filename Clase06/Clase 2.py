import numpy as np

a = np.arange(1,21,2)
b = np.linspace(1,19, num= 10, dtype=np.int64)


arr = np.array([2,1,5,3,7,4,6,8])
np.array([arr])

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])

z = np.concatenate((x,y))


#ndarray.ndim te dice la cantidad de ejes (o dimensiones) del arreglo.

p = z.reshape(1,6)

