# ==============================================================================
# 20 Esercizi sui Cicli For in Python (range, zip, enumerate)
# Livello: Semplice / Principiante
# ==============================================================================
# Questo file contiene 20 esercizi pensati per fare pratica con i cicli for,
# la funzione range(), la funzione zip() e la funzione enumerate().
# Ogni esercizio è accompagnato da una traccia e dallo spazio per scrivere la soluzione.
# In fondo al file sono presenti le soluzioni commentate per verificare il lavoro.
# ==============================================================================

print("--- Inizio Esercizi sui Cicli For ---\n")

# ------------------------------------------------------------------------------
# SEZIONE 1: Esercizi con range() (Esercizi 1-7)
# ------------------------------------------------------------------------------

# ESERCIZIO 1: Stampa i numeri da 1 a 10 (inclusi) usando range().
print("Esercizio 1:")
# Scrivi il tuo codice qui sotto:


print("-" * 40)

# ESERCIZIO 2: Stampa i numeri pari da 2 a 20 (inclusi) usando il terzo parametro (step) di range().
print("Esercizio 2:")
# Scrivi il tuo codice qui sotto:


print("-" * 40)

# ESERCIZIO 3: Stampa un conto alla rovescia da 10 a 1, seguito dalla parola "Decollo!".
print("Esercizio 3:")
# Scrivi il tuo codice qui sotto:


print("-" * 40)

# ESERCIZIO 4: Calcola la somma di tutti i numeri da 1 a 50 usando un ciclo for e range().
# Stampa il risultato finale.
print("Esercizio 4:")
# Scrivi il tuo codice qui sotto:


print("-" * 40)

# ESERCIZIO 5: Data la stringa "Python", stampa ogni singolo carattere su una nuova riga 
# ciclando sugli indici della stringa usando range() e len().
print("Esercizio 5:")
parola = "Python"
# Scrivi il tuo codice qui sotto:


print("-" * 40)

# ESERCIZIO 6: Stampa i primi 5 multipli di 5 (5, 10, 15, 20, 25) usando range().
print("Esercizio 6:")
# Scrivi il tuo codice qui sotto:


print("-" * 40)

# ESERCIZIO 7: Crea una lista vuota chiamata 'quadrati'. Usando un ciclo for e range(),
# calcola il quadrato dei numeri da 1 a 5 e aggiungili alla lista. Stampa la lista finale.
print("Esercizio 7:")
# Scrivi il tuo codice qui sotto:


print("-" * 40)


# ------------------------------------------------------------------------------
# SEZIONE 2: Esercizi con enumerate() (Esercizi 8-13)
# ------------------------------------------------------------------------------

# ESERCIZIO 8: Data una lista di frutti, stampa ogni frutto insieme al suo indice (es. "Indice 0: mela").
print("Esercizio 8:")
frutti = ["mela", "banana", "arancia", "fragola"]
# Scrivi il tuo codice qui sotto:


print("-" * 40)

# ESERCIZIO 9: Data una lista di città, stampa una classifica numerata che parte da 1 invece che da 0.
# (Suggerimento: usa il parametro 'start' di enumerate).
print("Esercizio 9:")
citta = ["Roma", "Milano", "Napoli", "Firenze"]
# Scrivi il tuo codice qui sotto:


print("-" * 40)

# ESERCIZIO 10: Data una lista di voti scolastici, usa enumerate() per stampare solo i voti 
# che si trovano in una posizione (indice) pari.
print("Esercizio 10:")
voti = [7, 8, 5, 9, 6, 10]
# Scrivi il tuo codice qui sotto:


print("-" * 40)

# ESERCIZIO 11: Data una lista di nomi, usa enumerate() per modificare la lista originale 
# trasformando ogni nome in lettere maiuscole. Stampa la lista alla fine.
print("Esercizio 11:")
nomi = ["anna", "luca", "marco", "sofia"]
# Scrivi il tuo codice qui sotto:


print("-" * 40)

# ESERCIZIO 12: Cerca il numero 42 nella lista seguente usando enumerate(). Quando lo trovi,
# stampa un messaggio indicando l'indice in cui si trova e interrompi il ciclo con 'break'.
print("Esercizio 12:")
numeri_misti = [10, 23, 42, 55, 12, 42, 90]
# Scrivi il tuo codice qui sotto:


print("-" * 40)

# ESERCIZIO 13: Data una stringa, usa enumerate() per stampare solo i caratteri 
# che hanno un indice dispari.
print("Esercizio 13:")
testo = "Informatica"
# Scrivi il tuo codice qui sotto:


print("-" * 40)


# ------------------------------------------------------------------------------
# SEZIONE 3: Esercizi con zip() (Esercizi 14-20)
# ------------------------------------------------------------------------------

# ESERCIZIO 14: Date due liste (una di nomi e una di età), usa zip() per stamparle insieme 
# nel formato: "Luca ha 25 anni".
print("Esercizio 14:")
nomi_ragazzi = ["Luca", "Sara", "Matteo"]
eta_ragazzi = [25, 22, 30]
# Scrivi il tuo codice qui sotto:


print("-" * 40)

# ESERCIZIO 15: Date due liste di numeri della stessa lunghezza, usa zip() per calcolare 
# la somma degli elementi corrispondenti e stampala (es. 1+10=11, 2+20=22...).
print("Esercizio 15:")
lista_a = [1, 2, 3, 4]
lista_b = [10, 20, 30, 40]
# Scrivi il tuo codice qui sotto:


print("-" * 40)

# ESERCIZIO 16: Date due liste, una con dei prodotti e una con i relativi prezzi, 
# crea una "lista di coppie" usando zip() e stampa la lista.
print("Esercizio 16:")
prodotti = ["Pane", "Latte", "Caffè"]
prezzi = [1.50, 1.20, 2.50]
# Scrivi il tuo codice qui sotto:


print("-" * 40)

# ESERCIZIO 17: Date due liste di stringhe (aggettivi e animali), usa zip() per combinare 
# ogni aggettivo con il rispettivo animale e stampa la combinazione (es. "Il leone è feroce").
print("Esercizio 17:")
animali = ["leone", "cane", "gatto"]
aggettivi = ["feroce", "fedele", "pigro"]
# Scrivi il tuo codice qui sotto:


print("-" * 40)

# ESERCIZIO 18: Date tre liste (nomi, cognomi e ruoli lavorativi), usa zip() per combinare 
# i tre elementi e stampare una descrizione completa di ogni persona.
print("Esercizio 18:")
nomi_completi = ["Mario", "Elena"]
cognomi_completi = ["Rossi", "Bianchi"]
ruoli = ["Sviluppatore", "Designer"]
# Scrivi il tuo codice qui sotto:


print("-" * 40)

# ESERCIZIO 19: Usa contemporaneamente enumerate() e zip() per ciclare su due liste 
# (studenti e corsi). Stampa l'indice (partendo da 1), il nome dello studente e il suo corso.
print("Esercizio 19:")
studenti = ["Alice", "Bob", "Charlie"]
corsi = ["Matematica", "Fisica", "Chimica"]
# Scrivi il tuo codice qui sotto:


print("-" * 40)

# ESERCIZIO 20: Date due liste di lunghezze diverse, usa zip() per stamparle insieme. 
# Osserva cosa succede agli elementi in più della lista più lunga (comportamento standard di zip).
print("Esercizio 20:")
colori = ["Rosso", "Verde", "Blu", "Giallo", "Viola"]
oggetti = ["Mela", "Foglia", "Cielo"]
# Scrivi il tuo codice qui sotto:


print("\n--- Fine degli Esercizi ---")
print("==============================================================================")