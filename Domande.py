
#1. Scrivi una funzione che restituisca il massimo di tre numeri.

def massimo_tra_tre_numeri(num1, num2, num3):
    return max(num1, num2, num3)

# Esempio di utilizzo della funzione
num1 = 10
num2 = 20
num3 = 15
massimo = massimo_tra_tre_numeri(num1, num2, num3)
print("Il massimo tra", num1, ",", num2, "e", num3, "e:", massimo)

#2. Scrivi una funzione che converta gradi Celsius in Fahrenheit.

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Esempio di utilizzo della funzione
temperatura_celsius = 25
temperatura_fahrenheit = celsius_to_fahrenheit(temperatura_celsius)
print(temperatura_celsius, "gradi Celsius corrispondono a", temperatura_fahrenheit, "gradi Fahrenheit.")

#3. Scrivi un programma che rimuova i duplicati da una lista.

def rimuovi_duplicati(lista):
    lista_senza_duplicati = list(set(lista))
    return lista_senza_duplicati

# Esempio di utilizzo del programma
lista_con_duplicati = [1, 2, 3, 4, 2, 3, 5, 6, 1]
lista_senza_duplicati = rimuovi_duplicati(lista_con_duplicati)
print("Lista originale:", lista_con_duplicati)
print("Lista senza duplicati:", lista_senza_duplicati)

#4. Crea una funzione che verifichi se una parola e un palindromo.
def is_palindromo(parola):

    # Rimuove eventuali spazi e converte la parola in minuscolo
    parola = parola.replace(" ", "").lower()
    # Confronta la parola con la sua inversione
    return parola == parola[::-1]

# Esempi di utilizzo della funzione
parola1 = "radar"
parola2 = "python"

print(parola1, "e un palindromo?", is_palindromo(parola1))
print(parola2, "e un palindromo?", is_palindromo(parola2))

#5. Scrivi una funzione che calcoli il fattoriale di un numero.

def fattoriale(n):
    # Se il numero e 0 o 1, il fattoriale e 1
    if n == 0 or n == 1:
        return 1
    # Altrimenti, calcola il fattoriale utilizzando la ricorsione
    else:
        return n * fattoriale(n - 1)

# Esempio di utilizzo della funzione
numero = 5
print("Il fattoriale di", numero, "e:", fattoriale(numero))

#6. Crea un dizionario da due liste, una che contiene le chiavi e l&#39;altra i valori.

keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]

# Creazione del dizionario utilizzando zip
dictionary = dict(zip(keys, values))

print(dictionary)

#7. Scrivi una funzione che unisca due liste in una lista di tuple.

def merge_lists_into_tuples(list1, list2):
    # Verifica che le liste abbiano la stessa lunghezza
    if len(list1) != len(list2):
        return "Le liste devono avere la stessa lunghezza."
    
    # Unisci le liste in una lista di tuple
    merged_list = [(list1[i], list2[i]) for i in range(len(list1))]
    
    return merged_list

# Esempio di utilizzo della funzione
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
result = merge_lists_into_tuples(list1, list2)
print(result)

#8. Scrivi un programma che ordini una lista di tuple per il secondo elemento.

def sort_list_of_tuples_by_second_element(list_of_tuples):
    # Ordina la lista di tuple in base al secondo elemento di ciascuna tupla
    sorted_list = sorted(list_of_tuples, key=lambda x: x[1])
    return sorted_list

# Esempio di utilizzo della funzione
list_of_tuples = [(3, 'c'), (1, 'a'), (2, 'b')]
sorted_list = sort_list_of_tuples_by_second_element(list_of_tuples)
print(sorted_list)

#9. Utilizza una list comprehension per creare una lista dei quadrati dei primi 10 numeri interi.

quadrati_primi_10 = [x**2 for x in range(1, 11)]

print(quadrati_primi_10)

#10. Utilizza una list comprehension per estrarre numeri pari da una lista data.

numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeri_pari = [x for x in numeri if x % 2 == 0]

print(numeri_pari)

#11. Crea una list comprehension che converta una lista di stringhe in maiuscolo.

lista_stringhe = ['ciao', 'mondo', 'python']
stringhe_maiuscole = [stringa.upper() for stringa in lista_stringhe]

print(stringhe_maiuscole)

#12. Utilizza una list comprehension per creare una lista di tuple (numero, quadrato del numero).

numeri = [1, 2, 3, 4, 5]
lista_tuple = [(x, x**2) for x in numeri]

print(lista_tuple)

#13. Scrivi una list comprehension che filtri le parole di una lista che iniziano con una vocale.

parole = ["apple", "banana", "orange", "kiwi", "grape"]
parole_vocali = [parola for parola in parole if parola[0].lower() in "aeiou"]

print(parole_vocali)

#14. Utilizza una list comprehension per eliminare i valori negativi da una lista.

lista = [10, -5, 20, -8, 15, -3, 0, 25, -12]
lista_positivi = [numero for numero in lista if numero >= 0]

print(lista_positivi)

#15. Crea una lista di tutte le lettere dell alfabeto con una list comprehension.

alfabeto = [chr(lettera) for lettera in range(ord('a'), ord('z') + 1)]

print(alfabeto)

import numpy as np

#16. Crea un array numpy di dimensione 3x3 con valori casuali.

array_casuale = np.random.rand(3, 3)

print(array_casuale)

#17. Scrivi un programma che calcoli la somma di tutti gli elementi in un array numpy.

array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

somma = np.sum(array)

print("La somma di tutti gli elementi dell array e:", somma)

#18. Crea un array numpy e calcolane la media, mediana e varianza.

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

media = np.mean(array)
mediana = np.median(array)
varianza = np.var(array)

print("Media dell array:", media)
print("Mediana dell array:", mediana)
print("Varianza dell array:", varianza)


#19. Scrivi un programma che moltiplichi due matrici numpy.

matrice1 = np.array([[1, 2, 3],
                     [4, 5, 6]])

matrice2 = np.array([[7, 8],
                     [9, 10],
                     [11, 12]])

prodotto = np.dot(matrice1, matrice2)

print("Matrice risultante:")
print(prodotto)

#20. Crea un array numpy e ordinalo in modo ascendente.

array = np.array([3, 1, 2, 5, 4])
array_ordinato = np.sort(array)

print("Array ordinato in modo ascendente:")
print(array_ordinato)

import pandas as pd

#21. Crea un DataFrame pandas da un dizionario.

dati = {
    'Nome': ['Alice', 'Bob', 'Charlie', 'David'],
    'Eta': [25, 30, 35, 40],
    'Citta': ['Roma', 'Milano', 'Napoli', 'Torino']
}

df = pd.DataFrame(dati)

print(df)

#22. Leggi un file CSV in un DataFrame pandas.

#df = pd.read_csv('dataset_climatico.csv')
#print(df)

#23. Seleziona una colonna specifica da un DataFrame.

data = {'A': [1, 2, 3, 4, 5],
        'B': ['a', 'b', 'c', 'd', 'e']}
df = pd.DataFrame(data)

# Seleziona la colonna 'A' utilizzando la notazione a dizionario
colonna_A = df['A']
# Seleziona la colonna 'A' utilizzando la notazione a attributo
colonna_A = df.A


print(colonna_A)

#24. Filtra un DataFrame pandas in base a una condizione.

data = {'A': [1, 2, 3, 4, 5],
        'B': ['a', 'b', 'c', 'd', 'e']}
df = pd.DataFrame(data)
filtro = df.loc[df['A'] > 3]

print(filtro)

#25. Calcola la media dei valori in ogni colonna di un DataFrame.

data = {'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50],
        'C': [100, 200, 300, 400, 500]}
df = pd.DataFrame(data)
media_colonne = df.mean()

print(media_colonne)

import matplotlib.pyplot as plt

#26. Crea un grafico a linee di una serie temporale con Matplotlib.

data = {
    'data_osservazione': ['2022-01-01', '2022-01-02', '2022-01-03'],
    'temperatura_media': [3.34, 34.64, 1.22]
}
df = pd.DataFrame(data)
# Convertiamo la colonna 'data_osservazione' in tipo datetime
df['data_osservazione'] = pd.to_datetime(df['data_osservazione'])

# Crea il grafico a linee
plt.figure(figsize=(10, 6))
plt.plot(df['data_osservazione'], df['temperatura_media'], marker='o', linestyle='-')
plt.title('Grafico a Linee della Temperatura Media')
plt.xlabel('Data')
plt.ylabel('Temperatura Media')
plt.grid(True)
plt.show()

#27. Crea un istogramma di una distribuzione di valori con Matplotlib.

np.random.seed(0)
valori = np.random.randn(1000)

plt.figure(figsize=(8, 6))
plt.hist(valori, bins=30, color='skyblue', edgecolor='black')
plt.title('Istogramma della distribuzione dei valori')
plt.xlabel('Valore')
plt.ylabel('Frequenza')
plt.grid(True)
plt.show()

#28. Crea un grafico a barre per rappresentare i dati di un DataFrame.

data = {
    'Categoria': ['A', 'B', 'C', 'D', 'E'],
    'Valore': [23, 45, 56, 78, 32]
}
df = pd.DataFrame(data)

plt.figure(figsize=(8, 6))
plt.bar(df['Categoria'], df['Valore'], color='skyblue')
plt.title('Grafico a Barre')
plt.xlabel('Categoria')
plt.ylabel('Valore')
plt.grid(axis='y')
plt.show()

#29. Crea un diagramma a dispersione (scatter plot) con due variabili di un DataFrame.

data = {
    'x': [1, 2, 3, 4, 5],
    'y': [2, 3, 5, 7, 11]
}
df = pd.DataFrame(data)

plt.scatter(df['x'], df['y'])
plt.xlabel('Variabile X')
plt.ylabel('Variabile Y')
plt.title('Diagramma a Dispersione')
plt.show()

#30. Crea un box plot per analizzare la distribuzione in un DataFrame.

data = {
    'valori': [10, 20, 25, 30, 35, 40, 45, 50, 55, 60]
}
df = pd.DataFrame(data)
plt.boxplot(df['valori'])

plt.title('Box Plot dei Valori')
plt.show()