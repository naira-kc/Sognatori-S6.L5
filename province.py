import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
import scrapy as sc

province = pd.read_csv("./covid19_province.csv")
df = pd.DataFrame(province)

# tolgo i Nan dal DataFrame
df_pulito = df.dropna()

# ordino il DataFrame in ordine alfabetico in base alle regioni
df_ordinato = df_pulito.sort_values(by="RegionName")

df_senza = df_ordinato.dropna()

# calcolo tutte le informazioni generali che possono essere utili
df_senza.describe()

# scopro qual è la provincia con più casi
max_casi = df_senza["TotalPositiveCases"].idxmax()
massimo_casi = df_senza.loc[max_casi]

# scopro quante sono le province con 0 casi
province_zero_casi = df_senza[df_senza['TotalPositiveCases'] == 0]
senza_nan_1 = province_zero_casi.dropna()

# scopro quante province hanno più di 20000 casi
piu_20000 = df_senza[df_senza["TotalPositiveCases"] > 20000]

df_messo_bene = df_senza.drop("Country", axis=1)



