#Raggruppamento dei valori per data
d1 = dati.groupby('Date')[["TotalPositiveCases", "Test"]].mean()

# Normalizzare i dati TotalPositiveCases
min_value = d1["TotalPositiveCases"].min()
max_value = d1["TotalPositiveCases"].max()
d1["TotalPositiveCases_normalized"] = (d1["TotalPositiveCases"] - min_value) / (max_value - min_value)

# Normalizzare i dati Test
min_value = d1["Test"].min()
max_value = d1["Test"].max()
d1["Test_normalized"] = (d1["Test"] - min_value) / (max_value - min_value)

#Creazione grafico
sns.lineplot(data = d1[["TotalPositiveCases_normalized","Test_normalized"]], palette="tab10", linewidth=2.5)
plt.title('Valori normalizzati')
plt.legend(['Casi totali', 'Tamponi'])
plt.show()
