import pandas as pd

try:
    # Carica il file Excel
    df_comuni_data = pd.read_excel('Comuni_python.xlsx')
    print("Caricamento del file Excel completato con successo!")
except Exception as e:
    print("Si è verificato un errore durante il caricamento del file Excel:", e)

# Visualizza informazioni sul DataFrame prima della pulizia
print("Informazioni sul DataFrame prima della pulizia:")
print(df_comuni_data.info())

# Visualizza statistiche di base per le colonne numeriche prima della pulizia
print("Statistiche di base per le colonne numeriche prima della pulizia:")
print(df_comuni_data.describe())

# Gestione dei valori mancanti
# Conta i valori mancanti per ogni colonna
valori_mancanti = df_comuni_data.isnull().sum()
print("\nValori mancanti per ogni colonna:")
print(valori_mancanti)

# Gestisci i valori mancanti come preferisci
# Ad esempio, puoi riempire i valori mancanti con un valore predefinito
# df_comuni_data['NomeColonna'] = df_comuni_data['NomeColonna'].fillna(valore_predefinito)

# Dopo aver gestito i valori mancanti, puoi eliminare le righe che contengono ancora valori mancanti
df_comuni_data.dropna(inplace=True)

# Rimuovi la colonna senza nome
if 'Unnamed: 1' in df_comuni_data.columns:
    df_comuni_data.drop(columns=['Unnamed: 1'], inplace=True)

# Controlla se ci sono righe duplicate
righe_duplicate = df_comuni_data[df_comuni_data.duplicated()]
print("\nRighe duplicate:")
print(righe_duplicate)

# Visualizza informazioni sul DataFrame dopo la pulizia
print("\nInformazioni sul DataFrame dopo la pulizia:")
print(df_comuni_data.info())

# Visualizza statistiche di base per le colonne numeriche dopo la pulizia
print("\nStatistiche di base per le colonne numeriche dopo la pulizia:")
print(df_comuni_data.describe())
