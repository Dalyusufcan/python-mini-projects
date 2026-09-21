def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
        except ValueError:
            print("Lütfen sayı giriniz. ")
            continue

        return number


def get_operator():
        while True:
            operator = input("işlem seçiniz:")
            if operator not in ("+", "-", "*", "/"):
                print("Lütfen geçerli işlem giriniz")
                continue

            return operator


def calculate(first_number, operator, second_number):
    if operator == "+":
        result = first_number + second_number

    elif operator == "-":
        result = first_number - second_number

    elif operator == "*":
        result = first_number * second_number

    elif operator == "/":
        result = first_number / second_number

    return result


def ask_replay():
    while True:
        replay = input("tekrar hesaplamak ister misiniz(e/h)").lower()
        if replay == "e" or replay == "h":
            return replay
        print("Lütfen sadece e veya h giriniz.")


def main():
    while True:
        first_number = get_number("Hesaplamak istediğiniz ilk sayıyı giriniz: ")
        operator = get_operator()

        while True:
            second_number = get_number("İkinci sayıyı giriniz: ")

            if operator == "/" and second_number == 0:
                print("Sıfıra bölme işlemi yapılamaz.")
                continue

            break

        result = calculate(first_number, operator, second_number)
        print(f"Sonuç: {result}")

        replay = ask_replay()

        if replay == "h":
            break


if __name__ == "__main__":
    main()