#Definisco funzione min max
def min_max(data):
    min_value = data.min()
    max_value = data.max()
    return (data - min_value) / (max_value - min_value)
   
#Raggruppamento dei valori per data
d1 = dati.groupby('Date')[["NewPositiveCases", "Test"]].sum()

#Faccio la standardizzazione min max sulle colonne interessate
d1[['NewPositiveCases','Test']] = min_max(d1[['NewPositiveCases','Test']])

#stampo il grafico
print(d1)
sns.lineplot(data = d1[["NewPositiveCases","Test"]], palette="tab10", linewidth=1.5)
plt.title('Valori normalizzati')
plt.legend(labels = ['Positivi','Tamponi'])
plt.show()
