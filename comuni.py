import pandas as pd

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

import humanize

# Esegui il metodo describe() sul DataFrame
statistiche_base = df_comuni.describe()

# Estrai i valori di interesse
count = statistiche_base.loc['count', 'Popolazione2011']
mean = statistiche_base.loc['mean', 'Popolazione2011']
std = statistiche_base.loc['std', 'Popolazione2011']
min_value = statistiche_base.loc['min', 'Popolazione2011']
quartile_25 = statistiche_base.loc['25%', 'Popolazione2011']
quartile_50 = statistiche_base.loc['50%', 'Popolazione2011']
quartile_75 = statistiche_base.loc['75%', 'Popolazione2011']
max_value = statistiche_base.loc['max', 'Popolazione2011']

# Formattazione dei dati utilizzando la libreria humanize
formatted_count = humanize.intword(count)
formatted_mean = humanize.intcomma(round(mean, 2))
formatted_std = humanize.intcomma(round(std, 2))
formatted_min_value = humanize.intword(min_value)
formatted_quartile_25 = humanize.intword(quartile_25)
formatted_quartile_50 = humanize.intword(quartile_50)
formatted_quartile_75 = humanize.intword(quartile_75)
formatted_max_value = humanize.intword(max_value)

# Stampare i dati formattati
print("Statistiche di base per le colonne numeriche dopo la pulizia:")
print(f"Count: {formatted_count}")
print(f"Mean: {formatted_mean}")
print(f"Std: {formatted_std}")
print(f"Min: {formatted_min_value}")
print(f"25th Percentile: {formatted_quartile_25}")
print(f"50th Percentile: {formatted_quartile_50}")
print(f"75th Percentile: {formatted_quartile_75}")
print(f"Max: {formatted_max_value}")

import matplotlib.pyplot as plt

# Raggruppo i dati per regione e calcolo la popolazione totale di ciascuna regione
popolazione_per_regione = df_comuni.groupby('Regione')['Popolazione2011'].sum()

# Normalizzo la popolazione per regione
popolazione_normalizzata = popolazione_per_regione / popolazione_per_regione.sum()

# Creo l'istogramma
plt.figure(figsize=(10, 6))
popolazione_normalizzata.plot(kind='bar', color='skyblue')
plt.title('Popolazione per Regione (Normalizzata)')
plt.xlabel('Regione')
plt.ylabel('Popolazione Normalizzata')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
