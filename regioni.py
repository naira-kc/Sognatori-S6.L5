import pandas as pd

file = "covid19_italy_region_python.csv"
dati = pd.read_csv(file)

#PULIZIA
#Sostiuzione valori NaN con 0 alla colonna test
dati['TestsPerformed'] = dati['TestsPerformed'].fillna(0)

#Data in data
dati['Date'] = pd.to_datetime(dati['Date'])

#Impostazione indice
dati.set_index('SNo', inplace=True)

#Cancello la colonna country, in quanto inutile
dati.drop('Country', axis=1, inplace=True)

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
