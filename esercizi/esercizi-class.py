# 1️⃣ Classe base
# Crea una classe Persona con attributi:
# - nome
# - età
# Crea un metodo che stampa:
# "Mi chiamo X e ho Y anni"
class Persona:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getInfo(self):
        print(f"Mi chiamo {self.name} e ho {self.age} anni")

    def isOver18(self):
        if self.age >= 18:
            return True
        else:
            return False


# 2️⃣ Metodo personalizzato
# Aggiungi alla classe Persona un metodo:
# is_maggiorenne()
# che ritorna True/False


# 3️⃣ Più istanze
# Crea 3 oggetti Persona e stampa le loro info
p1 = Persona("Edoardo", 35)
p2 = Persona("Marco", 16)
p3 = Persona("Chiara", 18)
p1.getInfo()
p1.isOver18()
p2.getInfo()
p2.isOver18()
p3.getInfo()
p3.isOver18()


# 4️⃣ Classe con stato modificabile
# Crea una classe Contatore
# con attributo valore iniziale = 0
# metodi:
# - incrementa()
# - decrementa()
class Contatore:

    def __init__(self, counter=0):
        self.counter = counter

    def increase(self, n):
        self.counter += n

    def decrease(self, n):
        self.counter = self.counter - n


# 5️⃣ Metodo con parametro
# Modifica Contatore per accettare:
# incrementa(n)
# decrementa(n)
c = Contatore()
c.increase(10)
c.decrease(5)


# 6️⃣ Classe Prodotto
# Attributi:
# - nome
# - prezzo
# Metodo:
# - applica_sconto(percentuale)
class Prodotto:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_Discount(self, percent):
        discount = self.price * percent / 100
        self.price -= discount


pr1 = Prodotto("Telefono", 800)
print(pr1.price)
pr1.apply_Discount(50)
print(pr1.price)
