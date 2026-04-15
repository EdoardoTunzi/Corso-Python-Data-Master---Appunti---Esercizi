# %%
import requests
import math
from requests.exceptions import HTTPError

# ========================================
# 🧠 ESERCIZI PYTHON – requests (1–10)
# Focus: HTTP GET, JSON, params, error handling, logica
# Difficoltà: crescente
# ========================================


# ========================================
# 1️⃣ GET base
# ========================================
# Traccia:
# Fai una richiesta GET a:
# https://jsonplaceholder.typicode.com/posts/1
# Stampa il titolo del post.
#
resp = requests.get("https://jsonplaceholder.typicode.com/posts/1")
data = resp.json()

# print(data["title"])


# Obiettivo:
# - Familiarizzare con requests.get()
# - Convertire risposta in JSON
# - Accedere a una chiave del dizionario


# ========================================
# 2️⃣ Lista di dati
# ========================================
# Traccia:
# Fai una GET a:
# https://jsonplaceholder.typicode.com/users
# Stampa solo i nomi degli utenti.
#
# Obiettivo:
# - Iterare su lista di dizionari
# - Estrarre un campo specifico

resp2 = requests.get("https://jsonplaceholder.typicode.com/users")
data2 = resp2.json()
usersNames = [user["name"] for user in data2]
# print(usersNames)

# ========================================
# 4️⃣ Parametri query
# ========================================
# Traccia:
# Fai una GET a:
# https://jsonplaceholder.typicode.com/comments
# Filtra solo i commenti con postId = 1 usando params.
#
# Obiettivo:
# - Usare parametro params={}
# - Non filtrare lato Python ma via URL
parametri = {"postId": 1}
resp3 = requests.get("https://jsonplaceholder.typicode.com/comments", params=parametri)
data3 = resp3.json()
# print(data3)


# ========================================
# 5️⃣ Controllo status code
# ========================================
# Traccia:
# Fai una richiesta a un endpoint valido e uno non valido.
# Gestisci il caso di errore stampando:
# "Errore nella richiesta"
#
# Obiettivo:
# - Usare response.status_code
# - Capire differenza tra 200 e errori
for url in ["https://www.theguardian.com", "https://repubblica.it/doesNotExist"]:
    try:
        response = requests.get(url)

        if response.status_code == 200:
            print("Successo")
        else:
            response.raise_for_status()

    except requests.exceptions.RequestException as err:
        print(f"Errore nella richiesta: {err}")


# ========================================
# 6️⃣ Funzione riutilizzabile
# ========================================
# Traccia:
# Crea una funzione:
# get_json(url)
# che ritorna il JSON della risposta.
#
# Se la richiesta fallisce:
# ritorna None.
#
# Obiettivo:
# - Incapsulare requests
# - Gestire errori base
def get_json(url):
    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        return data
    except requests.exceptions.RequestException:
        return None


# ========================================
# 9️⃣ Costruzione URL dinamico
# ========================================
# Traccia:
# Crea una funzione:
# get_user_posts(user_id)
#
# Che chiama:
# https://jsonplaceholder.typicode.com/posts?userId=X
#
# E ritorna i titoli dei post.
#
# Obiettivo:
# - Usare f-string o params
# - Creare funzioni dinamiche
def get_user_posts(user_id):
    params2 = {"userId": user_id}
    resp = requests.get("https://jsonplaceholder.typicode.com/posts", params=params2)
    # resp = requests.get(f"https://jsonplaceholder.typicode.com/posts?userId={user_id}")
    data = resp.json()
    postTitleList = [post["title"] for post in data]
    return postTitleList


print(get_user_posts(10))


# ========================================
# 🔟 🔥 HARD – Aggregazione dati API
# ========================================
# Traccia:
# Usa:
# https://jsonplaceholder.typicode.com/users
# https://jsonplaceholder.typicode.com/posts
#
# Crea un dizionario:
# {
#   "NomeUtente": numero_post
# }
#
# Obiettivo:
# - Fare 2 chiamate API
# - Collegare dati (userId)
# - Usare dizionari e cicli
#
# Hint:
# - users → id, name
# - posts → userId
def postNumberPerUserById(userId):
    dizionario = {}

    response1 = requests.get("https://jsonplaceholder.typicode.com/users")
    userData = response1.json()
    user = [user for user in userData if user["id"] == userId]

    response2 = requests.get(
        f"https://jsonplaceholder.typicode.com/posts?userId={userId}"
    )
    postsData = response2.json()

    dizionario[user[0]["name"]] = len(postsData)

    return dizionario


print(postNumberPerUserById(10))

# ========================================
# BONUS 🔥🔥 (facoltativo)
# ========================================
# Traccia:
# Trova l'utente con più post
#
# Output:
# "L'utente con più post è X con Y post"
#
# Obiettivo:
# - max()
# - logica aggregazione


def userWithMostPosts():

    response1 = requests.get("https://jsonplaceholder.typicode.com/users")
    userData = response1.json()

    response2 = requests.get(f"https://jsonplaceholder.typicode.com/posts")
    postsData = response2.json()

    counts = {}
    for post in postsData:
        userId = post["userId"]
        if userId in counts:
            counts[userId] += 1
        else:
            counts[userId] = 1

    maxPosts = -1
    bestUserId = None

    for userId, count in counts.items():
        if count > maxPosts:
            maxPosts = count
            bestUserId = userId

    bestUserName = ""
    for user in userData:
        if user["id"] == bestUserId:
            bestUserName = user["name"]
            break

    print(f"L'utente con più post è {bestUserName} con {maxPosts} post")


userWithMostPosts()


# %%

"""
========================================
🧠 Esercizio 1: Il Filtro "Smart" per API
(Manipolazione Dati)
========================================

● Traccia:
Scrivi una funzione che interroghi un'API pubblica
(es. https://jsonplaceholder.typicode.com/todos)
per ottenere una lista di attività.

La funzione deve accettare un parametro opzionale
completata (booleano) e restituire una lista filtrata
di titoli di attività che corrispondono allo stato richiesto.

● Algoritmo:
1. Effettua una chiamata GET all'URL.
2. Converti la risposta da JSON a una lista di dizionari Python.
3. Usa un ciclo o una filter/list comprehension per selezionare
   solo i dizionari dove la chiave "completed" corrisponde
   al parametro passato.
● Esempio I/O:
Input: filtra_todo(completata=True)

Output:
["delectus aut autem",
 "quis ut nam facilis et officia qui",
 ...]
(solo i titoli dei task completati)
"""


def filtra_todo(completata=None):

    url = "https://jsonplaceholder.typicode.com/todos"

    # richiesta GET
    response = requests.get(url)

    # converti JSON
    data = response.json()

    # filtra dati
    if completata is None:
        risultati = [item["title"] for item in data]
        return risultati
    else:
        risultati = [item["title"] for item in data if item["completed"] == completata]
        return risultati


# Test
print(filtra_todo(completata=True))


"""
========================================
🧠 Esercizio 2: Traduttore CLI Interattivo
========================================

● Traccia:
Crea un programma che chieda all'utente una parola
in italiano e la traduca in inglese usando l'API di MyMemory.

Il programma deve continuare finché l'utente non scrive "esci".

● Algoritmo:
1. Usa un ciclo while True.
2. Prendi l'input dell'utente.
   - Se è "esci", usa break.
3. Costruisci l'URL:
   https://api.mymemory.translated.net/get
   passando i parametri:
   - q (la parola)
   - langpair (valore: it|en)
4. Invia la richiesta GET con requests.
5. Estrai la traduzione dal JSON seguendo il percorso:
   responseData -> translatedText.

● Esempio I/O:
Input: "tavolo"

Output:
"Traduzione: table"
"""


def traduttore_cli():
    """
    TODO:
    - Loop infinito (while True)
    - Input utente
    - Se "esci" → break
    - Chiama API MyMemory
    - Estrai traduzione
    """

    base_url = "https://api.mymemory.translated.net/get"

    while True:
        parola = input("Inserisci parola (o 'esci'): ")

        # gestisci uscita
        if parola == "esci":
            break

        # crea params
        params = {"q": parola, "langpair": "it|en"}

        # GET request
        response = requests.get(base_url, params=params)

        # JSON parsing
        data = response.json()

        # estrai traduzione
        traduzione = data["responseData"]["translatedText"]

        print("Traduzione:", traduzione)


traduttore_cli()

"""
========================================
🧠 Esercizio 3:
Calcolatore di Distanza Geografica
(Logica Matematica + API)
========================================

● Traccia:
Crea uno script che accetti due indirizzi IP e calcoli
la distanza in chilometri tra le loro posizioni geografiche stimate.

Dovrai usare la formula di Haversine, che richiede
di lavorare su una sfera (la Terra).

● Passaggi matematici:
1. Ottieni Latitudine (lat) e Longitudine (lon) in gradi decimali.
2. Converti i gradi in radianti:
   rad = gradi * (PI / 180)
   - latitudine → phi
   - longitudine → lambda
3. Calcola le differenze:
   Δphi = phi_2 - phi_1
   Δlambda = lambda_2 - lambda_1
4. Applica la formula:
   (dove R è il raggio della Terra, circa 6371 km)

● Algoritmo:
1. Usa un'API di Geolocation (es. ip-api.com)
   per ottenere latitudine (phi) e longitudine (lambda)
   di entrambi gli IP.
2. Applica la Formula di Haversine
   per calcolare la distanza su una sfera (la Terra).
3. Restituisci il risultato espresso in KM.

● Esempio I/O:
Input:
IP1: "8.8.8.8"
IP2: "1.1.1.1"

Output:
"La distanza stimata tra gli IP è di 8540.2 km"
"""


def get_location(ip):
    url = f"http://ip-api.com/json/{ip}"

    response = requests.get(url)
    data = response.json()

    lat = data["lat"]
    lon = data["lon"]

    return lat, lon


def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # km
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    lambda1 = math.radians(lon1)
    lambda2 = math.radians(lon2)
    delta_phi = phi2 - phi1
    delta_lambda = lambda2 - lambda1

    a = (
        math.sin(delta_phi / 2) ** 2
        + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    )

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distanza = R * c

    return distanza


def distanza_ip(ip1, ip2):
    lat1, lon1 = get_location(ip1)
    lat2, lon2 = get_location(ip2)

    distanza = haversine(lat1, lon1, lat2, lon2)
    print(f"La distanza stimata tra gli IP è di {distanza:.2f} km")


# Test
distanza_ip("8.8.8.8", "77.88.8.8")
