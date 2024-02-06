#Raggruppo per regione
dati_raggruppati = dati.groupby('RegionName')["TotalPositiveCases"].sum().reset_index()

# Calcolare il minimo e il massimo dei dati TotalPositiveCases
min_value = dati_raggruppati["TotalPositiveCases"].min()
max_value = dati_raggruppati["TotalPositiveCases"].max()
# Normalizzare i dati TotalPositiveCases
dati_raggruppati["TotalPositiveCases_normalized"] = (dati_raggruppati["TotalPositiveCases"] - min_value) / (max_value - min_value)

#Ordiniamoli per valore
dati_raggruppati = dati_raggruppati.sort_values(by="TotalPositiveCases_normalized", ascending=False)


#Creiamo il grafico
sns.barplot(x="RegionName", y="TotalPositiveCases_normalized", data=dati_raggruppati, color="#82c89f")
plt.title('Casi positivi registrati (Normalizzati)')
plt.xlabel('Casi positivi')
plt.ylabel('Totale')
plt.xticks(rotation=45, ha = "right")
plt.show()
