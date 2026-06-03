# -*- coding: utf-8 -*-
"""
Esercizi di Base su Pandas
---------------------------
Questo file contiene 10 esercizi pensati per studenti che stanno iniziando a studiare Pandas.
Ogni esercizio è preceduto da una spiegazione semplice che funge da riferimento e da un blocco TODO.

Istruzioni:
1. Leggi la spiegazione.
2. Completa il codice sotto il commento "# TUO CODICE QUI".
3. Esegui il file Python per verificare l'output dei tuoi esercizi.
"""

import pandas as pd
import numpy as np

print("==================================================")
print("             ESERCIZI BASI DI PANDAS              ")
print("==================================================")

# --- DATASET DI PARTENZA ---
# Useremo questo dizionario di dati per la maggior parte degli esercizi.
dati_scuola = {
    'Nome': ['Alessandro', 'Beatrice', 'Claudio', 'Donatella', 'Edoardo', 'Federica'],
    'Età': [20, 21, 19, 22, 20, 21],
    'Voto': [28, 24, 18, 30, 25, 27],
    'Città': ['Roma', 'Milano', 'Roma', 'Napoli', 'Torino', 'Milano'],
    'Frequentante': ['Sì', 'No', 'Sì', 'Sì', 'No', 'Sì']
}


# ==============================================================================
# ESERCIZIO 1: Creazione di un DataFrame
# Spiegazione: Il DataFrame è la struttura dati principale di Pandas, simile a una
# tabella di un database o a un foglio Excel. Per creare un DataFrame a partire
# da un dizionario Python, si utilizza la funzione `pd.DataFrame(dizionario)`.
# ==============================================================================
print("Esercizio 1: Creazione di un DataFrame")
# TODO: Crea un DataFrame chiamato 'df' utilizzando il dizionario 'dati_scuola' definito sopra.

# TUO CODICE QUI
df = None  # Sostituisci None con il tuo codice

print("Risultato Esercizio 1:")
print(df)
print("-" * 50 + "")


# ==============================================================================
# ESERCIZIO 2: Visualizzare le prime righe (Head)
# Spiegazione: Quando si lavora con tabelle molto grandi, non è pratico stamparle interamente.
# Il metodo `df.head(n)` permette di visualizzare solo le prime 'n' righe del DataFrame.
# Se non si specifica 'n', mostrerà automaticamente le prime 5 righe.
# ==============================================================================
print("Esercizio 2: Visualizzare le prime righe")
# TODO: Mostra solo le prime 3 righe del DataFrame 'df' creato nell'esercizio precedente.
# Nota: Assicurati che l'esercizio 1 sia completato correttamente prima.

if df is not None:
    # TUO CODICE QUI
    pass
else:
    print("[Esercizio 1 non completato]")
print("-" * 50 + "")


# ==============================================================================
# ESERCIZIO 3: Selezionare una singola colonna
# Spiegazione: Per estrarre una colonna specifica da un DataFrame, puoi usare la
# sintassi con le parentesi quadre inserendo il nome della colonna come stringa:
# `df['NomeColonna']`. Il risultato sarà un oggetto chiamato Pandas Series.
# ==============================================================================
print("Esercizio 3: Selezionare una colonna")
# TODO: Seleziona la colonna 'Voto' dal DataFrame 'df' e stampala.

if df is not None:
    # TUO CODICE QUI
    colonna_voto = None  # Sostituisci None
    print("Risultato Esercizio 3:")
    print(colonna_voto)
else:
    print("[Esercizio 1 non completato]")
print("-" * 50 + "")


# ==============================================================================
# ESERCIZIO 4: Filtrare i dati con una condizione
# Spiegazione: Puoi filtrare le righe di un DataFrame applicando una condizione.
# La sintassi è `df[df['NomeColonna'] > valore]`. Questo comando manterrà solo
# le righe in cui la condizione tra parentesi quadre è Vera (True).
# ==============================================================================
print("Esercizio 4: Filtrare i dati")
# TODO: Filtra il DataFrame 'df' per mostrare solo gli studenti che hanno un 'Voto' superiore o uguale a 26.

if df is not None:
    # TUO CODICE QUI
    df_filtrato = None  # Sostituisci None
    print("Risultato Esercizio 4 (Voti >= 26):")
    print(df_filtrato)
else:
    print("[Esercizio 1 non completato]")
print("-" * 50 + "")


# ==============================================================================
# ESERCIZIO 5: Aggiungere una nuova colonna calcolata
# Spiegazione: È possibile creare una nuova colonna assegnandole direttamente dei valori.
# Ad esempio, si possono fare operazioni matematiche sulle colonne esistenti:
# `df['NuovaColonna'] = df['ColonnaEsistente'] * 2`.
# ==============================================================================
print("Esercizio 5: Aggiungere una nuova colonna")
# TODO: Aggiungi una nuova colonna al DataFrame 'df' chiamata 'Voto_In_Trentesimi'.
# Questa colonna deve contenere lo stesso valore della colonna 'Voto' (in questo caso sono già in trentesimi,
# ma facciamo finta di voler aggiungere un punto bonus di partenza a tutti: aumenta ogni voto di 1 punto).

if df is not None:
    # TUO CODICE QUI
    
    print("Risultato Esercizio 5 (con nuova colonna):")
    print(df)
else:
    print("[Esercizio 1 non completato]")
print("-" * 50 + "")


# ==============================================================================
# ESERCIZIO 6: Ordinare il DataFrame
# Spiegazione: Per ordinare le righe di un DataFrame in base ai valori di una colonna,
# si usa il metodo `df.sort_values(by='NomeColonna')`. Di default l'ordine è crescente.
# Se vuoi l'ordine decrescente, devi aggiungere l'argomento `ascending=False`.
# ==============================================================================
print("Esercizio 6: Ordinare i dati")
# TODO: Ordina il DataFrame 'df' in base alla colonna 'Età' in modo DECRESCENTE (dal più grande al più giovane).

if df is not None:
    # TUO CODICE QUI
    df_ordinato = None  # Sostituisci None
    print("Risultato Esercizio 6 (Ordinato per Età decrescente):")
    print(df_ordinato)
else:
    print("[Esercizio 1 non completato]")
print("-" * 50 + "")


# ==============================================================================
# ESERCIZIO 7: Raggruppare i dati e calcolare metriche (Groupby)
# Spiegazione: Il metodo `df.groupby('ColonnaA')['ColonnaB'].mean()` permette di
# raggruppare i dati in base ai valori unici di 'ColonnaA' e calcolare la media 
# della 'ColonnaB' per ogni gruppo. Al posto di `.mean()` si possono usare `.sum()`, `.count()`, ecc.
# ==============================================================================
print("Esercizio 7: Raggruppamento dati (Groupby)")
# TODO: Calcola il 'Voto' medio degli studenti raggruppati per la loro 'Città'.

if df is not None:
    # TUO CODICE QUI
    voto_medio_per_citta = None  # Sostituisci None
    print("Risultato Esercizio 7 (Media voti per città):")
    print(voto_medio_per_citta)
else:
    print("[Esercizio 1 non completato]")
print("-" * 50 + "")


# ==============================================================================
# ESERCIZIO 8: Gestione dei valori mancanti (NaN)
# Spiegazione: Nei dataset reali capita spesso di avere dati mancanti (indicati come NaN).
# Il metodo `df.fillna(valore)` permette di sostituire tutti i valori mancanti 
# con un valore predefinito (es. 0 o una stringa), evitando errori nelle analisi.
# Per questo esercizio useremo un mini DataFrame separato chiamato 'df_incompleto'.
# ==============================================================================
print("Esercizio 8: Gestione dati mancanti")

dati_incompleti = {
    'Prodotto': ['Computer', 'Mouse', 'Tastiera'],
    'Prezzo': [1200, None, 45]  # Il mouse non ha un prezzo specificato
}
df_incompleto = pd.DataFrame(dati_incompleti)
print("DataFrame Originale Incompleto:")
print(df_incompleto)

# TODO: Sostituisci il valore mancante (None/NaN) nella colonna 'Prezzo' con il numero 0.
# Assegna il risultato a una variabile chiamata 'df_pulito'.

# TUO CODICE QUI
df_pulito = None  # Sostituisci None

print("Risultato Esercizio 8 (Senza valori mancanti):")
print(df_pulito)
print("-" * 50 + "")


# ==============================================================================
# ESERCIZIO 9: Rinominare le colonne
# Spiegazione: Per cambiare il nome di una o più colonne, si usa il metodo
# `df.rename(columns={'VecchioNome': 'NuovoNome'})`. 
# Nota: Per rendere la modifica permanente sul DataFrame originale, ricordati di
# riassegnare il dataframe (`df = df.rename(...)`) oppure usa l'argomento `inplace=True`.
# ==============================================================================
print("Esercizio 9: Rinominare le colonne")
# TODO: Rinomina la colonna 'Frequentante' in 'Frequentante_Corso' all'interno del DataFrame 'df'.

if df is not None:
    # TUO CODICE QUI
    df = None  # Sostituisci None con il comando di rinomina
    print("Risultato Esercizio 9 (Colonne rinominate):")
    print(df.columns if df is not None else "df è None")
else:
    print("[Esercizio 1 non completato]")
print("-" * 50 + "")


# ==============================================================================
# ESERCIZIO 10: Esportare i dati in un file CSV
# Spiegazione: Una volta completata l'analisi o la pulizia dei dati, puoi salvare
# il DataFrame in un file esterno condivisibile (es. apribile in Excel).
# Il metodo utilizzato è `df.to_csv('nome_file.csv', index=False)`.
# L'argomento `index=False` serve a non salvare la colonna degli indici numerici (0, 1, 2...).
# ==============================================================================
print("Esercizio 10: Esportazione in CSV")
# TODO: Esporta il DataFrame 'df' finale in un file chiamato 'risultati_studenti.csv'.

if df is not None:
    # TUO CODICE QUI
    
    print("Risultato Esercizio 10:")
    print("File 'risultati_studenti.csv' generato con successo!")
else:
    print("[Esercizio 10 non eseguito perché df è None]")
print("==================================================")
