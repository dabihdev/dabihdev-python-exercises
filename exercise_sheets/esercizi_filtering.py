# ==========================================
# ESERCIZI: FILTRARE LE LISTE (FOR + IF)
# ==========================================

# Schema comune:
# 1. Definire una lista di partenza.
# 2. Inizializzare una lista vuota (es. risultato = []).
# 3. Iterare con un ciclo for.
# 4. Usare un if per controllare una condizione.
# 5. Se la condizione è vera, usare .append() per aggiungere l'elemento alla nuova lista.


# Esercizio 1: Numeri Pari
# Obiettivo: Filtra la lista 'numeri' e salva solo i numeri pari nella lista 'pari'
# Suggerimento: un numero è pari se n % 2 == 0
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pari = []

# Esercizio 2: Parole Lunghe
# Obiettivo: Crea una lista 'nomi_lunghi' che contenga solo i nomi con più di 4 lettere
nomi = ["Anna", "Luca", "Giovanni", "Marco", "Tea", "Alessandro"]
nomi_lunghi = []

# Esercizio 3: Prezzi Economici
# Obiettivo: Filtra la lista 'prezzi' e salva in 'economici' solo i prezzi inferiori a 10.0
prezzi = [15.50, 5.00, 9.99, 20.00, 2.50, 12.00]
economici = []

# Esercizio 4: Solo stringhe che iniziano con la 'A'
# Obiettivo: Filtra la lista 'frutti' e salva in 'frutti_a' quelli che iniziano con la lettera "A"
# Suggerimento: usa .startswith("A") o frutto[0] == "A"
frutti = ["Mela", "Arancia", "Albicocca", "Banana", "Ananas", "Pera"]
frutti_a = []

# Esercizio 5: Voti Promossi
# Obiettivo: Data una lista di voti, crea una lista 'promossi' con solo i voti >= 60
punteggi = [45, 70, 58, 90, 62, 30, 85]
promossi = []

# Esercizio 6: Messaggi Non Letti
# Obiettivo: Filtra la lista 'messaggi' per trovare solo quelli che hanno lo stato "non letto"
messaggi = [["Ciao", "letto"], ["Promozione", "non letto"], ["Vieni?", "non letto"]]
da_leggere = []

# Esercizio 7: Numeri Negativi
# Obiettivo: Estrarre tutti i numeri negativi dalla lista 'dati' e metterli in 'negativi'
dati = [10, -5, 3, -1, -8, 20, 0]
negativi = []

# Esercizio 8: Parole che contengono la 'e'
# Obiettivo: Crea una lista 'contiene_e' con le parole che hanno la lettera 'e' all'interno
# Suggerimento: usa l'operatore 'in' (es: if "e" in parola:)
oggetti = ["sedia", "tavolo", "libro", "penna", "computer", "muro"]
contiene_e = []

# Esercizio 9: Utenti Maggiorenni
# Obiettivo: Data una lista di età, crea una lista 'adulti' con chi ha 18 anni o più
eta = [12, 18, 25, 15, 40, 17, 21]
adulti = []

# Esercizio 10: Multipli di 5
# Obiettivo: Filtra la lista e trova solo i numeri divisibili per 5
valori = [10, 22, 35, 40, 51, 60, 73]
multipli_5 = []


# ------------------------------------------
# SUGGERIMENTO FINALE:
# Dopo ogni ciclo, usa print(nome_lista_risultato) per verificare
# di aver filtrato correttamente gli elementi!
# ------------------------------------------