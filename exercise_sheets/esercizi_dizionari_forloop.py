# ==========================================
# ESERCIZI DIZIONARI + CICLO FOR
# ==========================================

# Pagina web di riferimento: https://www.w3schools.com/python/python_dictionaries_loop.asp


# Esercizio 1: Iterazione semplice (Chiavi e Valori)
# Obiettivo: Usa un ciclo for e il metodo .items() per stampare ogni frutto e la sua quantità
# Formato richiesto: "Frutto: [nome], Quantità: [numero]"
frigo = {"mele": 5, "banane": 2, "arance": 8}

# Esercizio 2: Calcolare una somma totale
# Obiettivo: Calcola il prezzo totale del carrello sommando i valori nel dizionario
carrello = {"pane": 1.50, "latte": 1.20, "pasta": 0.90, "vino": 5.00}

# Esercizio 3: Filtrare i dati
# Obiettivo: Stampa solo i nomi degli studenti che hanno preso un voto superiore o uguale a 18
esame = {"Alice": 25, "Bob": 16, "Carlo": 19, "Diana": 30}

# Esercizio 4: Modifica massiva (Sconto)
# Obiettivo: Applica uno sconto del 10% a tutti i prodotti nel dizionario usando un ciclo for
# Suggerimento: nuovo_prezzo = vecchio_prezzo * 0.9
prezzi = {"Zaino": 50, "Astuccio": 15, "Quaderno": 5}

# Esercizio 5: Contare le occorrenze
# Obiettivo: Data la lista 'parole', usa un for per riempire il dizionario 'frequenza' 
# contando quante volte appare ogni parola.
parole = ["python", "java", "python", "c++", "python", "java"]
frequenza = {}

# Esercizio 6: Trovare il valore massimo
# Obiettivo: Trova e stampa la città con la temperatura più alta
temperature = {"Milano": 18, "Roma": 22, "Napoli": 25, "Torino": 15}

# Esercizio 7: Creare un nuovo dizionario filtrato
# Obiettivo: Crea un nuovo dizionario 'disponibili' che contenga solo i prodotti con quantità > 0
magazzino = {"monitor": 10, "tastiera": 0, "mouse": 5, "cavi": 0}

# Esercizio 8: Iterare sulle sole chiavi
# Obiettivo: Stampa una lista di invitati formattata come: "Invitato: [nome]"
# Suggerimento: puoi iterare direttamente sul dizionario o usare .keys()
invitati = {"Luca": "Confermato", "Sara": "In attesa", "Paolo": "Confermato"}

# Esercizio 9: Dizionari annidati e medie
# Obiettivo: Per ogni studente, calcola la media dei voti e stampala
# Struttura: "Studente: [nome], Media: [voto]"
classe = {
    "Marco": [24, 28, 22],
    "Anna": [30, 30, 28],
    "Luigi": [18, 20, 22]
}

# Esercizio 10: Invertire un dizionario
# Obiettivo: Crea un nuovo dizionario dove le chiavi diventano i valori e viceversa
# Esempio: {1: "A"} -> {"A": 1}
# Nota: Assumi che i valori siano univoci
codici = {101: "Admin", 102: "Editor", 103: "Guest"}


# ------------------------------------------
# SUGGERIMENTO:
# Per questi esercizi, il print() all'interno o dopo il ciclo for 
# è fondamentale per capire se la logica sta funzionando!
# ------------------------------------------