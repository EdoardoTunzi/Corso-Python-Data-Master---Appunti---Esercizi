# 🧠 ESERCIZI COMPREHENSION (1–30)

# 1️⃣ Base – quadrati
# Crea una lista con i quadrati dei numeri
# Usa SOLO list comprehension
# %%
numeri1 = [1, 2, 3, 4, 5]
squared = [num**2 for num in numeri1]
print("Esercizio 1 - Lista con numeri quadrati:", squared)

# 2️⃣ Base – filtro pari
# Crea una lista con solo i numeri pari

numeri2 = [1, 2, 3, 4, 5, 6]
even = [num for num in numeri2 if num % 2 == 0]
print("Esercizio 2 - Lista numeri pari:", even)

# 3️⃣ Base – stringhe uppercase
# Trasforma tutte le parole in maiuscolo

parole3 = ["ciao", "python", "ai"]
capitalized = [w.upper() for w in parole3]
print("Esercizio 3 - Lista parole con prima lettera maiuscola:", capitalized)


# 4️⃣ Filtro stringhe lunghe
# Prendi solo le parole con lunghezza > 4

parole4 = ["ciao", "python", "java", "ai", "sviluppo"]
long_words = [w for w in parole4 if len(w) > 4]
print("Esercizio 4 - Lista parole piu lunghe di 4 caratteri:", long_words)

# 5️⃣ If/else inline
# Trasforma numeri in "pari" o "dispari"

numeri5 = [1, 2, 3, 4]
# Prima soluzione come richiesto
even_uneven1 = ["pari" if num % 2 == 0 else "dispari" for num in numeri5]


# Seconda soluzione
def getEvenUneven(n):
    if n % 2 == 0:
        return "pari"
    else:
        return "dispari"


even_uneven2 = [getEvenUneven(num) for num in numeri5]


print("Esercizio 5 - Lista pari/dispari:", even_uneven1)
print("Esercizio 5 - Lista pari/dispari:", even_uneven2)


# 6️⃣ Usa funzione data
# Usa questa funzione per filtrare i numeri pari


def is_even(x):
    return x % 2 == 0


numeri6 = [1, 2, 3, 4, 5, 6]
evens = [num for num in numeri6 if is_even(num)]
print("Esercizio 6 - Lista pari:", evens)

# 7️⃣ Usa funzione nella trasformazione
# Usa questa funzione per trasformare i numeri


def double(x):
    return x * 2


numeri7 = [1, 2, 3, 4]
doubles = [double(num) for num in numeri7]
print("Esercizio 7 - numeri raddoppiati: ", doubles)


# 8️⃣ Set comprehension base
# Crea un set con i quadrati (rimuove duplicati automaticamente)

numeri8 = [1, 2, 2, 3, 3, 4]
squaredSet = {num**2 for num in numeri8}
print("Esercizio 8 - set con quadrati ", squaredSet)


# 9️⃣ Set con filtro
# Crea un set con solo numeri dispari

numeri9 = [1, 2, 3, 4, 5, 6]
unevenSet = {num for num in numeri9 if num % 2 != 0}
print("Esercizio 9 - set con numeri dispari ", unevenSet)


# 🔟 Dict base
# Crea un dizionario numero: quadrato

numeri10 = [1, 2, 3, 4]
squaredDict = {num: num**2 for num in numeri10}
print("Esercizio 10 - dizionario con num:quadrato ", squaredDict)


# 1️⃣1️⃣ Dict con filtro
# Solo numeri pari come chiavi

numeri11 = [1, 2, 3, 4, 5, 6]
evenNameDict = {num: "pari" for num in numeri11 if num % 2 == 0}

print("Esercizio 11 - Solo numeri pari come chiavi", evenNameDict)
# 1️⃣2️⃣ Dict da tuple
# Crea un dizionario da lista di tuple

dati12 = [("a", 1), ("b", 2), ("c", 3)]
dictFromTuple = {chiave: valore for chiave, valore in dati12}
print("Esercizio 12 - dizionario da lista di tuple ", dictFromTuple)

# 1️⃣3️⃣ Inverti dizionario
# Scambia chiavi e valori

dizionario13 = {"a": 1, "b": 2}
inverted = {v: k for k, v in dizionario13.items()}
print("Esercizio 13 - dizionario invertito ", inverted)

# 1️⃣4️⃣ Usa len()
# Crea lista con lunghezza delle parole

parole14 = ["ciao", "python", "AI"]
lengthList = [len(w) for w in parole14]
print("Esercizio 14 - lista con lunghezza delle parole ", lengthList)

# 1️⃣5️⃣ Filtra usando funzione len()
# Solo parole con lunghezza >= 5

parole15 = ["ciao", "python", "java", "AI"]
longwords2 = [w for w in parole15 if len(w) >= 5]

print("Esercizio 15- Solo parole con lunghezza >= 5 ", longwords2)

# 1️⃣6️⃣ Matrice – flatten
# Appiattisci la matrice in una lista singola
# Usa comprehension annidata

matrice16 = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrice16 for num in row]

print("Esercizio 16 - Matrice flatten", flattened)

# 1️⃣7️⃣ Matrice – filtro
# Prendi solo numeri pari dalla matrice

matrice17 = [[1, 2], [3, 4], [5, 6]]
flattenedEvens = [num for row in matrice17 for num in row if num % 2 == 0]
print("Esercizio 17- solo numeri pari dalla matrice ", flattenedEvens)

# 1️⃣8️⃣ Matrice – trasformazione
# Crea una nuova matrice con numeri al quadrato

matrice18 = [[1, 2], [3, 4]]
matrixSquared = [[num**2 for num in row] for row in matrice18]
print("Esercizio 18 - matrice con numeri al quadrato", matrixSquared)

# 1️⃣9️⃣ Matrice – somma righe
# Crea una lista con la somma di ogni riga

matrice19 = [[1, 2], [3, 4], [5, 6]]
summedMatrix = [sum(row) for row in matrice19]
print("Esercizio 19 - lista con la somma di ogni riga della matrice", summedMatrix)

# 2️⃣0️⃣ If/else complesso
# Se numero > 3 → "alto", altrimenti "basso"

numeri20 = [1, 2, 3, 4, 5]
highLow = ["alto" if num > 3 else "basso" for num in numeri20]
print('Esercizio 20 -Se numero > 3 → "alto", altrimenti "basso" ', highLow)

# 2️⃣1️⃣ Funzione custom da creare
# Crea una funzione is_multiple_of_3(x)
# Poi usa comprehension per filtrare i multipli di 3

numeri21 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def is_multiple_of_3(n):
    if n % 3 == 0:
        return True
    else:
        return False


list2 = [num for num in numeri21 if is_multiple_of_3(num)]
print("Esercizio 21 - filtrare i multipli di 3", list2)

# 2️⃣2️⃣ Funzione nella trasformazione
# Crea funzione square(x) e usala nella comprehension


def square(n):
    return n**2


numeri22 = [1, 2, 3, 4]
squared2 = [square(n) for n in numeri22]
print("Esercizio 22 - funzione square(x)", squared2)

# 2️⃣3️⃣ Dict avanzato
# Crea dict con chiave numero e valore "pari"/"dispari"

numeri23 = [1, 2, 3, 4]
dictEvenUneven = {num: "pari" if num % 2 == 0 else "dispari" for num in numeri23}
print("Esercizio 23 - dict con chiave numero e valore pari/dispari ", dictEvenUneven)

# 2️⃣4️⃣ Set da matrice
# Crea un set con tutti i valori unici della matrice

matrice24 = [[1, 2, 2], [3, 4, 4]]
newSet = {num for row in matrice24 for num in row}
print("Esercizio 24- set con tutti i valori unici della matrice", newSet)

# 2️⃣5️⃣ Doppio filtro
# Numeri pari e > 5

numeri25 = [1, 2, 3, 4, 5, 6, 7, 8]
newSet2 = [num for num in numeri25 if num % 2 == 0 and num > 5]
print("Esercizio 25 - Numeri pari e > 5", newSet2)

# 2️⃣6️⃣ Dict da lista parole
# Chiave parola, valore lunghezza

parole26 = ["python", "ai", "sviluppo"]
words = {w: len(w) for w in parole26}
print("Esercizio 26 - Chiave parola, valore lunghezza ", words)

# 2️⃣7️⃣ Matrice – flatten con filtro
# Appiattisci e prendi solo numeri > 3

matrice27 = [[1, 2], [3, 4], [5, 6]]
flattened3 = [num for row in matrice27 for num in row if num > 3]
print("Esercizio 27 - Appiattisci e prendi solo numeri > 3", flattened3)

# 2️⃣8️⃣ Comprehension annidata avanzata
# Crea lista con tutte le combinazioni tra due liste (tipo prodotto cartesiano)

listaA = [1, 2, 3]
listaB = ["a", "b"]

newList = [str(num) + ch for num in listaA for ch in listaB]
print("Esercizio 28 - prodotto cartesiano ", newList)

# 2️⃣9️⃣ Dict complesso
# Chiave numero, valore lista dei suoi multipli fino a 3 volte (es: 2 → [2,4,6])
# Usa comprehension annidata

numeri29 = [1, 2, 3]
newList2 = {num: [num * n for n in range(1, 4)] for num in numeri29}
print(
    "Esercizio 29 - Chiave numero, valore lista dei suoi multipli fino a 3 volte ",
    newList2,
)

# 3️⃣0️⃣ 🔥 HARD – matrice condizionale
# Trasforma la matrice:
# - se numero pari → mantieni
# - se dispari → metti 0
# Usa comprehension annidata con if/else

matrice30 = [[1, 2, 3], [4, 5, 6]]

matrix2 = [[num if num % 2 == 0 else 0 for num in row] for row in matrice30]
print("Esercizio 30 -  ", matrix2)
# %%
