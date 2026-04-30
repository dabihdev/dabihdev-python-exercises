# =================================================================
# ESERCIZI PYTHON: LISTE, SLICING E CONDIZIONALI
# =================================================================

# -----------------------------------------------------------------
# PARTE 1: INDEXING DELLE LISTE (Esercizi 1-5)
# -----------------------------------------------------------------

# Pagina di riferimento: https://www.w3schools.com/python/python_lists_access.asp

# 1. Estrai il primo elemento della lista 'frutti' e stampalo.
frutti = ["mela", "banana", "ciliegia", "kiwi"]


# 2. Accedi al quarto elemento della lista 'anni' e memorizzalo in una variabile.
anni = [1990, 1995, 2000, 2005, 2010]


# 3. Data la lista 'computer', stampa l'ultimo elemento usando un indice negativo.
computer = ["Asus", "Apple", "Dell", "HP", "Lenovo"]


# 4. Cambia il valore del secondo elemento di 'colori' in "arancione" e stampa la lista.
colori = ["rosso", "verde", "blu"]


# 5. (Liste Annidate) Estrai il valore "Python" dalla lista 'linguaggi'.
# Devi usare due indici: uno per la lista esterna e uno per quella interna.
linguaggi = ["Java", ["C++", "Python", "Ruby"], "JavaScript"]


# -----------------------------------------------------------------
# PARTE 2: SLICING DELLE LISTE (Esercizi 6-10)
# (es: lista[1:3])
# -----------------------------------------------------------------

# 6. Estrai i primi tre elementi della lista 'numeri' e stampali.
numeri = [1, 2, 3, 4, 5, 6, 7]


# 7. Crea una nuova lista chiamata 'centro' che contenga gli elementi dal secondo al quarto (inclusi).
valori = [10, 20, 30, 40, 50, 60]


# 8. Estrai tutti gli elementi della lista 'alfabeto' partendo dal terzo elemento fino alla fine.
alfabeto = ["a", "b", "c", "d", "e", "f"]


# 9. Estrai i primi due elementi di 'citta' usando lo slicing.
citta = ["Roma", "Parigi", "Londra", "Berlino"]


# 10. Data la lista 'temperature', estrai i valori centrali (indice 1 e 2).
temperature = [18.5, 22.0, 25.5, 19.0]


# -----------------------------------------------------------------
# PARTE 3: MIX INDEXING E IF-ELSE (Esercizi 11-20)
# -----------------------------------------------------------------

# 11. Controlla se il primo elemento di 'voti' è maggiore o uguale a 6. 
# Se sì, stampa "Sufficiente", altrimenti "Insufficiente".
voti = [5.5, 7, 8, 4]


# 12. Se il secondo elemento di 'nomi' è "Anna", stampa "Ciao Anna!", 
# altrimenti stampa "Nome non trovato".
nomi = ["Marco", "Anna", "Luca"]


# 13. Controlla se l'ultimo elemento di 'numeri_misti' è pari o dispari (usa l'indice positivo).
numeri_misti = [10, 15, 20, 25, 30]


# 14. Verifica se il primo elemento della lista 'parole' è uguale all'ultimo.
parole = ["casa", "cane", "gatto", "casa"]


# 15. Data la lista 'coordinate', controlla se il valore all'indice 0 è positivo (> 0).
coordinate = [-5, 10, 15]


# 16. Controlla se la lunghezza della lista 'oggetti' è maggiore di 2. 
# Se lo è, stampa il terzo elemento (indice 2).
oggetti = ["penna", "gomma", "quaderno"]


# 17. Se l'elemento all'indice 1 di 'misto' è una stringa, stampa "È una stringa".
# (Suggerimento: usa type(misto[1]) == str)
misto = [100, "Python", True]


# 18. Confronta il primo e il secondo elemento di 'prezzi'. 
# Stampa quale dei due è il maggiore.
prezzi = [12.50, 9.99, 15.00]


# 19. Data la lista 'stati', se il terzo elemento è "Italia", stampa "Benvenuti", 
# altrimenti stampa lo stato trovato a quell'indice.
stati = ["Francia", "Spagna", "Italia", "Germania"]


# 20. (Bonus) Accedi alla sottolista in 'dati' e controlla se il suo primo elemento è 0.
dati = [1, [0, 5], 3]


# =================================================================
# FINE ESERCIZI
# =================================================================