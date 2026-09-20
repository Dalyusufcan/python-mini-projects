import random

print("Sayı tahmin etme oyunu: ")

while True:
    while True:
        zorluk = input("Lütfen zorluk seçimi yapınız: (k/n/z): ").lower()

        if zorluk == "k" or zorluk == "n" or zorluk == "z":
            break
        else:
            print("Lütfen geçerli değer giriniz.")
    if zorluk == "k":
        max_number = 50
    elif zorluk == "n":
        max_number = 100
    elif zorluk == "z":
        max_number = 500

    print(f"1-{max_number} arasında sayı tahmin ediniz: ")
    secret = random.randint(1,max_number)
    guess_counter = 0
    
    while True:
        try:
            guess = int(input("Tahmininizi giriniz: "))
        except ValueError: 
            print("Lütfen sayı giriniz")
            continue

        if guess < 1 or guess > max_number:
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

    while True:
        cevap = input("Tekrar oynamak ister misiniz? (e/h): ").lower()

        if cevap == "e" or cevap == "h":
            break

        print("Lütfen sadece e veya h giriniz.")
    if cevap == "h": 
        break