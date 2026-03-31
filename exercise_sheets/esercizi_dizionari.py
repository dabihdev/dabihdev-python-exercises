# ==========================================
# ESERCIZI SUI DIZIONARI PYTHON
# ==========================================

# Esercizio 1: Accedi al valore di una chiave specifica
# Obiettivo: Stampa il nome della capitale
capitale = {"Italia": "Roma", "Francia": "Parigi", "Spagna": "Madrid"}

# Esercizio 2: Modifica il valore di una chiave esistente
# Obiettivo: Cambia l'anno dell'auto in 2024
auto = {"marca": "Fiat", "modello": "500", "anno": 2015}

# Esercizio 3: Aggiungi una nuova coppia chiave-valore
# Obiettivo: Aggiungi la chiave "voto" con valore 28
studente = {"nome": "Marco", "corso": "Python"}

# Esercizio 4: Rimuovi una coppia chiave-valore
# SUGGERIMENTO: usa il metodo .pop() o la parola chiave del
# Obiettivo: Rimuovi la chiave "prezzo" dal dizionario
prodotto = {"id": 101, "nome": "Mouse", "prezzo": 25.50}

# Esercizio 5: Accesso sicuro con il metodo .get()
# SUGGERIMENTO: .get() evita errori se la chiave non esiste
# Obiettivo: Cerca la chiave "colore" nel dizionario (che non esiste)
vestito = {"taglia": "L", "materiale": "cotone"}

# Esercizio 6: Ottieni tutte le chiavi del dizionario
# Obiettivo: Trasforma in una lista tutte le chiavi presenti
rubrica = {"Luca": "333...", "Sara": "347...", "Paolo": "320..."}

# Esercizio 7: Verifica se una chiave è presente nel dizionario
# SUGGERIMENTO: usa l'operatore 'in'
# Obiettivo: Controlla se "mele" è presente nel magazzino
magazzino = {"pere": 10, "banane": 5, "arance": 12}

# Esercizio 8: Unisci due dizionari
# SUGGERIMENTO: prova a usare il metodo .update()
# Obiettivo: Aggiungi i dati di 'info_extra' dentro 'utente'
utente = {"username": "coder99"}
info_extra = {"email": "test@esempio.com", "stato": "attivo"}

# Esercizio 9: Accedi a un valore in un dizionario annidato
# Obiettivo: Cambia il colore delle preferenze in "verde"
profilo = {
    "id": 1,
    "preferenze": {
        "colore": "rosso",
        "notifiche": True
    }
}

# Esercizio 10: Svuota completamente il dizionario
# Obiettivo: Rimuovi tutti gli elementi in un colpo solo
sessione = {"token": "abc123xyz", "scadenza": "2024-12-31"}


# ------------------------------------------
# SUGGERIMENTO:
# Per vedere i risultati e verificare le modifiche, usa print().
# ------------------------------------------