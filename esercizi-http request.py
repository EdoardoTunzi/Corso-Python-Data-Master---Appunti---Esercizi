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

import requests


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
import math


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
