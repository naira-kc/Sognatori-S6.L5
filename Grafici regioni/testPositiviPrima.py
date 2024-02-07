import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

file = "covid19_italy_region_pulito.csv"
df = pd.read_csv(file)

# L'intervallo di date è riferito ai primi due mesi
inizio = "2020-02-24"
fine = "2020-04-24"

# Filtro riferito alle due date
dati_filtrati = df[df['Date'].between(inizio,fine)]

#Raggruppo per regioni in quel primo periodo
dati_raggruppati = dati_filtrati.groupby('RegionName')[['Test','TotalPositiveCases']].sum().reset_index()

#Li ordino
dati_raggruppati = dati_raggruppati.sort_values(by="Test", ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x="RegionName", y="Test", data=dati_raggruppati, color="#82c89f", label="Test Eseguiti")
sns.barplot(x="RegionName", y="TotalPositiveCases", data=dati_raggruppati, color="#ff7f0e", label="Positivi ", alpha = 0.5)
plt.title('Numero di tamponi eseguiti per regione nella prima fase(feb-apr)')
plt.xlabel('Regioni')
plt.ylabel('Total')
plt.xticks(rotation=45, ha="right")
plt.legend()
plt.show()
