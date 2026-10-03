def clean_text(text):
    text = text.lower()

    punctuation = ".,!?;:"
    for punct in punctuation:
        text = text.replace(punct, " ")

    return text


def count_frequency(words):
    frequency = {}

    for word in words:
        if word not in frequency:
            frequency[word] = 1
        else:
            frequency[word] += 1

    return frequency


def find_longest_words(words):
    longest_words = []
    max_length = 0

    unique_words = set(words)

    for word in unique_words:
        if len(word) > max_length:
            max_length = len(word)
            longest_words = [word]

        elif len(word) == max_length:
            longest_words.append(word)

    return longest_words, max_length


def find_most_frequent_words(frequency):
    max_frequency = 0
    most_frequent_words = []
    for word in frequency:
        if frequency[word] > max_frequency:
            most_frequent_words = [word]
            max_frequency = frequency[word]
        elif frequency[word] == max_frequency:
            most_frequent_words.append(word)

    return most_frequent_words, max_frequency


def count_characters(words):
    character_count = 0

    for word in words:
        character_count = character_count + len(word)

    return character_count


def main():
    while True:
        text = input("analiz edilmesini istediğiniz metni giriniz: ")
        
        if not text.strip():
            print("Metin boş olamaz.")
            continue
        else:
            break
    
    text = clean_text(text)

    words = text.split()

    frequency = count_frequency(words)
    character_count = count_characters(words)

    longest_words, max_length = find_longest_words(words)
    most_frequent_words, max_frequency = find_most_frequent_words(frequency)
    
    print("\n--- Text Analysis ---")
    print(f"Kelime sayısı: {len(words)}")
    print(f"Benzersiz kelime sayısı: {len(set(words))}")
    print(f"Karakter sayısı: {character_count}")
    print(f"En uzun kelime/kelimeler: {longest_words}")
    print(f"En uzun kelime uzunluğu: {max_length}")
    print(f"En sık geçen kelime/kelimeler: {most_frequent_words}")
    print(f"Maksimum tekrar sayısı: {max_frequency}")
    print(f"Kelime frekansları: {frequency}")


if __name__ == "__main__":
    main()