# ==============================================================================
# GUIDA RAPIDA: IL PATTERN DELLA "FINESTRA MOBILE" (SLIDING WINDOW VIA SLICE)
# ==============================================================================
"""
Cosa significa "Slicing Mobile"?
Immagina di avere una stringa o una lista e di volerla esaminare a "blocchi" 
di lunghezza fissa (chiamata 'k'). È come appoggiare una cornice di vetro 
sopra il testo e farla scorrere verso destra di un carattere alla volta.

Esempio visivo con testo = "python" e k = 3:

Passo 1: [p y t] h o n   -> slice: testo[0:3] -> "pyt"
Passo 2:  p [y t h] o n   -> slice: testo[1:4] -> "yth"
Passo 3:  p y [t h o] n   -> slice: testo[2:5] -> "tho"
Passo 4:  p y t [h o n]   -> slice: testo[3:6] -> "hon"

IL TRUCCO DEGLI INDICI (Formula fondamentale):
Se una stringa è lunga 'N' e la finestra è lunga 'k':
1. Lo slice generico sarà sempre: testo[i : i + k]
2. L'indice di partenza 'i' deve fermarsi in tempo, altrimenti la finestra
   diventa più corta di 'k' o va fuori range!
3. Il ciclo for corretto è SEMPRE:
   for i in range(0, N - k + 1):

Applica questa logica nei 10 esercizi qui sotto!
"""

# ==============================================================================
# ESERCIZI PYTHON
# ==============================================================================

# ------------------------------------------------------------------------------
# Esercizio 1: Finestre fisse su stringa
# Richiesta: Data una stringa, restituisci una lista di tutte le sottostringhe
# di lunghezza esatta 'k' che si possono ottenere scorrendo la stringa.
# ------------------------------------------------------------------------------
def finestre_fisse_stringa(testo: str, k: int) -> list:
    """
    Esempio: finestre_fisse_stringa("python", 3) -> ["pyt", "yth", "tho", "hon"]
    """
    # TODO: Implementa la logica qui
    pass


# ------------------------------------------------------------------------------
# Esercizio 2: Conteggio occorrenze esatte
# Richiesta: Conta quante volte una specifica sottostringa 'target' (di lunghezza K)
# appare in una stringa più grande, usando uno slice mobile.
# (Nota: non usare testo.count(), muoviti esplicitamente con gli indici!)
# ------------------------------------------------------------------------------
def conta_sottostringa_mobile(testo: str, target: str) -> int:
    """
    Esempio: conta_sottostringa_mobile("banana", "ana") -> 2 (le finestre si sovrappongono!)
    """
    # TODO: Implementa la logica qui
    pass


# ------------------------------------------------------------------------------
# Esercizio 3: Somma massima di una sottolista
# Richiesta: Data una lista di numeri interi e una lunghezza 'k', trova la
# somma massima possibile tra tutte le sottoliste contigue di lunghezza 'k'.
# ------------------------------------------------------------------------------
def somma_massima_k(numeri: list, k: int) -> int:
    """
    Esempio: somma_massima_k([1, 4, 2, 10, 23, 3, 1, 0, 20], 4) -> 39 (data da [4, 2, 10, 23])
    """
    # TODO: Implementa la logica qui
    pass


# ------------------------------------------------------------------------------
# Esercizio 4: Sottostringhe palindrome mobili
# Richiesta: Estrai tutte le sottostringhe di lunghezza esatta 'k' che sono
# palindrome (ovvero che si leggono uguali da destra e da sinistra).
# ------------------------------------------------------------------------------
def sottostringhe_palindrome(testo: str, k: int) -> list:
    """
    Esempio: sottostringhe_palindrome("abacaba", 3) -> ["aba", "aca", "aba"]
    """
    # TODO: Implementa la logica qui
    pass


# ------------------------------------------------------------------------------
# Esercizio 5: Media mobile di una lista
# Richiesta: Calcola la media mobile di una lista di numeri con una finestra 'k'.
# Restituisci una lista con le medie arrotondate a due cifre decimali.
# ------------------------------------------------------------------------------
def media_mobile(numeri: list, k: int) -> list:
    """
    Esempio: media_mobile([1, 2, 3, 4, 5], 3) -> [2.0, 3.0, 4.0]
    """
    # TODO: Implementa la logica qui
    pass


# ------------------------------------------------------------------------------
# Esercizio 6: Finestra con elementi unici
# Richiesta: Trova l'indice di partenza della PRIMA sotto-lista di lunghezza 'k'
# che contiene solo elementi UNICI (senza duplicati). Se non esiste, restituisci -1.
# ------------------------------------------------------------------------------
def prima_finestra_unica(lista: list, k: int) -> int:
    """
    Esempio: prima_finestra_unica([1, 2, 2, 3, 4, 2], 3) -> 2
    # Spiegazione: la prima finestra senza duplicati è [2, 3, 4], che parte dall'indice 2.
    """
    # TODO: Implementa la logica qui
    pass


# ------------------------------------------------------------------------------
# Esercizio 7: Sottoliste con somma pari
# Richiesta: Restituisci tutte le sottoliste di lunghezza 'k' la cui somma dei
# componenti sia un numero pari.
# ------------------------------------------------------------------------------
def sottoliste_somma_pari(numeri: list, k: int) -> list:
    """
    Esempio: [1, 3, 2, 4], k=2 -> [[1, 3], [2, 4]] perché 1+3=4 (pari) e 2+4=6 (pari).
    """
    # TODO: Implementa la logica qui
    pass


# ------------------------------------------------------------------------------
# Esercizio 8: Caccia all'anagramma (Slice vs Stringa)
# Richiesta: Data una stringa 'testo' e una stringa 'pattern', verifica se esiste
# almeno una sottostringa in 'testo' che sia un anagramma di 'pattern' usando lo slicing.
# Restituisci True o False.
# ------------------------------------------------------------------------------
def contiene_anagramma(testo: str, pattern: str) -> bool:
    """
    Esempio: contiene_anagramma("cbaebabacd", "abc") -> True (la finestra "cba" è un anagramma)
    """
    # TODO: Implementa la logica qui
    pass


# ------------------------------------------------------------------------------
# Esercizio 9: Finestra a vocali alternate
# Richiesta: Trova tutte le sottostringhe di lunghezza 'k' che iniziano E finiscono
# con una vocale (a, e, i, o, u - sia minuscole che maiuscole).
# ------------------------------------------------------------------------------
def finestre_vocali(testo: str, k: int) -> list:
    """
    Esempio: finestre_vocali("elefante", 3) -> ["ele"] ('e' iniziale, 'e' finale)
    """
    # TODO: Implementa la logica qui
    pass


# ------------------------------------------------------------------------------
# Esercizio 10: Sottolista con valore minimo target
# Richiesta: Scorrendo una lista con una finestra di lunghezza 'k', restituisci
# la finestra (sottolista) che contiene il valore Massimo più BASSO possibile.
# In caso di parità, restituisci la prima incontrata.
# ------------------------------------------------------------------------------
def finestra_con_max_minimo(numeri: list, k: int) -> list:
    """
    Esempio: finestra_con_max_minimo([1, 10, 2, 3, 1, 4], 3)
    Finestre di 3:
    [1, 10, 2] -> max è 10
    [10, 2, 3] -> max è 10
    [2, 3, 1]  -> max è 3  <-- Questo è il massimo più basso!
    [3, 1, 4]  -> max è 4
    Ritorna: [2, 3, 1]
    """
    # TODO: Implementa la logica qui
    pass