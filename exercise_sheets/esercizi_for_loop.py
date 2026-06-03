# -*- coding: utf-8 -*-
"""
Raccolta di 20 Esercizi sul ciclo 'for' in Python - Versione senza soluzioni e con Test Case
Ordinati per complessità crescente.

Istruzioni:
Ogni esercizio contiene una breve descrizione dell'obiettivo, le variabili di input 
e un commento con il 'Test Case' che mostra l'output esatto che il tuo codice dovrà stampare.
Scrivi il tuo codice direttamente sotto il commento '# SCRIVI QUI IL TUO CODICE'.
"""

print("==============================================================================")
print("INIZIO ESERCIZI SUL CICLO FOR")
print("==============================================================================")

# ==============================================================================
# PARTE 1: ITERAZIONE SU LISTE E STRINGHE
# ==============================================================================

# ------------------------------------------------------------------------------
# Esercizio 1: Stampare ogni elemento di una lista.
# Obiettivo: Stampare a schermo ciascun elemento presente nella lista 'lista_frutti',
# visualizzandone uno per riga.
#
# TEST CASE ATTESO:
# mela
# banana
# arancia
# ------------------------------------------------------------------------------
print("\n--- Esercizio 1 ---")
lista_frutti = ['mela', 'banana', 'arancia']

# SCRIVI QUI IL TUO CODICE



# ------------------------------------------------------------------------------
# Esercizio 2: Contare le vocali in una stringa.
# Obiettivo: Calcolare il numero totale di vocali (a, e, i, o, u) presenti nella
# stringa 'stringa_testo', ignorando la differenza tra maiuscole e minuscole.
# Salva il totale in 'conteggio' e stampalo.
#
# TEST CASE ATTESO:
# Numero di vocali: 4
# ------------------------------------------------------------------------------
print("\n--- Esercizio 2 ---")
stringa_testo = "Python Programming"
conteggio = 0
vocali = "aeiouAEIOU"

# SCRIVI QUI IL TUO CODICE



# ------------------------------------------------------------------------------
# Esercizio 3: Trasformazione di una lista.
# Obiettivo: Popolare la lista vuota 'risultati' inserendo tutti i valori contenuti
# in 'numeri', ma raddoppiati. Al termine, stampa la lista 'risultati'.
#
# TEST CASE ATTESO:
# [2, 4, 6, 8]
# ------------------------------------------------------------------------------
print("\n--- Esercizio 3 ---")
numeri = [1, 2, 3, 4]
risultati = []

# SCRIVI QUI IL TUO CODICE



# ------------------------------------------------------------------------------
# Esercizio 4: Trovare la stringa più lunga.
# Obiettivo: Identificare la parola che contiene più caratteri all'interno della
# lista 'parole'. Salva questo elemento in 'parola_piu_lunga' e stampalo.
#
# TEST CASE ATTESO:
# La parola più lunga è: computer
# ------------------------------------------------------------------------------
print("\n--- Esercizio 4 ---")
parole = ["casa", "computer", "python", "it"]
parola_piu_lunga = parole[0]

# SCRIVI QUI IL TUO CODICE



# ==============================================================================
# PARTE 2: GENERAZIONE DI SEQUENZE NUMERICHE
# ==============================================================================

# ------------------------------------------------------------------------------
# Esercizio 5: Stampare numeri pari in un intervallo.
# Obiettivo: Generare e stampare in sequenza tutti i numeri pari compresi
# tra 2 e 20 (inclusi).
#
# TEST CASE ATTESO:
# 2
# 4
# ... (fino a 20)
# ------------------------------------------------------------------------------
print("\n--- Esercizio 5 ---")

# SCRIVI QUI IL TUO CODICE



# ------------------------------------------------------------------------------
# Esercizio 6: Somma cumulativa.
# Obiettivo: Calcolare la somma complessiva di tutti i numeri interi partendo da 1
# fino ad arrivare al numero 'n' compreso. Salva il totale in 'somma_totale' e stampalo.
#
# TEST CASE ATTESO:
# Somma totale da 1 a 5: 15
# ------------------------------------------------------------------------------
print("\n--- Esercizio 6 ---")
n = 5
somma_totale = 0

# SCRIVI QUI IL TUO CODICE



# ------------------------------------------------------------------------------
# Esercizio 7: Tabellina numerica.
# Obiettivo: Generare e mostrare a schermo la tabellina (moltiplicazioni da 1 a 10)
# del valore memorizzato in 'numero_tabellina', rispettando il formato del test case.
#
# TEST CASE ATTESO:
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 10 = 50
# ------------------------------------------------------------------------------
print("\n--- Esercizio 7 ---")
numero_tabellina = 5

# SCRIVI QUI IL TUO CODICE



# ------------------------------------------------------------------------------
# Esercizio 8: Sequenza decrescente.
# Obiettivo: Calcolare il quadrato di ciascun numero intero partendo da 10 fino a 1
# (in ordine decrescente). Inserisci i risultati in 'quadrati' e stampa la lista finale.
#
# TEST CASE ATTESO:
# [100, 81, 64, 49, 36, 25, 16, 9, 4, 1]
# ------------------------------------------------------------------------------
print("\n--- Esercizio 8 ---")
quadrati = []

# SCRIVI QUI IL TUO CODICE



# ==============================================================================
# PARTE 3: ITERAZIONE CON INDICI E POSIZIONI
# ==============================================================================

# ------------------------------------------------------------------------------
# Esercizio 9: Stampare indice e valore.
# Obiettivo: Mostrare a schermo ogni elemento della lista 'citta' affiancato dal suo 
# rispettivo indice di posizione, seguendo esattamente il formato indicato.
#
# TEST CASE ATTESO:
# Indice 0: Roma
# Indice 1: Milano
# Indice 2: Napoli
# ------------------------------------------------------------------------------
print("\n--- Esercizio 9 ---")
citta = ["Roma", "Milano", "Napoli"]

# SCRIVI QUI IL TUO CODICE



# ------------------------------------------------------------------------------
# Esercizio 10: Filtrare elementi in base alla posizione.
# Obiettivo: Esaminare la lista 'nomi' e inserire nella lista 'nomi_filtrati' solo i 
# valori che si trovano in una posizione (indice) DISPARI. Infine, stampa la lista.
#
# TEST CASE ATTESO:
# ['Beppe', 'Daniele']
# ------------------------------------------------------------------------------
print("\n--- Esercizio 10 ---")
nomi = ["Anna", "Beppe", "Carlo", "Daniele", "Elena"]
nomi_filtrati = []

# SCRIVI QUI IL TUO CODICE



# ------------------------------------------------------------------------------
# Esercizio 11: Interruzione alla prima occorrenza negativa.
# Obiettivo: Trovare la posizione del primo numero minore di zero all'interno di 
# 'valori'. Salva questo indice in 'indice_negativo' e blocca subito l'esecuzione.
# Infine, stampa il risultato.
#
# TEST CASE ATTESO:
# Il primo numero negativo si trova all'indice: 2
# ------------------------------------------------------------------------------
print("\n--- Esercizio 11 ---")
valori = [4, 7, -2, 9, -5]
indice_negativo = -1

# SCRIVI QUI IL TUO CODICE



# ==============================================================================
# PARTE 4: ITERAZIONE SU PIÙ SEQUENZE IN PARALLELO
# ==============================================================================

# ------------------------------------------------------------------------------
# Esercizio 12: Associare liste parallele.
# Obiettivo: Combinare in modo corrispondente gli elementi di 'nomi_persone' con quelli 
# di 'eta_persone' per stampare una frase che associ ogni nome alla propria età.
#
# TEST CASE ATTESO:
# Luca ha 25 anni.
# Sara ha 30 anni.
# ------------------------------------------------------------------------------
print("\n--- Esercizio 12 ---")
nomi_persone = ["Luca", "Sara"]
eta_persone = [25, 30]

# SCRIVI QUI IL TUO CODICE



# ------------------------------------------------------------------------------
# Esercizio 13: Prodotto scalare tra vettori.
# Obiettivo: Calcolare il prodotto scalare tra 'vettore_a' e 'vettore_b'. Moltiplica 
# tra loro gli elementi che si trovano nella stessa posizione e accumula la somma in 'prodotto_scalare'.
#
# TEST CASE ATTESO:
# Prodotto scalare: 44
# ------------------------------------------------------------------------------
print("\n--- Esercizio 13 ---")
vettore_a = [1, 3, 5]
vettore_b = [2, 4, 6]
prodotto_scalare = 0

# SCRIVI QUI IL TUO CODICE



# ------------------------------------------------------------------------------
# Esercizio 14: Calcolo spesa complessiva da più liste.
# Obiettivo: Elaborare i dati di tre liste parallele. Per ogni articolo calcola il costo parziale 
# (quantità * prezzo unitario) e stampalo. Accumula tutti i parziali in 'spesa_totale' e mostra il totale finale.
#
# TEST CASE ATTESO:
# Pane: 3.0 €
# Latte: 3.6 €
# Spesa totale generale: 6.6 €
# ------------------------------------------------------------------------------
print("\n--- Esercizio 14 ---")
prodotti = ["Pane", "Latte"]
quantita = [2, 3]
prezzi_unitari = [1.50, 1.20]
spesa_totale = 0.0

# SCRIVI QUI IL TUO CODICE



# ==============================================================================
# PARTE 5: ITERAZIONE SU DIZIONARI
# ==============================================================================

# ------------------------------------------------------------------------------
# Esercizio 15: Visualizzare chiavi e valori.
# Obiettivo: Estrarre e stampare tutte le coppie di dati memorizzate all'interno di 
# 'computer_specs', formattandole come "Chiave: Valore".
#
# TEST CASE ATTESO:
# CPU: Ryzen 5
# RAM: 16GB
# SSD: 512GB
# ------------------------------------------------------------------------------
print("\n--- Esercizio 15 ---")
computer_specs = {"CPU": "Ryzen 5", "RAM": "16GB", "SSD": "512GB"}

# SCRIVI QUI IL TUO CODICE



# ------------------------------------------------------------------------------
# Esercizio 16: Filtrare elementi di un dizionario.
# Obiettivo: Esaminare il dizionario 'registro_voti' e copiare all'interno di 'registro_filtrato' 
# solo le chiavi (studenti) il cui valore (voto) è strettamente maggiore di 'soglia'. Stampa il risultato.
#
# TEST CASE ATTESO:
# {'Alice': 28, 'Luigi': 30}
# ------------------------------------------------------------------------------
print("\n--- Esercizio 16 ---")
registro_voti = {"Mario": 24, "Alice": 28, "Luigi": 30, "Anna": 22}
soglia = 25
registro_filtrato = {}

# SCRIVI QUI IL TUO CODICE



# ------------------------------------------------------------------------------
# Esercizio 17: Inversione di un dizionario.
# Obiettivo: Creare una copia speculare di 'dizionario_originale' all'interno di 
# 'dizionario_invertito', in modo che le vecchie chiavi diventino i nuovi valori e viceversa.
#
# TEST CASE ATTESO:
# {1: 'a', 2: 'b', 3: 'c'}
# ------------------------------------------------------------------------------
print("\n--- Esercizio 17 ---")
dizionario_originale = {"a": 1, "b": 2, "c": 3}
dizionario_invertito = {}

# SCRIVI QUI IL TUO CODICE



# ==============================================================================
# PARTE 6: STRUTTURE MISTE E CASI AVANZATI
# ==============================================================================

# ------------------------------------------------------------------------------
# Esercizio 18: Generare chiavi e stringhe invertite.
# Obiettivo: Popolare il dizionario 'diz_parole_invertite' usando l'indice di posizione della 
# parola in 'lista_parole_mix' come chiave e la parola stessa scritta al contrario come valore.
#
# TEST CASE ATTESO:
# {0: 'ottag', 1: 'enac'}
# ------------------------------------------------------------------------------
print("\n--- Esercizio 18 ---")
lista_parole_mix = ["gatto", "cane"]
diz_parole_invertite = {}

# SCRIVI QUI IL TUO CODICE



# ------------------------------------------------------------------------------
# Esercizio 19: Elenco numerato con accoppiamento.
# Obiettivo: Abbinare sequenzialmente gli elementi di 'studenti_mix' con 'corsi_mix' e stampare 
# l'elenco finale. Ogni riga deve presentare una numerazione progressiva che parte da 1.
#
# TEST CASE ATTESO:
# 1. Marco è iscritto al corso Matematica
# 2. Elena è iscritto al corso Fisica
# ------------------------------------------------------------------------------
print("\n--- Esercizio 19 ---")
studenti_mix = ["Marco", "Elena"]
corsi_mix = ["Matematica", "Fisica"]

# SCRIVI QUI IL TUO CODICE



# ------------------------------------------------------------------------------
# Esercizio 20: Calcolo stipendi con incentivi variabili (Cicli Annidati).
# Obiettivo: Determinare la retribuzione complessiva annua per ciascun dipendente in 'diz_stipendi'. 
# Per ogni lavoratore, calcola la somma dei 12 mesi modificando lo stipendio base mensile con la 
# rispettiva percentuale di bonus indicata in 'bonus_mensili'. Salva il risultato finale in 'stipendi_totali_annui'.
#
# TEST CASE ATTESO:
# {'Alice': 26600.0}
# ------------------------------------------------------------------------------
print("\n--- Esercizio 20 ---")
diz_stipendi = {"Alice": [2000.0] * 12}
bonus_mensili = [0.1] * 11 + [0.2]  # 11 mesi al 10%, l'ultimo mese al 20%
stipendi_totali_annui = {}

# SCRIVI QUI IL TUO CODICE


print("\n==============================================================================")
print("FINE FILE ESERCIZI")
print("==============================================================================")