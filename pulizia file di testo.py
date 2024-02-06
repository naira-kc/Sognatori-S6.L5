# Leggo il file di testo
with open('ripartizione-geografica_python.txt', 'r') as file:
    lines = file.readlines()
column_names = lines[0].strip().split('\t')
data = []
for line in lines[1:]:
    values = line.strip().split('\t')
    row_data = dict(zip(column_names, values))
    data.append(row_data)
df = pd.DataFrame(data)
df.to_csv('ripartizione-geografica_python.csv', index=False)
Ripartizione_geografica = pd.read_csv('ripartizione-geografica_python.csv')
Ripartizione_geografica.set_index('Codice Regione', inplace=True)
print(Ripartizione_geografica)
