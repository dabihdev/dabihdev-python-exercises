# esercizi_conteggio_dizionari.py

"""
ESERCIZI PYTHON: IL PATTERN DEL CONTEGGIO
Focus: Utilizzo dei dizionari per mappare frequenze ed occorrenze.
"""

# ESERCIZIO 1: Conteggio caratteri base
# Scrivi una funzione che prenda una stringa e restituisca un dizionario 
# con la frequenza di ogni singolo carattere.
# Esempio: "mela" -> {'m': 1, 'e': 1, 'l': 1, 'a': 1}
def conta_caratteri(stringa):
    pass

# ESERCIZIO 2: Conteggio parole in una frase
# Scrivi una funzione che prenda una frase e restituisca la frequenza di ogni parola.
# Usa il metodo .split() per separare le parole.
# Esempio: "il gatto rincorre il topo" -> {'il': 2, 'gatto': 1, 'rincorre': 1, 'topo': 1}
def conta_parole(frase):
    pass

# ESERCIZIO 3: Frequenza di numeri
# Data una lista di numeri interi, crea un dizionario che indichi quante volte appare ogni numero.
# Esempio: [1, 2, 2, 3, 3, 3] -> {1: 1, 2: 2, 3: 3}
def frequenza_numeri(lista_numeri):
    pass

# ESERCIZIO 4: Conteggio condizionale (Solo Vocali)
# Scrivi una funzione che conti solo le vocali presenti in una stringa, ignorando le consonanti.
# Esempio: "programmazione" -> {'o': 2, 'a': 2, 'i': 1, 'e': 1}
def conta_vocali(stringa):
    pass

# ESERCIZIO 5: Case-Insensitivity
# Modifica il conteggio delle parole in modo che non faccia distinzione tra maiuscole e minuscole.
# Esempio: "Mela mela MELA" -> {'mela': 3}
def conta_parole_unificate(frase):
    pass

# ESERCIZIO 6: Lunghezza delle parole
# Data una lista di parole, crea un dizionario dove la chiave è la lunghezza della parola 
# e il valore è quante parole di quella lunghezza sono presenti.
# Esempio: ["casa", "sole", "mela", "e"] -> {4: 3, 1: 1}
def frequenza_lunghezze(lista_parole):
    pass

# ESERCIZIO 7: Iniziali comuni
# Data una lista di nomi, conta quanti nomi iniziano con la stessa lettera.
# Esempio: ["Anna", "Alberto", "Beatrice", "Bruno", "Carlo"] -> {'A': 2, 'B': 2, 'C': 1}
def conta_iniziali(nomi):
    pass

# ESERCIZIO 8: Filtrare i risultati
# Scrivi una funzione che conti le occorrenze degli elementi in una lista, 
# ma restituisca solo quelli che appaiono più di una volta (i duplicati).
# Esempio: [1, 1, 2, 3, 3, 3, 4] -> {1: 2, 3: 3}
def solo_duplicati(lista):
    pass

# ESERCIZIO 9: Conteggio di categorie (Pari e Dispari)
# Data una lista di numeri, crea un dizionario con due chiavi: "pari" e "dispari", 
# contenenti il conteggio totale per categoria.
# Esempio: [1, 2, 3, 4, 5] -> {'dispari': 3, 'pari': 2}
def conta_pari_dispari(numeri):
    pass

# ESERCIZIO 10: Analisi di una lista annidata
# Data una lista che contiene altre liste di stringhe, conta le occorrenze totali di ogni stringa.
# Esempio: [["a", "b"], ["a", "c"], ["b"]] -> {'a': 2, 'b': 2, 'c': 1}
def conta_annidati(lista_di_liste):
    pass