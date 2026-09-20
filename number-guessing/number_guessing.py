import random

secret = random.randint(1,100)
guess_counter = 0

print("1-100 arasında sayı tahmin etme oyunu: ")

while True:
    try:
        guess = int(input("Tahmininizi giriniz: "))
    except ValueError: 
        print("Lütfen sayı giriniz")
        continue

    if guess < 1 or guess > 100:
        print("Lütfen geçerli bir değer giriniz.")
        continue

    guess_counter += 1

    if guess < secret:
        print("tahmininizi arttırın")
        

    elif guess > secret:
        print("tahmininizi küçültün")
        
    else:
        
        print(f"Tebrikler Tahmininiz Doğru \nGizli Sayı = {secret}\nAdım sayısı = {guess_counter}")
        break