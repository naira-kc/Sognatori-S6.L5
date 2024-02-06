# scarico le librerie
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scrapy as sc
import humanize as hm

# PULIZIA RIPARTIZIONI
with open('ripartizione-geografica_python.txt', 'r') as file:
    lines = file.readlines()
column_names = lines[0].strip().split('\t')
data = []
for line in lines[1:]:
    values = line.strip().split('\t')
    row_data = dict(zip(column_names, values))
    data.append(row_data)
df = pd.DataFrame(data)
df.to_csv('ripartizione-geografica_python.csv', index=False)
Ripartizione_geografica = pd.read_csv('ripartizione-geografica_python.csv')
Ripartizione_geografica.set_index('Codice Regione', inplace=True)
print(Ripartizione_geografica)


#PULIZIA REGIUONI
file = "covid19_italy_region_python.csv"
dati = pd.read_csv(file)

dati['TestsPerformed'] = dati['TestsPerformed'].fillna(0) #Sostiuzione valori NaN con 0 alla colonna test

dati['Date'] = pd.to_datetime(dati['Date']) #Data in data

dati.set_index('SNo', inplace=True) #Impostazione indice

dati.drop('Country', axis=1, inplace=True) #Cancello la colonna country, in quanto inutile

#Per pulizia si rinominano le colonne
nuove_colonne = {
    'HospitalizedPatients': 'In ospedale',
    'CurrentPositiveCases': 'Positivi',
    'IntensiveCarePatients': 'Ter_intensiva',
    'RegionCode': 'Code',
    'HomeConfinement': 'In Casa',
    'TestsPerformed': 'Test'
}

# Rinomina le colonne utilizzando il metodo rename()
dati.rename(columns=nuove_colonne, inplace=True)

df = pd.DataFrame(dati)
print(dati)

#PULIZIA PROVINCE
# Pulizia PROVINCE
province = pd.read_csv("./covid19_italy_province_python.csv")
df_province = pd.DataFrame(province)

# Rimuovi la colonna "Country" direttamente dal DataFrame `province`
df_province.drop("Country", axis=1, inplace=True)

# Rimuovi i NaN dal DataFrame
df_province = df_province.dropna()

# Ordina il DataFrame in ordine alfabetico in base alle regioni
df_province = df_province.sort_values(by="RegionName")

# Calcola tutte le informazioni generali che possono essere utili
print(df_province.describe())



#PULIZIA COMUNI 

try:
    # Carico il file Excel
    df_comuni = pd.read_excel('Comuni_python.xlsx')
    print("Caricamento del file Excel completato con successo!")
except Exception as e:
    print("Si è verificato un errore durante il caricamento del file Excel:", e)

# Visualizzo le  informazioni sul DataFrame prima della pulizia
print("Informazioni sul DataFrame prima della pulizia:")
print(df_comuni.info())

# Seleziono solo le colonne rilevanti per l'analisi
colonne_rilevanti = ['Denominazione', 'Regione', 'Sigla automobilistica', 'Popolazione2011']
df_comuni = df_comuni[colonne_rilevanti]

# Ora faccio la gestione dei valori mancanti
# Conto i valori mancanti per ogni colonna
valori_mancanti = df_comuni.isnull().sum()
print("\nValori mancanti per ogni colonna:")
print(valori_mancanti)

# Elimino solo le righe con valori mancanti nelle colonne rilevanti
df_comuni.dropna(subset=colonne_rilevanti, inplace=True)

# Rimuovo la colonna senza nome, se presente
if 'Unnamed: 1' in df_comuni.columns:
    df_comuni.drop(columns=['Unnamed: 1'], inplace=True)

# Controllo se ci sono righe duplicate
righe_duplicate = df_comuni[df_comuni.duplicated()]
print("\nRighe duplicate:")
print(righe_duplicate)

# Visualizzo informazioni sul DataFrame dopo la pulizia
print("\nInformazioni sul DataFrame dopo la pulizia:")
print(df_comuni.info())

# Visualizzo statistiche di base per le colonne numeriche dopo la pulizia
print("\nStatistiche di base per le colonne numeriche dopo la pulizia:")
print(df_comuni.describe())


'''
prime ansalisi di pitro
# Trova la provincia con il maggior numero di casi
max_casi = df_province["TotalPositiveCases"].idxmax()
massimo_casi = df_province.loc[max_casi]
print("Provincia con più casi:")
print(massimo_casi)

# Trova quante sono le province con 0 casi
province_zero_casi = df_province[df_province['TotalPositiveCases'] == 0]
senza_nan_1 = province_zero_casi.dropna()
print("Province con 0 casi:")
print(senza_nan_1)

# Trova quante province hanno più di 20000 casi
piu_20000 = df_province[df_province["TotalPositiveCases"] > 20000]
print("Province con più di 20000 casi:")
print(piu_20000)
'''
