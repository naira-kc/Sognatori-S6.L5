import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

file = "regioniPulite.csv"
df = pd.read_csv(file)

# L'intervallo di date è riferito agli ultimi due mesi
inizio = "2020-10-01"
fine = "2020-12-06"

# Filtro riferito alle due date
dati_filtrati = df[df['Date'].between(inizio,fine)]

#Raggruppo per regioni in quel primo periodo
dati_raggruppati = dati_filtrati.groupby('RegionName')[['Test','TotalPositiveCases']].sum().reset_index()

#Li ordino
dati_raggruppati = dati_raggruppati.sort_values(by="Test", ascending=False)

sns.barplot(x="RegionName", y="Test", data=dati_raggruppati, color="#82c89f", label="Test Eseguiti")
sns.barplot(x="RegionName", y="TotalPositiveCases", data=dati_raggruppati, color="#ff7f0e", label="Positivi ", alpha = 0.5)
plt.title('Numero di tamponi eseguiti per regione nella seconda fase(set-dec)')
plt.xlabel('Regioni')
plt.ylabel('Total')
plt.xticks(rotation=45, ha="right")
plt.legend()
plt.show()
