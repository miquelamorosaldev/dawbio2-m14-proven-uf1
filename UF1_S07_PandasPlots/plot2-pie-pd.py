import numpy as np 
import pandas as pd
import copy
import matplotlib.pyplot as plt

# Obtingudes de: https://www.naciodigital.cat/municipals2019/municipi/08101/hospitalet-llobregat
csv_file_path: str = "vots-lh-2019.csv"
df_eleccions: pd.DataFrame = pd.read_csv(csv_file_path, sep=";")

print(df_eleccions)

# Afegim una nova columna amb els colors dels partits.
# https://re-thought.com/how-to-add-new-columns-in-a-dataframe-in-pandas/
colorsPartits=["Red","Yellow","Orange","Purple","Blue","Pink"]
df_eleccions.loc[:,'Color'] = colorsPartits

pl_title = "Resultats Eleccions Municipals 2019 en vots, L'Hospitalet de Llobregat"
# Most pandas plots use the label and color arguments (note the lack of “s” on those). 
# To be consistent with matplotlib.pyplot.pie() you must use labels and colors.

# Pintem el diagrama de sectors i el guardem.
df_eleccions.loc[:,'NumVots'].plot.pie(
    title=pl_title, 
    colors=df_eleccions.loc[:,'Color'],
    autopct="%1.1f%%",
    fontsize=12,
    labels=df_eleccions.loc[:,'Partit']
)
plt.savefig('pieplot-pd-2.png')

# Esborrem el contenidor per a fer l'altre gràfic.
plt.clf()

# Pintem el diagrama de barres i el guardem.

# Per defecte a l'eix de les x posa l'index del dataframe. 
# Farem un nou dataframe en el que l'index sigui el nom del partit en comptes 
# d'un número autogenerat així quedarà bé  
df_eleccions2 = copy.deepcopy(df_eleccions)

# inplace=True per a què actualitzi inmediatament.
df_eleccions2.set_index('Partit', inplace=True)
df_eleccions2.loc[:,'Regidors'].plot.bar(
    title=pl_title, 
    y=df_eleccions.loc[:,'Regidors'], 
    color=df_eleccions.loc[:,'Color'],
    x=df_eleccions.loc[:,'NumVots']
)
plt.savefig('barplot-pd-2.png')
