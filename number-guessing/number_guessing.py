import random

secret = random.randint(1,100)
guess_counter = 0

while True:
    guess = int(input("Tahmininizi giriniz: "))

    if guess < secret:
        print("tahmininizi arttırın")
        guess_counter += 1

    elif guess > secret:
        print("tahmininizi küçültün")
        guess_counter += 1
    else:
        guess_counter += 1
        print(f"Tebrikler Tahmininiz Doğru \nGizli Sayı = {secret}\nAdım sayısı = {guess_counter}")
        break