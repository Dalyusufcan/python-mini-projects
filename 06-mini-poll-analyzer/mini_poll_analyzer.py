def collect_choices():
    choices = []

    while True:
        user_choice = input("Seçim: ").strip().lower().replace("i̇", "i")

        if user_choice == "bitir":
            break

        elif user_choice == "":
            print("boş seçim olmaz")
            continue
        
        choices.append(user_choice)

    return choices


def count_frequency(choices):
    frequency = {}

    for choice in choices:
        if choice not in frequency:
            frequency[choice] = 1

        else:
            frequency[choice] += 1

    return frequency


def find_most_selected(frequency):

    max_frequency = 0   
    most_selected = []

    for choice in frequency:

        if frequency[choice] > max_frequency:
            most_selected = [choice]
            max_frequency = frequency[choice]

        elif frequency[choice] == max_frequency:
            most_selected.append(choice)

    return most_selected, max_frequency


def main():
    choices = collect_choices()
    frequency = count_frequency(choices)
    most_selected, max_frequency = find_most_selected(frequency)

    print("\n--- Poll Analysis ---")
    print(f"Toplam oy: {len(choices)}")
    print(f"Benzersiz seçenek sayısı: {len(frequency)}")
    print(f"Frekanslar: {frequency}")
    print(f"En çok seçilen seçenek/seçenekler: {most_selected}")
    print(f"Maksimum oy sayısı: {max_frequency}")


if __name__ == "__main__":
    main()