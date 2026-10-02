import random


def result(user_choice, computer_choice):
    if computer_choice == user_choice:
        return "Berabere"

    elif (
            (user_choice == "taş" and computer_choice == "makas")
        or  (user_choice == "kağıt" and computer_choice == "taş")
        or  (user_choice == "makas" and computer_choice == "kağıt")
    ):
        return "Galibiyet"

    else:
        return "Kaybettiniz"


choices = ["taş", "kağıt", "makas"]

computer_choice = random.choice(choices)

user_choice = input("Seçiminizi giriniz: ").strip().lower()

game_result = result(user_choice, computer_choice)
print(f"rakibin seçimi: {computer_choice}")
print(game_result)