import pandas as pd

# --- DATI INIZIALI E CREAZIONE DATAFRAME ---
data = {
    'Nome': ['Alice', 'Bob', 'Charlie', 'David', 'Elena', 'Federico', 'Giorgia'],
    'Dipartimento': ['HR', 'IT', 'IT', 'Marketing', 'Sales', 'IT', 'Sales'],
    'Stipendio': [31000, 45000, 52000, 38000, 42000, 48000, 33000],
    'Anni_Esperienza': [2, 5, 10, 4, 7, 6, 3]
}

indici_personalizzati = ['ID_001', 'ID_002', 'ID_003', 'ID_004', 'ID_005', 'ID_006', 'ID_007']

# Creazione del DataFrame
df = pd.DataFrame(data, index=indici_personalizzati)

# ---------------------------------------------------------
# 1. ESERCIZIO: 
# Usa un comando per visualizzare le informazioni generali del DataFrame 
# (nomi colonne, tipi di dati, valori non nulli).
# Scrivi qui sotto:


# ---------------------------------------------------------
# 2. ESERCIZIO: Seleziona solo la colonna 'Nome' e salvala in una variabile.
# Scrivi qui sotto:


# ---------------------------------------------------------
# 3. ESERCIZIO: Seleziona le colonne 'Nome' e 'Stipendio' contemporaneamente.
# Scrivi qui sotto:


# ---------------------------------------------------------
# 4. ESERCIZIO: Estrai le prime 3 righe del DataFrame usando il metodo .head().
# Scrivi qui sotto:


# ---------------------------------------------------------
# 5. ESERCIZIO: Estrai le prime 5 righe del DataFrame usando lo slicing ([:n]).
# Scrivi qui sotto:


# ---------------------------------------------------------
# 6. ESERCIZIO: Filtra il DataFrame per mostrare solo chi ha uno 'Stipendio' 
# superiore a 40.000.
# Scrivi qui sotto:


# ---------------------------------------------------------
# 7. ESERCIZIO: Seleziona tutte le righe dove il 'Dipartimento' è uguale a 'IT'.
# Scrivi qui sotto:


# ---------------------------------------------------------
# 8. ESERCIZIO: Filtra i dipendenti che hanno uno 'Stipendio' > 35.000 
# E contemporaneamente più di 5 'Anni_Esperienza'.
# Scrivi qui sotto:


# ---------------------------------------------------------
# 9. ESERCIZIO: Filtra i dipendenti che appartengono al Dipartimento 'HR' 
# OPPURE al Dipartimento 'Marketing'.
# Scrivi qui sotto:


# ---------------------------------------------------------
# 10. ESERCIZIO: Usa .loc per selezionare solo la colonna 'Nome' 
# delle righe in cui 'Anni_Esperienza' è minore di 5.
# Scrivi qui sotto: