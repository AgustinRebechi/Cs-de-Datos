import pandas as pd
import os
import seaborn as sns

directorio = '../Data'
archivo = 'arbolado-en-espacios-verdes.csv'
fname = os.path.join(directorio, archivo)
df = pd.read_csv(fname)


df_jacarandas = df[df['nombre_com'] == 'Jacarandá']
cols = ['altura_tot', 'diametro', 'inclinacio']

df_jacarandas = df_jacarandas[cols]
df_jacarandas.tail()

df_jacarandas.describe()


df_jacarandas.plot.scatter(x = 'diametro', y = 'altura_tot')



sns.scatterplot(data = df_jacarandas, x = 'diametro', y = 'altura_tot')