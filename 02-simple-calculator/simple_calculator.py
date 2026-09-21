while True:   
    while True:
        try:
            first_number = float(input("hesaplamak istediğiniz ilk sayıyı giriniz: "))
        except ValueError:
            print("Lütfen sayı giriniz. ")
            continue
        break

    while True:
        operator = input("işlem seçiniz:")
        if operator not in ("+", "-", "*", "/"):
            print("Lütfen geçerli işlem giriniz")
            continue
        break

    while True:
        try:
            second_number = float(input("ikinci sayıyı giriniz:"))
        except ValueError:
            print("Lütfen sayı giriniz. ")
            continue
        if operator == "/" and second_number == 0:
            print("Lütfen başka bir sayı giriniz")
            continue
        break

    if operator == "+":
        result = first_number + second_number

    elif operator == "-":
        result = first_number - second_number

    elif operator == "*":
        result = first_number * second_number

    elif operator == "/":
        result = first_number / second_number
    
    print(f"sonuç: {result}")

    while True:
        replay = input("tekrar hesaplamak ister misiniz(e/h)").lower()
        if replay == "e" or replay == "h":
            break
        print("Lütfen sadece e veya h giriniz.")

    if replay == "h": 
        break
            