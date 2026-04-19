# =================================================================
# ESERCIZI SULLE F-STRINGS IN PYTHON
# =================================================================
# Ricorda: Una f-string inizia con f" e usa le graffe { } 
# per contenere variabili o codice Python.
# =================================================================

# 0. ESEMPIO GUIDATO: Crea una frase che saluti l'utente.
nome_utente = "Alice"
# Risoluzione:
print(f"Ciao {nome_utente}, benvenuta!")


# 1. Crea una stringa che dica: "Hai 3 messaggi non letti." 
# usando la variabile 'n_messaggi'.
n_messaggi = 3


# 2. Stampa il risultato di una somma direttamente nella f-string:
# "Il totale è: 30" (sommando a + b).
a = 10
b = 20


# 3. Usa il metodo .upper() dentro le graffe per stampare:
# "ATTENZIONE: PERICOLO" usando la variabile 'allerta'.
allerta = "pericolo"


# 4. Formatta il numero decimale 'prezzo' per mostrare solo due cifre
# dopo la virgola: "Il costo è 12.50€". (Suggerimento: {prezzo:.2f})
prezzo = 12.5


# 5. Unisci l'indexing delle liste con le f-strings! 
# Stampa: "Oggi è Lunedì" prendendo l'elemento corretto dalla lista.
giorni = ["Lunedì", "Martedì", "Mercoledì"]


# 6. Calcola la lunghezza della stringa 'password' direttamente nella f-string:
# "La tua password è lunga 8 caratteri."
password = "segreta1"


# 7. Crea una frase che usi tre variabili: 
# "Il modello è iPhone, colore Nero, memoria 128GB."
modello = "iPhone"
colore = "Nero"
giga = 128


# 8. Stampa il valore di una divisione arrotondato all'intero:
# "Ogni persona riceve 3 fette." (usa // per la divisione intera)
fette_totali = 10
persone = 3


# 9. Trasforma in maiuscolo solo l'iniziale del nome dentro la f-string
# usando .capitalize(): "Benvenuto, Matteo".
utente = "matteo"


# 10. (Bonus) Accedi all'elemento della sottolista e stampalo:
# "Il codice segreto è 99".
dati_complessi = ["Admin", [55, 99, 102], "Attivo"]


# =================================================================