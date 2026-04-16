# ==============================================================================
# ESEMPIO GUIDA (ESERCIZIO 0)
# Traccia: Scrivi una funzione 'conta_maggiori_di_cinque' che riceve una lista 
# di numeri e restituisce quanti di questi sono maggiori di 5.
# ==============================================================================

def conta_maggiori_di_cinque(lista_numeri):
    contatore = 0  # Inizializzo il contatore
    for numero in lista_numeri:
        if numero > 5:
            contatore += 1  # Incremento se la condizione è vera
    return contatore  # Restituisco il risultato finale

# Esempio di utilizzo:
risultato = conta_maggiori_di_cinque([2, 7, 4, 9, 10])
print(risultato) #-> Stamperà 3


# ==============================================================================
# ESERCIZI DA SVOLGERE (SOLO LISTE)
# ==============================================================================

# Esercizio 1:
# Scrivi una funzione chiamata 'conta_positivi' che riceve una lista di numeri 
# e restituisce quanti numeri sono maggiori di zero.

# Esercizio 2:
# Scrivi una funzione chiamata 'conta_pari' che riceve una lista di numeri 
# e restituisce quanti numeri sono divisibili per 2.

# Esercizio 3:
# Scrivi una funzione chiamata 'conta_maggiori_di_cento' che riceve una lista 
# e restituisce quanti numeri superano il valore 100.

# Esercizio 4:
# Scrivi una funzione chiamata 'conta_zeri' che riceve una lista di numeri 
# e restituisce quante volte compare esattamente il numero 0.

# Esercizio 5:
# Scrivi una funzione chiamata 'conta_multipli_di_cinque' che riceve una lista 
# e restituisce quanti numeri sono divisibili per 5.

# Esercizio 6:
# Scrivi una funzione chiamata 'conta_compresi' che riceve una lista di numeri 
# e restituisce quanti numeri sono compresi tra 10 e 20 (estremi inclusi).

# Esercizio 7:
# Scrivi una funzione chiamata 'conta_dispari' che riceve una lista di numeri 
# e restituisce il numero totale di elementi dispari.

# Esercizio 8:
# Scrivi una funzione chiamata 'conta_minori_di_n' che riceve una lista di numeri 
# e un numero 'n'. Restituisce quanti elementi della lista sono minori di 'n'.

# Esercizio 9:
# Scrivi una funzione chiamata 'conta_uguali' che riceve due liste della stessa 
# lunghezza e restituisce quanti elementi nella stessa posizione sono identici.

# Esercizio 10:
# Scrivi una funzione chiamata 'conta_booleani_true' che riceve una lista di 
# valori booleani (True/False) e restituisce il numero di valori True presenti.