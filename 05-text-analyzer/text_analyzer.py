text = input("Metni giriniz: ")

words = text.split()
print(words)

longest_words = []
max_length = 0

unique_words = set(words)
for word in unique_words:
    if len(word) > max_length:
        max_length = len(word)
        longest_words = [word]

    elif len(word) == max_length:
        longest_words.append(word)

print(f"en uzun kelimeler: {longest_words}")
print("Kelime sayısı:", len(words))