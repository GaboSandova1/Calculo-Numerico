import pandas as pd
surveys_df = pd.read_csv("  ")
surveys_df.head() # Se formatean los datos para que quepan 
surveys_df.columns() # Visualiza las columnas 
pd.unique(surveys_df['species_id']) # Retorna un array 
surveys_df['weight'].describe() # Regresa los valores de estas estadisticas 
surveys_df['weight'].max() # Regresa el maximo
surveys_df['weight'].min() # Regresa el minimo
surveys_df['weight'].mean() # Regresa la media 
surveys_df['weight'].std() # Desviacion estandar 
surveys_df['weight'].count() # Numero de elemento

# Datos agrupados por sexo 
grouped_data = surveys_df.groupby('sex')

# Estadisticas para todas las columnas 
grouped_data.describe()
grouped_data.mean() # Estadisticas para todas las columnas por sexo


spiecs_counts = surveys_df.groupby('spieces_id')['record_id'].count()


surveys_df['weight']*2
%matplotlib inline
spiecs_counts.plot(kind = 'bar')

d = {'one': pd.Series([1, 2, 3], index = ['a', 'b', 'c']), 'two': pd.Series([1, 2, 3, 4], index = ['a', 'b', 'c', 'd'])}

pd.DataFrame(d)
my_df = pd.DataFrame(d)
my_df.plot(kind='bar', stacked=True, title="    ")

