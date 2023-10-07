import numpy as np 
import pandas as pd
import copy
import matplotlib.pyplot as plt

# Creem el data_range dels últims 5 anys (anual).
range_20_last_years = pd.date_range("1/1/2018", periods=5, freq='A')

df = pd.DataFrame(
    index=range_20_last_years, 
    data= {
            "Barcelona":[23,22,24,26,28],
            "Lisboa":[21,23,21,24,25],
            "Rabat":[25,23,25,30,28],
        }
    )
df.index.name="Year"
# display(df)
df.plot(title="Temperatures últims 5 anys",legend=True)

# Per a què es mostri el gràfic amb Python cal guardar-lo en fitxer.
plt.savefig('intro-lineplot1.png')
