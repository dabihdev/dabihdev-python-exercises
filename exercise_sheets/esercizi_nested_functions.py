"""
===============================================================================
GUIDA DI SOPRAVVIVENZA: COME FUNZIONA IL "RETURN" NELLE FUNZIONI INNESTATE
===============================================================================

Immagina una funzione come un ROBOT o un ARTIGIANO a cui dai dei materiali.
Quando il robot finisce il suo lavoro, ti CONSEGNA un oggetto fisico nelle mani.

Se scrivi:
    risultato = calcola_prezzo(10)
Il robot 'calcola_prezzo' lavora, e poi SCOMPARE, lasciando al suo posto 
il valore reale (ad esempio, il numero 12).

Cosa succede se chiamiamo una funzione DENTRO un'altra funzione?
Vedi l'esempio sotto:
"""

def sforna_pane(tipo_farina):
    # Questo robot prende la farina e RESTITUISCE un pezzo di pane (stringa)
    return f"un filone di pane di {tipo_farina}"

def prepara_panino(tipo_farina):
    # Per fare un panino, ho BISOGNO del pane.
    # Chiamo il robot 'sforna_pane'. Quando ha finito, la chiamata a funzione
    # VIENE SOSTITUITA dal suo risultato effettivo!
    
    pane_fresco = sforna_pane(tipo_farina) 
    # Ora la variabile pane_fresco contiene DAVVERO la stringa "un filone di pane di..."
    
    stringa_finale = f"Prendo {pane_fresco} e ci aggiungo il salame!"
    return stringa_finale

# Prova a togliere il commento alla riga sotto per vedere cosa succede:
# print(prepara_panino("Integrale"))

"""
REGOLA D'ORO PER GLI ESERCIZI:
Quando vedi una funzione dentro l'altra, chiediti sempre: 
"Cosa mi sta mettendo in mano questa funzione interna?" 
Prendi quel valore e usalo per il passaggio successivo.

Ora tocca a te! Completa le funzioni dove vedi scritto 'pass' o i puntini.
===============================================================================
"""

# -----------------------------------------------------------------------------
# ESERCIZIO 1: Il Convertitore di Valuta
# Obiettivo: Capire come salvare il risultato in una variabile intermedia.
# -----------------------------------------------------------------------------
def converti_in_dollari(euro):
    return euro * 1.10

def crea_ricevuta_usa(euro_spesi):
    # TESSERA MANCANTE: Chiama 'converti_in_dollari' passando 'euro_spesi' 
    # e salva il risultato in una variabile 'dollari'.
    dollari = ... 
    return f"Hai speso {dollari} USD"


# -----------------------------------------------------------------------------
# ESERCIZIO 2: Il Quadrato del Doppio
# Obiettivo: Passare il risultato di una funzione direttamente come argomento.
# -----------------------------------------------------------------------------
def calcola_quadrato(numero):
    return numero * numero

def quadrato_del_doppio(numero):
    # Calcola prima il doppio del numero (numero * 2)
    doppio = numero * 2
    # TESSERA MANCANTE: Usa la funzione 'calcola_quadrato' passando 'doppio' 
    # come argomento e restituisci (return) il risultato.
    pass


# -----------------------------------------------------------------------------
# ESERCIZIO 3: Allarme Temperatura
# Obiettivo: Usare un valore Booleano (True/False) generato da una sotto-funzione.
# -----------------------------------------------------------------------------
def e_pericolosa(temperatura):
    # Restituisce True se la temperatura supera i 100 gradi, altrimenti False
    return temperatura > 100

def controlla_reattore(temperatura_attuale):
    # TESSERA MANCANTE: Chiama 'e_pericolosa' usando la temperatura_attuale.
    # Se il risultato è True, restituisci "EVACUARE", altrimenti "Tutto ok".
    pass


# -----------------------------------------------------------------------------
# ESERCIZIO 4: Pulizia e Conteggio
# Obiettivo: Lavorare con le stringhe e i loro output modificati.
# -----------------------------------------------------------------------------
def pulisci_testo(testo):
    # Rimuove gli spazi bianchi all'inizio/fine e mette tutto in minuscolo
    return testo.strip().lower()

def conta_lettere_a(testo_grezzo):
    # TESSERA MANCANTE: Pulisci il 'testo_grezzo' usando la funzione sopra.
    # Poi conta quante lettere 'a' ci sono nel testo pulito usando .count('a')
    # Infine restituisci il numero ottenuto.
    pass


# -----------------------------------------------------------------------------
# ESERCIZIO 5: Sconto e Tasse (La Catena)
# Obiettivo: Capire che il risultato di una funzione può essere modificato matematicamente.
# -----------------------------------------------------------------------------
def applica_sconto_dieci_per_cento(prezzo_originale):
    return prezzo_originale * 0.90

def calcola_prezzo_finale(prezzo_originale):
    # 1. Ottieni il prezzo scontato chiamando 'applica_sconto_dieci_per_cento'
    # 2. Aggiungi 2 euro di spese di spedizione al prezzo scontato.
    # 3. Restituisci il prezzo finale.
    pass


# -----------------------------------------------------------------------------
# ESERCIZIO 6: Il Massimo Esagerato
# Obiettivo: Estrarre un dato da una lista tramite funzione e fare un controllo.
# -----------------------------------------------------------------------------
def trova_massimo(lista_numeri):
    return max(lista_numeri)

def il_massimo_e_superiore_a_cento(lista_numeri):
    # TESSERA MANCANTE: Usa 'trova_massimo' per ottenere il numero più grande.
    # Restituisce True se quel numero è maggiore di 100, altrimenti False.
    pass


# -----------------------------------------------------------------------------
# ESERCIZIO 7: Chiamata Diretta Senza Variabili (Livello Pro)
# Obiettivo: Capire che si può annidare una funzione dentro l'altra in una riga sola.
# -----------------------------------------------------------------------------
def incrementa_di_uno(n):
    return n + 1

def triplica(n):
    return n * 3

def incrementa_e_poi_triplica(numero):
    # ESERCIZIO: Prova a farlo in una sola riga di codice!
    # Ricorda: La funzione interna viene eseguita per prima e "diventa" un numero.
    # Esempio: return triplica(incrementa_di_uno(...))
    pass


# -----------------------------------------------------------------------------
# ESERCIZIO 8: Il Generatore di Tweet
# Obiettivo: Unire stringhe generate da funzioni diverse.
# -----------------------------------------------------------------------------
def ottieni_hashtag():
    return "#PythonCoding"

def crea_tweet(messaggio):
    # TESSERA MANCANTE: Prendi il messaggio dell'utente, aggiungi uno spazio, 
    # e poi incolla il risultato della funzione 'ottieni_hashtag()'.
    # Restituisci la stringa completa.
    pass


# -----------------------------------------------------------------------------
# ESERCIZIO 9: Il Super-Media Voti
# Obiettivo: Gestione dei tipi di dato complessi (Liste -> Float -> Stringa).
# -----------------------------------------------------------------------------
def calcola_media(lista_voti):
    return sum(lista_voti) / len(lista_voti)

def genera_pagella(lista_voti, nome_studente):
    # 1. Calcola la media usando la funzione 'calcola_media'
    # 2. Arrotonda la media a due cifre decimali usando la funzione nativa round(media, 2)
    # 3. Restituisci una stringa del tipo: "Lo studente [nome] ha la media di [media]"
    pass


# -----------------------------------------------------------------------------
# ESERCIZIO 10: Il Validatore di Password
# Obiettivo: Unire più concetti in un flusso logico.
# -----------------------------------------------------------------------------
def controlla_lunghezza(password):
    # Restituisce True se la lunghezza è di almeno 8 caratteri
    return len(password) >= 8

def controlla_sicurezza_totale(password):
    # 1. Controlla la lunghezza usando la funzione 'controlla_lunghezza'.
    # 2. Se la lunghezza NON è valida (è False), restituisci "Password troppo corta".
    # 3. Se invece è valida, controlla se la password contiene il carattere "!".
    #    Se lo contiene restituisci "Password Sicura", altrimenti "Password Debole".
    pass
