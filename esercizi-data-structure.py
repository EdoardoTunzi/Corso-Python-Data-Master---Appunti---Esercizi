"""# 1️⃣ Somma lista
# Calcola la somma di tutti gli elementi usando un ciclo
numeri1 = [1, 2, 3, 4, 5]
sum = 0
for numero in numeri1:
    sum += numero
print(sum)


# 2️⃣ Numeri pari
# Crea una nuova lista con solo i numeri pari
numeri2 = [1, 2, 3, 4, 5, 6]
numeriPari = []
for numero in numeri2:
    if numero % 2 == 0:
        numeriPari.append(numero)
print(numeriPari)

# 3️⃣ Conteggio stringhe
# Conta quante volte compare "ciao"
parole1 = ["ciao", "hello", "ciao", "hi"]
print("la parola ciao appare", parole1.count("ciao"), "volte nella lista")


# 4️⃣ Tuple unpacking
# Assegna i valori a due variabili e stampali
coordinate = (10, 20)
a, b = coordinate
print(a)
print(b)
# 5️⃣ Verifica presenza
# Verifica se il numero 3 è presente
numeri3 = [1, 2, 3, 4]
for num in numeri3:
    if num == 3:
        print("La lista contiene il numero 3")


# 6️⃣ Rimuovi duplicati
# Rimuovi i duplicati usando un set
numeri4 = [1, 2, 2, 3, 4, 4, 5]
newSet = set(numeri4)
print(newSet)

# 7️⃣ Dizionario base
# Aggiungi una nuova chiave "città"
persona1 = {"nome": "Edo", "eta": 17}
persona1["città"] = "Bari"
print(persona1)

# 8️⃣ Iterazione dizionario
# Stampa tutte le chiavi e i valori
persona2 = {"nome": "Edo", "eta": 17}
print(persona2.items())

# 9️⃣ Lista di tuple
# Stampa solo i primi valori usando unpacking
punti = [(1, 2), (3, 4), (5, 6)]
p1, p2, p3 = punti
print(p1[0])
print(p2[0])
print(p3[0])

# 🔟 Filtra numeri
# Crea una lista con numeri maggiori di 20
numeri5 = [10, 15, 20, 25, 30]
newList = []
for num in numeri5:
    if num >= 20:
        newList.append(num)
print("Lista con numeri maggiori di 20:", newList)

# 1️⃣1️⃣ Conta elementi (dict)
# Crea un dizionario con il conteggio di ogni parola
parole2 = ["a", "b", "a", "c", "b", "a"]
dictCount = {}

for lettera in parole2:
    if lettera in dictCount:
        dictCount[lettera] += 1
    else:
        dictCount[lettera] = 1

print(dictCount)

# 1️⃣2️⃣ Intersezione set
# Trova gli elementi in comune
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
set_c = set_a & set_b
print(set_c)

# 1️⃣3️⃣ Merge dizionari
# Unisci i due dizionari
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
d3 = d1 | d2
print(d3)

# 1️⃣4️⃣ Trova massimo
# Trova il numero più grande senza usare max()
numeri6 = [5, 12, 3, 20, 7]
biggestInt = numeri6[0]
for num in numeri6:
    if num > biggestInt:
        biggestInt = num

print("Il numero piu grande è:", biggestInt)


# 1️⃣5️⃣ Raggruppamento per categoria
# Crea un dizionario raggruppato per categoria
prodotti = [
    {"nome": "maglia", "categoria": "abbigliamento"},
    {"nome": "jeans", "categoria": "abbigliamento"},
    {"nome": "mouse", "categoria": "tech"},
]
raggruppati = {}

for prodotto in prodotti:
    nome = prodotto["nome"]
    categoria = prodotto["categoria"]
    if categoria in raggruppati:
        raggruppati[categoria].append(nome)
    else:
        raggruppati.setdefault(categoria, []).append(nome)

print(raggruppati)"""

# 🧠 Esercizi Python – parte 2 (16-30)
# Focus: cicli, liste, tuple, set, dizionari, matrici, unpacking, while, cicli annidati

# 1️⃣6️⃣ Stampa multipli di 3
# Lista di numeri già fornita. Hint: usa un ciclo for + condizione %

numeri16 = list(range(1, 21))
for numero in numeri16:
    if numero % 3 == 0:
        print("IL numero", numero, "è divisibile per 3")


# 1️⃣7️⃣ Filtra stringhe che iniziano con 'p'
# Lista di parole fornita. Hint: ciclo for + controllo del primo carattere


parole17 = ["python", "java", "php", "c++", "perl"]
for parola in parole17:
    if parola[0] == "p":
        print(parola)

# 1️⃣8️⃣ Somma valori di un dizionario
# Dizionario con valori numerici. Hint: itera sulle chiavi o sui valori


dizionario18 = {"a": 10, "b": 20, "c": 5}
somma2 = 0
for value in dizionario18.values():
    somma2 += value

print(somma2)

# 1️⃣9️⃣ Controlla se tutti i numeri in lista sono positivi
# Lista di numeri fornita. Hint: ciclo for + condizione, puoi usare un flag booleano

numeri19 = [1, 2, 3, -4, 5]
boolValue = True
for numero in numeri19:
    if numero < 0:
        boolValue = False
if boolValue:
    print("La lista contiene solo numeri positivi")
else:
    print("La lista contiene numeri negativi")


# 2️⃣0️⃣ Unpack lista di tuple
# Lista di tuple fornita. Hint: ciclo for + unpacking tuple


punti20 = [(1, 2), (3, 4), (5, 6)]
newList = []
for x, y in punti20:
    newList.append(x)
    newList.append(y)
print("nuova lista", newList)


# 2️⃣1️⃣ While loop – somma fino a superare 50
# Lista di numeri fornita. Hint: usa un indice o pop della lista, ciclo while e accumulatore


numeri21 = [5, 10, 15, 20, 25]
somma3 = 0
i = 0
while somma3 <= 50 and i < len(numeri21):
    somma3 += numeri21[i]
    print(numeri21[i])
    i += 1
print("Totale", somma3)

# 2️⃣2️⃣ Lista di quadrati
# Lista di numeri fornita. Hint: ciclo for + elevamento a potenza


numeri22 = [1, 2, 3, 4, 5]
quadrati = []
for numero in numeri22:
    quadrati.append(numero**2)
print(quadrati)

# 2️⃣3️⃣ Conta elementi unici
# Lista con duplicati. Hint: usa set e/o ciclo for


numeri23 = [1, 2, 2, 3, 4, 4, 5, 5, 5]
setNumeri23 = set(numeri23)
print(len(setNumeri23))

# 2️⃣4️⃣ Matrice 3x3 – somma righe
# Matrice già fornita. Hint: ciclo for annidato per sommare ogni riga


matrice24 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


for riga in matrice24:
    sommaRiga = 0
    for num in riga:
        sommaRiga += num
    print(sommaRiga)


# 2️⃣5️⃣ Matrice 3x3 – somma colonne
# Stessa matrice. Hint: ciclo for con indice colonna + ciclo interno per le righe


""" matrice25 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for colonna in range(len(matrice25[0])):
    sommaColonna = 0
    for indice in colonna:
        sommaColonna += colonna[indice]
    print(sommaColonna)
 """

# 2️⃣6️⃣ Dizionario di liste – aggiungi un elemento
# Dizionario fornito. Hint: seleziona la chiave giusta e usa il metodo corretto per aggiungere a una lista


dizionario26 = {"frutta": ["mela", "banana"], "verdura": ["carota", "zucchina"]}
dizionario26["frutta"].append("banana")
dizionario26["verdura"].append("melanzana")
print(dizionario26)


# 2️⃣7️⃣ Rimuovi elementi pari da lista
# Lista numerica. Hint: ciclo for + condizione % 2 oppure lista comprensione


numeri27 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dispari = []
for numero in numeri27:
    if numero % 2 != 0:
        print("rimuovo il numero dispari:", numero)
        dispari.append(numero)
print(dispari)
# 2️⃣8️⃣ Trova la parola più lunga
# Lista di parole. Hint: ciclo for + verifica lunghezza + variabile per memoria massima


parole28 = ["casa", "automobile", "AI", "programmazione"]
longestWord = ""
for word in parole28:
    if len(word) > len(longestWord):
        longestWord = word
print("La parola piu lunga è:", longestWord)

# 2️⃣9️⃣ Genera lista con tuple (numero, quadrato)
# Lista di numeri fornita. Hint: ciclo for + tuple + append


numeri29 = [1, 2, 3, 4, 5]
tupleNumQuadrato = []
for numero in numeri29:
    tupleNumQuadrato.append((numero, numero**2))
print(tupleNumQuadrato)


# 3️⃣0️⃣ Raggruppa numeri per parità
# Lista di numeri. Hint: crea un dizionario con chiavi "pari" e "dispari" e aggiungi numeri alle liste corrette


numeri30 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pari_e_dispari = {"pari": [], "dispari": []}

for numero in numeri30:
    if numero % 2 == 0:
        pari_e_dispari["pari"].append(numero)
    else:
        pari_e_dispari["dispari"].append(numero)

print(pari_e_dispari)
