import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

file_name = "insurance.csv"

try:
	insurance = pd.read_csv(file_name)
except:
	print("Errore caricamento")
	
dati = pd.DataFrame(insurance)
print(dati)

#Set dei valori di riferimento per il BMI
normal_bmi = 28


dati['Risk_bmi'] = np.where(dati['bmi'] >= 28, 0.05*dati['charges'], 0)
dati['Risk_smoker'] = np.where(dati['smoker'] == 'yes', 0.05*dati['charges'], 0)
dati['Total_risk'] = (dati['Risk_bmi']+ dati['Risk_smoker'])*dati['children']
dati['New_total'] = (dati['charges']+dati['Total_risk'])

print(dati)

tab = dati.groupby('age')[['New_total','charges']].sum()

tab.plot(kind = "bar")

plt.xlabel("Età", color = "b")
plt.ylabel("Valore", color = "b")
plt.title("Charge assicurativa prima e dopo l'aumento'", color = "b")
plt.legend(["Nuova rata", "Vecchia rata"])

plt.show()



tab2 = dati[dati['smoker']== 'yes']
tab21 = tab2.groupby('sex')[['smoker']].count()

tab21.plot(kind = "bar")
plt.xlabel("Età", color = "b")
plt.ylabel("Valore", color = "b")
plt.title("Charge assicurativa prima e dopo l'aumento'", color = "b")
print(tab21)

plt.show()


tab31 = tab2.groupby('sex')[['charges']].mean()

tab31.plot(kind = "bar")
plt.xlabel("Età", color = "b")
plt.ylabel("Valore", color = "b")
plt.title("Charge assicurativa prima e dopo l'aumento'", color = "b")
print(tab31)

plt.show()
