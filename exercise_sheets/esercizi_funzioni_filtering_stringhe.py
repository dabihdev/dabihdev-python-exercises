# ESERCIZI PYTHON: FOR LOOP E FILTERING SU STRINGHE
# Istruzioni: Completa le funzioni. Usa i cicli 'for' per scorrere le stringhe 
# e le istruzioni 'if' per filtrare i caratteri.

# --- ESEMPIO DI RISOLUZIONE ---

def conta_lettere_x(testo, lettera):
    """
    Esempio: Conta quante volte una specifica lettera appare nel testo.
    Test Case: "mamma", "m" -> 3
    """
    conteggio = 0
    for carattere in testo:
        if carattere == lettera:
            conteggio += 1
    return conteggio


# ---------------------------------------------------------
# PARTE 1: ITERAZIONE E CICLI FOR (10 Esercizi)
# ---------------------------------------------------------

def raddoppia_caratteri(stringa):
    # 1. Restituisci una stringa dove ogni carattere è ripetuto due volte.
    # Test Case: "Ciao" -> "CCiiaaoo"
    pass

def conta_vocali(stringa):
    # 2. Conta quante vocali (a, e, i, o, u) sono presenti nella stringa.
    # Test Case: "Python" -> 1
    pass

def inverti_con_for(stringa):
    # 3. Inverti la stringa usando un ciclo for (non usare lo slicing [::-1]).
    # Test Case: "Sfida" -> "adifS"
    pass

def solo_posizioni_pari(stringa):
    # 4. Crea una nuova stringa usando solo i caratteri che si trovano in un indice pari.
    # Test Case: "Computer" -> "Cmue"
    pass

def sostituisci_spazi(stringa):
    # 5. Sostituisci ogni spazio " " con un trattino "-" usando un ciclo for.
    # Test Case: "A B C" -> "A-B-C"
    pass

def stringa_a_lista_codici(stringa):
    # 6. Trasforma la stringa in una lista contenente il codice ASCII di ogni carattere (usa ord()).
    # Test Case: "Ab" -> [65, 98]
    pass

def alterna_maiuscolo(stringa):
    # 7. Restituisci la stringa con i caratteri in posizione pari maiuscoli e dispari minuscoli.
    # Test Case: "casa" -> "CaSa"
    pass

def trova_prima_vocale(stringa):
    # 8. Restituisci l'indice della prima vocale che incontri. Se non ci sono, restituisci -1.
    # Test Case: "Gym" -> -1 | "Mela" -> 1
    pass

def raggruppa_trattini(n):
    # 9. Ricevi un intero n e genera una stringa con n gruppi di "*-*".
    # Test Case: 3 -> "*-**-**-*"
    pass

def conta_maiuscole(stringa):
    # 10. Conta quante lettere maiuscole sono presenti nella stringa.
    # Test Case: "ProGramma" -> 2
    pass


# ---------------------------------------------------------
# PARTE 2: ALGORITMI DI FILTERING (10 Esercizi)
# ---------------------------------------------------------

def solo_consonanti(stringa):
    # 1. Restituisci una stringa che contenga solo le consonanti dell'originale.
    # Test Case: "Informatica" -> "nfrmtc"
    pass

def rimuovi_punteggiatura(stringa):
    # 2. Data una stringa, elimina punti, virgole e punti esclamativi (.,!).
    # Test Case: "Ehilà! Come va?" -> "Ehilà Come va" (ignora il punto interrogativo per ora)
    pass

def filtra_numeri(stringa):
    # 3. Estrai solo i caratteri numerici da una stringa mista.
    # Test Case: "Codice123" -> "123"
    pass

def stringa_senza_doppie(stringa):
    # 4. Rimuovi i caratteri consecutivi identici (es. "mamma" -> "mama").
    # Test Case: "Aaaabbbb" -> "Ab"
    pass

def solo_parole_lunghe(testo):
    # 5. (Difficile) Ricevi una stringa di parole separate da spazi. 
    # Restituisci una stringa con solo le parole più lunghe di 3 caratteri.
    # Test Case: "Il gatto corre" -> "gatto corre"
    pass

def filtra_maiuscole_stringa(stringa):
    # 6. Crea una nuova stringa che contenga solo le lettere maiuscole trovate.
    # Test Case: "uNiversitÀ" -> "NÀ"
    pass

def nascondi_caratteri(stringa):
    # 7. Sostituisci ogni carattere tranne il primo e l'ultimo con un asterisco "*".
    # Test Case: "Segreto" -> "S*****o"
    pass

def estrai_esadecimali(stringa):
    # 8. Mantieni solo i caratteri che sono cifre (0-9) o lettere dalla 'a' alla 'f'.
    # Test Case: "gh12afz" -> "12af"
    pass

def rimuovi_vocali_specifiche(stringa, vocali_da_rimuovere):
    # 9. Rimuovi dalla stringa solo le vocali indicate nel secondo parametro.
    # Test Case: ("Parallelo", "ae") -> "Prlllo"
    pass

def verifica_presenza_numeri(stringa):
    # 10. Restituisci True se la stringa contiene almeno un numero, altrimenti False.
    # Test Case: "User2024" -> True | "Admin" -> False
    pass