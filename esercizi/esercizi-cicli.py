import random

# 1 Assegnazione Semplice: Crea tre variabili per rappresentare il tuo nome, la tua età e la tua città, poi stampale separatamente
name = "EDOARDO"
age = 36
city = "Bari"

print("Il mio nome è:", name)
print("La mia età è:", age)
print("La mia città è:", city)
# 2 Verifica Maggiorenne: Chiedi all'utente la sua età tramite input(); usa un'istruzione if-else per stampare "Sei maggiorenne" se l'età è 18 o superiore, altrimenti "Sei minorenne"
userAge = int(input("Inserisci la tua età: "))

if userAge >= 18:
    print("Sei maggiorenne")
else:
    print("Sei minorenne")

# 3 Somma da 1 a N: Chiedi un numero positivo N e usa un ciclo for con la funzione range() per calcolare e stampare la somma di tutti i numeri da 1 a N
n = int(input("Inserisci un numero positivo: "))
sum = 0
for num in range(1, n + 1):
    sum += num
print("La somma dei numeri da 1 a", n, "è:", sum)

# 4 Numeri Pari: Scrivi un ciclo for che stampi tutti i numeri da 1 a 20, ma utilizza l'istruzione continue per saltare tutti i numeri dispari
for num in range(1, 21):
    if num % 2 != 0:
        continue
    print(num)

# 5 Indovina il Numero: Genera un numero casuale tra 1 e 10. Usa un ciclo while per continuare a chiedere all'utente di indovinare finché non trova quello corretto
randomNum = random.randint(1, 10)
while True:
    guess = int(input("Inserisci un numero tra 1 e 10: "))
    if guess == randomNum:
        print("Hai indovinato!")
        break
    else:
        print("Riprova!")

# 7 Interruzione Forzata: Crea un ciclo while True che chiede all'utente di inserire una parola. Il ciclo deve interrompersi usando break solo se l'utente scrive "esci"
while True:
    inputWord = input("Inserisci una parola (scrivi 'esci' per terminare): ")
    if inputWord.lower() == "esci":
        print("Programma terminato.")
        break
    else:
        print("Hai inserito:", inputWord)

# 8 Verifica Numero Primo: Scrivi un programma che utilizzi un ciclo for e una condizione if per determinare se un numero inserito dall'utente è primo (divisibile solo per 1 e per se stesso)
num1 = int(input("Inserisci un numero: "))
if num1 % 1 == 0 and num1 / num1 == 1:
    print(num1, "è un numero primo.")
else:
    print(num1, "non è un numero primo.")
# 9 Media Voti Dinamica: Usa un ciclo while per permettere all'utente di inserire una serie di voti; il ciclo deve terminare quando viene scritta la parola "fine", calcolando poi la media dei voti inseriti
voti = []

while True:
    inputVoto = input("Inserisci un voto (scrivi 'fine' per terminare): ")
    if inputVoto.lower() == "fine":
        break
    voti.append(int(inputVoto))
if voti:
    media = sum(voti) / len(voti)
    print("La media dei voti inseriti è:", media)
else:
    print("Nessun voto inserito.")
