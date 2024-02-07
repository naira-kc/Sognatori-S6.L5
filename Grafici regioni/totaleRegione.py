import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

file = "regioniPulite.csv"
df = pd.read_csv(file)

#Raggruppo per regione
dati_raggruppati = df.groupby('RegionName')["NewPositiveCases"].sum().reset_index()

#Importiamoli in un csv per la distribuzione geografica su excel
dati_raggruppati.to_csv("TotaleRegione.csv", index = False)

#Ordiniamoli per valore
dati_raggruppati = dati_raggruppati.sort_values(by="NewPositiveCases", ascending=False)

#Creiamo il grafico
sns.barplot(x="RegionName", y="NewPositiveCases", data=dati_raggruppati, color="#82c89f")
plt.title('Casi positivi registrati')
plt.xlabel('Casi positivi')
plt.ylabel('Totale')
plt.xticks(rotation=45, ha = "right")
plt.show()
