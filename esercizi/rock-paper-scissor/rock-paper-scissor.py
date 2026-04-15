import random

possible_choices = ["sasso", "carta", "forbice"]

win_map = {"sasso": "forbice", "forbice": "carta", "carta": "sasso"}

user_score = 0
computer_score = 0

while True:
    cmp_choice = random.choice(possible_choices)
    user_choice = (
        input(f"Scegli {",".join(possible_choices)}. Scrivi esc per uscire. -> ")
        .lower()
        .strip()
    )

    if user_choice == "esc":
        print("Partita terminata!")

        if user_score == computer_score:
            print(f"La partita finisce in parità {user_score} a {computer_score}")
        elif user_score > computer_score:
            print(f"Hai vinto tu la partita con {user_score} punti")
        else:
            print(f"Il computer vince la partita con {computer_score} punti")

        break

    if user_choice not in possible_choices:
        print(f"Inserisci un valore valido tra: {",".join(possible_choices)}")
        continue

    print(f"CMP ha scelto: {cmp_choice} - TU hai scelto: {user_choice}")
    if user_choice == cmp_choice:
        print("Patta, riprova!")
    elif win_map[user_choice] == cmp_choice:
        user_score += 1
        print("Hai vinto !")
    else:
        computer_score += 1
        print("Vince il computer !")

    print(f"Punteggio. CMP:{computer_score} - TU:{user_score}")
