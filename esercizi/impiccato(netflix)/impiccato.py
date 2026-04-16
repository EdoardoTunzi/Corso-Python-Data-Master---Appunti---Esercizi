import csv
import random
import string
import os

vocabulary = []

# with open("netflix_titles.csv") as csvfile:

with open(os.path.join(os.path.dirname(__file__), "netflix_titles.csv")) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        countries = row["country"].split(", ")
        if "Italy" in countries:
            vocabulary.append(row["title"])

# print(vocabulary)

letters = []
attempts = 5
guessed = ""

# random.seed(a=0)
random_index = random.randrange(0, len(vocabulary))

word = vocabulary[random_index].lower()


def init_guessed(plainText):
    w = ""
    for char in plainText:
        if char.isspace() or char in string.punctuation:
            w += char
        else:
            w += "-"
    return w


guessed = init_guessed(word)


def check_letters(l, w):
    found = False

    for i in w:
        if l == i:
            found = True
            break

    return found


def find_occurrences(l, w):
    occurrences = []
    for i in range(0, len(w)):
        if l == w[i]:
            occurrences.append(i)
    return occurrences


def sub_letters(l, pos, g):
    letters_list = list(g)
    letters_list[pos] = l
    return "".join(letters_list)


while True:
    print("\n--- GIOCO DELL'IMPICCATO ---")
    print(f"Titolo del film Netflix da indovinare: {guessed}")
    print(f"Tentativi rimasti: {attempts}")
    choice = input("Prova a indovinare il titolo o inserisci 0 per uscire: ")

    if choice == "0":
        break
    elif choice.lower() == word:
        print("Complimenti! Hai indovinato il titolo!")
        break
    else:
        print("Non hai indovinato !")
        print("Lettere estratte: {}".format(letters))
        choice = input("Estrai una lettera: ")
        choice = choice.lower()

        if check_letters(choice, letters):
            print("Hai già usato questa lettera.")
        else:
            letters.append(choice)
            if check_letters(choice, word):
                print(f"Bravo! La lettera '{choice}' è presente nel titolo.")
                occ = find_occurrences(choice, word)
                for pos in occ:
                    guessed = sub_letters(choice, pos, guessed)
                if guessed == word:
                    print(f"Complimenti! Hai indovinato il titolo: {word}")
                    break
            else:
                print(f"La lettera '{choice}' non è presente nel titolo.")
                attempts -= 1
                print(f"Tentativi rimasti: {attempts}")
                if attempts == 0:
                    print("GAME OVER")
                    print(f"Il titolo del film era: {word}")
                    print("")
                    break
