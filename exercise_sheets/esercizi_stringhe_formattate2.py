# ESERCIZI PYTHON: LE F-STRINGS
# Completa gli esercizi scrivendo il codice sotto ogni commento.

# PAGINA DI RIFERIMENTO: https://www.w3schools.com/python/python_string_formatting.asp

# ESERCIZIO 0 (Esempio)
# Obiettivo: Stampare nome e età usando le variabili fornite.
nome = "Marco"
eta = 25
# Soluzione:
print(f"Ciao, mi chiamo {nome} e ho {eta} anni.")

# -----------------------------------------------------------------------------

# ESERCIZIO 1
# Obiettivo: Mostra il nome del prodotto e il suo prezzo.
prodotto = "Smartphone"
prezzo = 499.99
# TODO: Stampa "Il costo del Smartphone è di 499.99 euro."

# ESERCIZIO 2
# Obiettivo: Usa una variabile booleana con un if statement.
is_online = True
utente = "Gianluca"
# TODO: Se is_online è True, stampa "L'utente Gianluca è attualmente connesso". 
# Altrimenti stampa "L'utente Gianluca è offline".

# ESERCIZIO 3
# Obiettivo: Formattazione decimale. 
# Arrotonda il numero pi greco a due cifre decimali all'interno della f-string.
import math
pi = math.pi
# TODO: Stampa "Il valore di PI arrotondato è: 3.14"

# ESERCIZIO 4
# Obiettivo: Operazioni matematiche dirette.
base = 10
altezza = 5
# TODO: Calcola l'area (base * altezza) direttamente dentro la f-string.
# Stampa: "L'area del rettangolo è 50 cm quadrati."

# ESERCIZIO 5
# Obiettivo: Gestione di booleani per lo sconto.
cliente_vip = False
prezzo_pieno = 100
# TODO: Usa un if statement. Se cliente_vip è True, stampa "Prezzo scontato: 80€".
# Altrimenti stampa "Prezzo standard: 100€".

# ESERCIZIO 6
# Obiettivo: Allineamento e padding.
titolo = "MENU"
# TODO: Stampa la parola "MENU" centrata in una riga di 20 caratteri totali, 
# riempiendo gli spazi vuoti con dei trattini (-). Es: "--------MENU--------"

# ESERCIZIO 7
# Obiettivo: Trasformazione testo.
citta = "roma"
regione = "lazio"
# TODO: Stampa le variabili in modo che la prima lettera sia maiuscola.
# Stampa: "Roma si trova nel Lazio." (Suggerimento: usa il metodo .capitalize())

# ESERCIZIO 8
# Obiettivo: Controllo temperatura (booleano).
temperatura = 32
e_caldo = temperatura > 30
# TODO: Usa un if statement su 'e_caldo'. Se True, stampa "Oggi fa molto caldo: 32 gradi".
# Se False, stampa "La temperatura è gradevole: 32 gradi".

# ESERCIZIO 9
# Obiettivo: Formattazione grandi numeri.
abitanti = 59000000
# TODO: Stampa il numero di abitanti usando la virgola o il punto come separatore delle migliaia.
# Esempio: "L'Italia ha 59,000,000 abitanti."

# ESERCIZIO 10
# Obiettivo: Messaggio di benvenuto condizionale complesso.
ore = 19
is_registrato = True
nome_utente = "Alice"
# TODO: Se l'utente è registrato, usa un if statement per decidere se stampare 
# "Buonasera Alice" (se ore >= 18) o "Buongiorno Alice" (se ore < 18).
# Se non è registrato, stampa "Benvenuto, ospite".