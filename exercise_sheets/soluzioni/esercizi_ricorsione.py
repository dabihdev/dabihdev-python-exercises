# --- SOLUZIONI ESERCIZI RICORSIONE ---

# 1. Fattoriale
# Caso base: il fattoriale di 0 o 1 è 1.
def fattoriale(n):
    if n <= 1:
        return 1
    return n * fattoriale(n - 1)

# 2. Somma dei primi N numeri
# Caso base: se n è 1, la somma è 1.
def somma_n(n):
    if n == 1:
        return 1
    return n + somma_n(n - 1)

# 3. Elevamento a Potenza
# Caso base: qualsiasi numero elevato a 0 è 1.
def potenza(base, esponente):
    if esponente == 0:
        return 1
    return base * potenza(base, esponente - 1)

# 4. Sequenza di Fibonacci
# Casi base: F(0)=0, F(1)=1.
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# 5. Invertire una Stringa
# Caso base: stringa vuota o di un solo carattere.
def inverti_stringa(s):
    if len(s) <= 1:
        return s
    return s[-1] + inverti_stringa(s[:-1])

# 6. Somma degli elementi di una lista
# Caso base: lista vuota (somma = 0).
def somma_lista(lista):
    if not lista:
        return 0
    return lista[0] + somma_lista(lista[1:])

# 7. Conteggio delle cifre
# Caso base: il numero ha una sola cifra (n < 10).
def conta_cifre(n):
    if n < 10:
        return 1
    return 1 + conta_cifre(n // 10)

# 8. Verifica Palindromo
# Caso base: 0 o 1 carattere rimasto (True).
def is_palindromo(parola):
    if len(parola) <= 1:
        return True
    if parola[0] != parola[-1]:
        return False
    return is_palindromo(parola[1:-1])