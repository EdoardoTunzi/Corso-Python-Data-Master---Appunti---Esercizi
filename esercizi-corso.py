"""
Esercizio 1: Validatore di Quadrati Magici

Traccia: Un quadrato magico è una matrice quadrata N x N (rappresentata come una
lista di liste) in cui la somma dei numeri di ogni riga, di ogni colonna e delle due diagonali
è sempre la stessa. Scrivi un programma che verifichi se una matrice data è un quadrato
magico.
Algoritmo:
○ Calcola la "costante magica" usando la prima riga come riferimento.
○ Usa i cicli per sommare gli elementi di ogni riga e confrontarli con la costante.
○ Fai lo stesso per le colonne (fissando l'indice della colonna e iterando sulle
righe).
○ Calcola la somma delle due diagonali: la principale (dove l'indice di riga è uguale
a quello di colonna i=j) e la secondaria (dove la somma degli indici è uguale a
N-1).
Esempio I/O:
○ Input: [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
○ Output: "La matrice è un quadrato magico (costante: 15)"
○ Input: [[1, 2], [3, 4]]
○ Output: "La matrice non è un quadrato magico"
"""

# %%
matrix = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
matrix2 = [[1, 2], [3, 4]]


def isMagicBox(matrice):
    firstRow = sum(matrice[0])
    rowIsMagic = True
    colIsMagic = True
    n = len(matrice)
    diag1IsMagic = True
    diag2IsMagic = True
    # righe
    for row in matrice:
        if sum(row) != firstRow:
            rowIsMagic = False
    # colonne
    for col in range(n):
        colSum = 0
        for row in matrice:
            colSum += row[col]
        if colSum != firstRow:
            colIsMagic = False

    # diagonale principale
    diag1Sum = 0
    for i in range(n):
        diag1Sum += matrice[i][i]
    if diag1Sum != firstRow:
        diag1IsMagic = False

    # diagonale secondaria
    diag2Sum = 0
    for i in range(n):
        diag2Sum += matrice[i][n - 1 - i]
    if diag2Sum != firstRow:
        diag2IsMagic = False

    # risultato finale
    if rowIsMagic and colIsMagic and diag1IsMagic and diag2IsMagic:
        print("La matrice è un quadrato magico. Costante:", firstRow)
    else:
        print("La matrice non è un quadrato magico")


isMagicBox(matrix)
# %%

"""
Esercizio 2: Sistema di Suggerimento "Interessi Comuni"
Traccia: Gestisci un database di utenti dove ogni utente ha un set di interessi. Scrivi una
funzione che, dato un utente target, trovi l'utente "più simile" basandosi sull'Indice di Jaccard.
Algoritmo: L'indice di Jaccard misura la somiglianza tra due insiemi A e B. Si calcola
dividendo la dimensione dell'intersezione per la dimensione dell'unione: 
J(A, B) = |A ∩ B| / |A ∪ B|.
○ Rappresenta gli utenti in un dizionario: { "Nome": {"Interesse1","Interesse2"} }.
○ Calcola l'indice tra l'utente target e tutti gli altri.
○ Restituisce il nome dell'utente con il valore di J più alto.
Esempio I/O:
○ Input: Target: "Luca" (Interessi: {"Python","AI","Vela"})
○ Dati: {"Anna": {"AI", "Vela", "Yoga"}, "Marco": {"Python","C++"}}
○ Output: "L'utente più simile a Luca è Anna (Indice: 0.5)"
"""
# %%
# Dizionario utenti: chiave = nome, valore = set di interessi
utenti = {
    "Luca": {"Python", "AI", "Vela"},
    "Anna": {"AI", "Vela", "Yoga"},
    "Marco": {"Python", "C++", "AI"},
    "Sara": {"Python", "AI", "Vela", "Yoga"},
    "Paolo": {"C++", "Giochi", "AI"},
}

# Utente target
target = "Luca"


def getSimilarUsers(target, users):
    users_without_target = {k: v for k, v in users.items() if k != target}
    interests_target = users[target]
    max_index = -1
    similar_user = ""

    for user in users_without_target:
        interests_user = users_without_target[user]
        intersection = interests_user & interests_target
        union = interests_user | interests_target
        jacard_index = len(intersection) / len(union)

        if jacard_index > max_index:
            max_index = jacard_index
            similar_user = user

    print(f"L'utente più simile a {target} è {similar_user} (Indice: {max_index})")


getSimilarUsers("Luca", utenti)
# %%


"""
Esercizio 3: Scomposizione in Fattori Primi con Comprehension
Traccia: Dato un numero intero, restituisci la sua scomposizione in fattori primi sotto
forma di una lista di tuple, dove ogni tupla contiene (fattore, esponente). Usa una list
comprehension per formattare l'output finale partendo da un dizionario di conteggio.
Algoritmo:
○ Inizia a dividere il numero n per il più piccolo primo d=2.
● Finché n è divisibile per d, conta quante volte avviene la divisione (esponente) e
aggiorna n = n // d.
○ Incrementa d e ripeti finché n=1.
○ Memorizza i risultati in un dizionario {fattore: esponente} e usa una list
comprehension per trasformarlo in una lista di tuple.
Esempio I/O:
○ Input: 60
○ Output: [(2, 2), (3, 1), (5, 1)] (Spiegazione: 2^2 x 3^1 x 5^1 = 60)
○ Input: 13
○ Output: [(13, 1)]
"""
