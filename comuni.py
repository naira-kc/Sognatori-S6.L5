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
