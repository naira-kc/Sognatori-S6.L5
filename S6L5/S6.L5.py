
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

insurance_data = pd.read_csv ("insurance.csv")
print(insurance_data)

print(insurance_data.describe())

plt.figure(figsize=(12, 6))
plt.subplot(2, 2, 1)
sns.histplot(insurance_data['age'], kde=True, color='skyblue')
plt.title('Distribuzione di eta')

plt.subplot(2, 2, 2)
sns.histplot(insurance_data['bmi'], kde=True, color='salmon')
plt.title('Distribuzione di BMI')

plt.subplot(2, 2, 3)
sns.countplot(x='children', data=insurance_data, palette='pastel')
plt.title('Distribuzione della quantita dei bambini')

plt.subplot(2, 2, 4)
sns.countplot(x='smoker', data=insurance_data, palette='pastel')
plt.title('Distribuzione degli fumatori')

# Visualizziamo la distribuzione della variabile categorica 'sex'
plt.figure(figsize=(8, 6))
sns.countplot(x='sex', data=insurance_data, palette='pastel')
plt.title('Distribuzione per il sesso')

plt.tight_layout()
plt.show()



# Crea un boxplot
plt.figure(figsize=(12, 8))
sns.boxplot(x='sex', y='charges', data=insurance_data, palette='Set2')
plt.title('Boxplot tra Charges e Sesso')
plt.xlabel('Sesso')
plt.ylabel('Costi (Charges)')
plt.show()



plt.figure(figsize=(12, 8))
sns.stripplot(x='children', y='charges', data=insurance_data, palette='Set3')
plt.title('Swarmplot tra il Numero di Figli e i Costi delle Assicurazioni')
plt.xlabel('Numero di Figli')
plt.ylabel('Costi (Charges)')
plt.show()

"""La reggione piu pericolosa da accoro della tariffa"""

# Boxplot dei costi per regione
plt.figure(figsize=(12, 8))
sns.boxplot(data=insurance_data, x='region', y='charges', palette='Set1')
plt.title('Boxplot dei Costi per Regione')
plt.xlabel('Regione')
plt.ylabel('Costi (Charges)')
plt.show()


plt.figure(figsize=(10, 6))
sns.scatterplot(x='bmi', y='charges', data=insurance_data, color='skyblue')
plt.title('Correlazione tra BMI e Charges')
plt.xlabel('BMI')
plt.ylabel('Charges')
plt.show()

# le colonne in liste

age_list = insurance_data['age'].tolist()
sex_list = insurance_data['sex'].tolist()
bmi_list = insurance_data['bmi'].tolist()
children_list = insurance_data['children'].tolist()
smoker_list = insurance_data['smoker'].tolist()
region_list = insurance_data['region'].tolist()
charges_list = insurance_data['charges'].tolist()

def filter_data(age_list, smoker_list, children_list, charges_list, bmi_list, region_list):
    # Creazione di un DataFrame dai dati delle liste
    df = pd.DataFrame({
        'age': age_list,
        'smoker': smoker_list,
        'children': children_list,
        'charges': charges_list,
        'bmi': bmi_list,
        'region': region_list,
         'sex': sex_list
    })

    # Filtraggio del DataFrame secondo i criteri
    filtered_df = df[(df['smoker'] == 'no') & (df['children'] == 0) & (df['age'] < 30) & (df['bmi'] >= 18.5) & (df['bmi'] <= 24.9) & (df['region'] != "southeast") & (df['sex'] != "male")]

    return filtered_df

# Chiamata della funzione con le liste
filtered_df = filter_data(age_list, smoker_list, children_list, charges_list, bmi_list, region_list)

# Stampa del DataFrame risultante
print(filtered_df)


print(filtered_df.describe())













