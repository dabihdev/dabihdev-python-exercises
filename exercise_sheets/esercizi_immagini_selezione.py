# -*- coding: utf-8 -*-
"""
==============================================================================
Esercizi Python Semplificati: Selezione e Navigazione nelle Immagini (RGB)
==============================================================================

In questo script lavoreremo sulle immagini intese come matrici di pixel (liste di liste).
Ogni pixel è una tupla di 3 numeri (R, G, B) che rappresenta i colori Rosso, 
Verde e Blu (con valori compresi tra 0 e 255).

Tutti gli esercizi si concentrano sulla SELEZIONE, la LETTURA e la NAVIGAZIONE 
all'interno della matrice, senza effettuare modifiche o sostituzioni.

Struttura degli indici per lo studio:
- immagine[indice_riga] -> Seleziona una riga intera.
- immagine[indice_riga][indice_colonna] -> Seleziona un singolo pixel.
- immagine[indice_riga][indice_colonna][0] -> Seleziona solo il canale Rosso (R) del pixel.

Istruzioni:
Completa il codice richiesto sotto la traccia di ciascun esercizio. Puoi eseguire
questo file direttamente con l'interprete Python sul tuo PC.
"""

# CELLA DI SETUP: Immagine di test (matrice 4x4 pixel)
immagine_test = [
    [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 255)],     # Riga 0: Rosso, Verde, Blu, Bianco
    [(0, 0, 0), (255, 255, 0), (0, 255, 255), (255, 0, 255)],     # Riga 1: Nero, Giallo, Ciano, Magenta
    [(100, 100, 100), (200, 200, 200), (255, 0, 0), (0, 0, 0)],   # Riga 2: Grigio Scuro, Grigio Chiaro, Rosso, Nero
    [(255, 255, 255), (0, 255, 0), (120, 120, 120), (0, 0, 255)]  # Riga 3: Bianco, Verde, Grigio Medio, Blu
]

print("--- Setup Iniziale ---")
print(f"Immagine di test caricata! Dimensioni: {len(immagine_test)}x{len(immagine_test[0])} pixel.\n")


# ------------------------------------------------------------------------------
# Esercizio 1: Il Primo Pixel
# Traccia: Seleziona il pixel posizionato nell'angolo in alto a sinistra 
# (riga 0, colonna 0) di `immagine_test` e stampalo a video.
# ------------------------------------------------------------------------------
print("Esercizio 1:")
# Scrivi qui sotto il tuo codice




print("-" * 40)

# ------------------------------------------------------------------------------
# Esercizio 2: L'Ultimo Pixel
# Traccia: Seleziona il pixel posizionato nell'angolo in basso a destra 
# (riga 3, colonna 3) di `immagine_test` e stampalo a video.
# ------------------------------------------------------------------------------
print("Esercizio 2:")
# Scrivi qui sotto il tuo codice




print("-" * 40)

# ------------------------------------------------------------------------------
# Esercizio 3: Estrazione Canale Singolo
# Traccia: Prendi il pixel situato a riga 0, colonna 1 (il pixel Verde). 
# Estrai da questo pixel SOLO il valore del canale Verde (G) 
# (il secondo elemento della tupla) e stampalo.
# ------------------------------------------------------------------------------
print("Esercizio 3:")
# Scrivi qui sotto il tuo codice




print("-" * 40)

# ------------------------------------------------------------------------------
# Esercizio 4: Selezione di una Riga Intera
# Traccia: Seleziona l'intera terza riga (indice 2) di `immagine_test`. 
# Salvala in una variabile chiamata `riga_selezionata` e stampala.
# ------------------------------------------------------------------------------
print("Esercizio 4:")
# Scrivi qui sotto il tuo codice




print("-" * 40)

# ------------------------------------------------------------------------------
# Esercizio 5: Navigazione mista
# Traccia: Prendi l'ultimo pixel della seconda riga (indice riga 1, indice colonna 3) 
# ed estrai il valore del suo canale Blu (B) (il terzo elemento della tupla). 
# Stampa il valore ottenuto.
# ------------------------------------------------------------------------------
print("Esercizio 5:")
# Scrivi qui sotto il tuo codice




print("-" * 40)

# ------------------------------------------------------------------------------
# Esercizio 6: Scorrere una Riga
# Traccia: Scrivi un ciclo `for` semplice per scorrere ed esaminare uno alla volta 
# i pixel presenti nella prima riga (indice 0) di `immagine_test`. 
# Stampa ogni pixel su una riga separata.
# ------------------------------------------------------------------------------
print("Esercizio 6:")
# Scrivi qui sotto il tuo codice




print("-" * 40)

# ------------------------------------------------------------------------------
# Esercizio 7: Algoritmo Filtro - Contare i Pixel Bianchi
# Traccia: Usa un doppio ciclo `for` annidato per scorrere tutti i pixel della matrice.
# Usa l'istruzione `if` per verificare se il pixel corrente è completamente 
# bianco (255, 255, 255). Conta quanti pixel bianchi ci sono in totale e stampa il risultato.
# ------------------------------------------------------------------------------
print("Esercizio 7:")
# Scrivi qui sotto il tuo codice




print("-" * 40)

# ------------------------------------------------------------------------------
# Esercizio 8: Algoritmo Filtro - Trovare la Posizione dei Pixel Neri
# Traccia: Scorri l'intera matrice `immagine_test` usando un doppio ciclo `for` 
# combinato con `enumerate()` (per tracciare gli indici di riga e colonna).
# Se trovi un pixel completamente nero (0, 0, 0), stampa a video le sue coordinate 
# nel formato: `Riga: X, Colonna: Y`.
# ------------------------------------------------------------------------------
print("Esercizio 8:")
# Scrivi qui sotto il tuo codice




print("-" * 40)

# ------------------------------------------------------------------------------
# Esercizio 9: Algoritmo Filtro - Selezione Mirata su Riga
# Traccia: Scrivi un ciclo `for` per scorrere i pixel della quarta riga (indice 3). 
# Usa un `if` per stampare SOLO i pixel che hanno il canale del Rosso (R) uguale a 0.
# ------------------------------------------------------------------------------
print("Esercizio 9:")
# Scrivi qui sotto il tuo codice




print("-" * 40)

# ------------------------------------------------------------------------------
# Esercizio 10: Algoritmo Filtro - Controllo di Esistenza Rapido
# Traccia: Scorri l'intera matrice per cercare se esiste almeno un pixel di colore 
# Verde (0, 255, 0). Usa un ciclo `for` annidato e un `if`. Non appena l'algoritmo 
# trova il primo pixel verde, deve stampare "Colore Verde individuato!" e 
# fermarsi immediatamente usando l'istruzione `break`.
# ------------------------------------------------------------------------------
print("Esercizio 10:")
# Scrivi qui sotto il tuo codice




print("\n--- Fine dello script ---")
