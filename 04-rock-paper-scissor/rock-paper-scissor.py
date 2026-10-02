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


def ask_replay():
    while True:
        replay = input("Tekrar oynamak ister misiniz (e/h): ").strip().lower()

        if replay == "e":
            return True
        elif replay == "h":
            return False
        else:
            print("Lütfen e veya h giriniz.")


def main():
    
    choices = ["taş", "kağıt", "makas"]   
    while True:

        computer_choice = random.choice(choices)

        while True:
            user_choice = input("Seçiminizi giriniz: ").strip().lower()

            if user_choice not in choices:
                print("lütfen taş, kağıt yada makas yazın")
                continue
            break

        game_result = result(user_choice, computer_choice)
        print(f"rakibin seçimi: {computer_choice}")
        print(game_result)

        if not ask_replay():
            break


if __name__ == "__main__":
    main()