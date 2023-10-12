import numpy as np
import pandas as pd
import os.path
from urllib.request import urlretrieve

url: str = "https://marcos-marva.web.uah.es/CursoSanitaria/practicas/datos/osteoporosis.csv"

csv_file:str = "nou_oestoporisi.csv"

if not os.path.isfile(csv_file):
    urlretrieve(url,csv_file)

# Llegim dataframe, separador fitxers \t, acceptem la primera columna com a index.
col_list: list[str] = ['registro','area','grupedad','edad','imc','bua','clasific','edad_men','menop','tipo_men']

df_oestop: pd.DataFrame = pd.read_csv(url, sep = "\t")

df_oestop = df_oestop.loc[:, col_list] 

# df_oestop=pd.DataFrame(df_oestop,columns=col_list)
print(df_oestop.info())
# print(df_oestop.describe())

# Comptem si hi ha valors no nuls.
print(df_oestop.isna().sum())
   
# 5, 6 i 7.
# Mostra les 10 primeres files.
# Obtén la classificació de les pacients que van des del 100 al 199. → loc, iloc
# Obtén la edat i l’imc de les pacients que van des del 50 al 99. → loc, iloc
print(df_oestop.head())
print(df_oestop.loc[100:199,'clasific'])
print(df_oestop.loc[50:99,['edad','imc']])

# Podem fer la mitjana d'edat.
print('Average age = ',df_oestop['edad'].describe().mean())

# Però l'IMC ens l'ha reconegut com a object i l'hem de convertir a float.  
df_oestop['imc'] = df_oestop['imc'].replace(',', '.')

#2 mètodes per convertir d'obj a float
#df_oestop = df_oestop['imc'].astype(float)
df_oestop['imc'] = pd.to_numeric(df_oestop['imc'], errors='coerce')

print('Average imc = ',df_oestop['imc'].describe().mean())

ruta_nou_fitxer: str = "nou_fitxer_oestoporosi.csv"
# Ja podem guardar el nou fitxer si volem, amb ;
df_oestop.to_csv(ruta_nou_fitxer, sep = ";", index=False) 


df_oestop['imc'] = df_oestop['imc'].astype('category')
df_oestop['clasific'] = df_oestop['clasific'].astype('category')
print(df_oestop.dtypes)

print(df_oestop['grupedad'].value_counts(ascending=True))
print(df_oestop['clasific'].value_counts())